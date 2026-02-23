import os
from pinecone import Pinecone
from dotenv import load_dotenv
from flask import Flask, render_template, request

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

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
# Build Raw Output
# -----------------------------
def build_output(results):
    if not results or len(results) == 0:
        return "No results found for your query."

    output = ""
    for r in results:
        fields = r.get("fields", {})
        output += f"""
ID: {r.get('_id')}
Score: {r.get('_score')}
Details: {fields}
------------------------
"""
    return output


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

        answer = build_output(results)

    return render_template("index.html", answer=answer)

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
