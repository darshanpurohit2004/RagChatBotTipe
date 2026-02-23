import os
from pinecone import Pinecone
from dotenv import load_dotenv
from flask import Flask, render_template, request
import google.generativeai as genai
import markdown

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# -----------------------------
# Initialize Gemini
# -----------------------------
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


# -----------------------------
# Initialize Flask
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Initialize Pinecone
# -----------------------------
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)


# -----------------------------
# Detect Namespace
# -----------------------------
def detect_namespace(query):
    q = query.lower()
    if "exporter" in q:
        return "exporters", "exporter"
    elif "importer" in q or "buyer" in q:
        return "importers", "importer"
    elif "news" in q or "risk" in q:
        return "global_news", "news"
    else:
        return "exporters", "exporter"


# -----------------------------
# Retrieve From Pinecone
# -----------------------------
def retrieve(namespace, query, top_k=5):

    response = index.search(
        namespace=namespace,
        query={
            "inputs": {"text": query},
            "top_k": top_k
        }
    )

    return response.get("result", {}).get("hits", [])


# -----------------------------
# Build Context For Gemini
# -----------------------------
def build_context(results):
    context = ""
    for r in results:
        fields = r.get("fields", {})
        context += f"""
ID: {r.get('_id')}
Score: {r.get('_score')}
Details: {fields}
------------------------
"""
    return context


# -----------------------------
# Gemini Formatter
# -----------------------------
# -----------------------------
# Gemini Formatter (Improved + Guarded)
# -----------------------------
def generate_answer(user_query, results, record_type):

    # 🚫 If no Pinecone results
    if not results or len(results) == 0:
        return "⚠️ **Not able to answer this query based on available trade data.**"

    context = build_context(results)

    prompt = f"""
You are TIPE AI – Trade Intent Prediction Engine.

User Query:
{user_query}

Record Type:
{record_type}

Retrieved Trade Records:
{context}

IMPORTANT RULES:

1. If retrieved data is NOT relevant to the user query, respond ONLY with:
   "Not able to answer based on available trade intelligence."

2. If relevant, generate a structured professional trade intelligence report.
3.If user entered a number like 3-4 then give only that many answers in the ranked results section. If no number is mentioned then give 5 answers.
4.if a length is menthined like 3-4 then give only that many insights in the strategic insights section. If no number is mentioned then give 5 insights.lines only
STRICT FORMAT:

# 🤖 Trade Intelligence Report

## 🔎 Executive Summary
(2-3 lines summary explaining findings)

## 📊 Ranked Results

For each result:
**Rank X**
- **Entity ID:**
- **Location:**
- **Industry:**
- **Revenue:**
- **Intent Score:**
- **Risk Indicators:**
- **Why Relevant:**

## 📈 Strategic Insights
- Insight 1
- Insight 2
- Insight 3

DO NOT mention raw JSON.
DO NOT output technical metadata.
Keep formatting clean with markdown-style bold headings.
"""

    try:
        response = model.generate_content(prompt)
        output = response.text.strip()

        # 🔍 Safety guard if model ignores instruction
        if "not able" in output.lower():
            return "⚠️ **Not able to answer this query based on available trade data.**"

        return output

    except Exception:
        return "⚠️ **AI processing error. Please try again.**"

# -----------------------------
# Routes
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():

    answer = None

    if request.method == "POST":
        user_query = request.form["query"]

        namespace, record_type = detect_namespace(user_query)
        results = retrieve(namespace, user_query)

        raw_answer = generate_answer(user_query, results, record_type)

        # 🔥 Convert markdown to HTML
        answer = markdown.markdown(raw_answer)

    return render_template("index.html", answer=answer)

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
