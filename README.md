# 🌍 TIPE(Trade Intent Prediction Engine) Intelligence AI
### RAG-Powered Export Intelligence Engine

An AI-powered Trade Intelligence & Intent Prediction Engine for semantic search across exporters, importers, and global trade news — generating structured AI intelligence reports.

---

## 🧠 Architecture

```
User Query
    ↓
Pinecone Semantic Search
    ↓
Top-K Relevant Trade Records
    ↓
Gemini LLM Formatting + Ranking
    ↓
Structured Trade Intelligence Report
```

This follows a **RAG (Retrieval Augmented Generation)** pattern.

---

## ⚡ Tech Stack

| Layer       | Technology              |
|-------------|-------------------------|
| Backend     | Flask                   |
| Vector DB   | Pinecone                |
| LLM         | Gemini 2.5 Flash        |
| Embeddings  | Integrated Pinecone Model |
| Frontend    | HTML + CSS              |
| Architecture| RAG                     |

---

## ✅ Features

- Semantic search using vector embeddings
- Multi-namespace architecture (Exporters / Importers / News)
- Trade intent scoring integration
- Risk factor intelligence (Tariff, War, Currency, Stock Shock)
- AI-ranked results with reasoning
- Markdown → HTML formatted reports
- Dark mode modern UI
- Structured trade intelligence summaries

---

## 📂 Project Structure

```
RagChatBot/
│
├── app.py                # Flask backend
├── templates/
│   └── index.html        # UI
├── requirements.txt
├── .env                  # API keys (NOT committed publicly)
└── README.md
```
## 📸 Screenshots

![Dashboard](https://img.sanishtech.com/u/0183600995b369e65b99f6e6524eaebe.png)

![Report Output](https://img.sanishtech.com/u/532351db941303fea0db13c920091e59.png)---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
PINECONE_API_KEY=your_pinecone_key
PINECONE_INDEX=your_index_name
GEMINI_API_KEY=your_gemini_key
```

---

## 📦 Installation

**1. Clone the repository**
```bash
git clone https://github.com/darshanpurohit20/RagChatBot.git
cd RagChatBot
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the application**
```bash
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

---

## 🔎 Example Queries

- `Top 5 solar exporters in Gujarat`
- `High intent medical device buyers in Asia`
- `Tariff impact on textiles in Europe`
- `Electronics exporters with high revenue`
- `Buyers with strong response probability`

---

## 📊 Sample Output Format

```
🤖 Trade Intelligence Report

## Executive Summary
Brief industry overview...

## Ranked Results

Rank 1
Exporter ID:  EXP_XXXX
Revenue:      $XX,XXX,XXX
Intent Score: 0.87
Risk Factors: Tariff · War · Currency
Why Relevant: Explanation...
```

---

## 🧠 Intelligent Features

**Multi-Namespace Retrieval**
- `exporters`
- `importers`
- `global_news`

**Risk Intelligence Layer**
- Tariff impact
- Stock market shock
- War risk
- Natural calamity risk
- Currency shift

**Trade Intent Prediction Signals**
- Intent score
- Hiring growth
- Funding events
- Engagement spikes
- Response probability

---

## 🎨 UI Features

- Dark mode professional dashboard
- Structured AI reports
- Clean SaaS-style layout
- Markdown rendering for bold & headings

---

## 🏆 Why This Project Matters

Global trade data is noisy and fragmented. This system:

- Converts structured CSV trade datasets into semantic vectors
- Enables intelligent natural language querying
- Adds AI reasoning over raw trade records
- Produces business-ready intelligence reports

> This is not just search. **This is AI-powered trade decision intelligence.**

---

## 📈 Future Improvements

- [ ] Chat history
- [ ] User authentication
- [ ] Trade opportunity scoring engine
- [ ] Visualization dashboard
- [ ] API deployment
- [ ] Docker containerization
- [ ] Cloud deployment (GCP / AWS)

---

## 👨‍💻 Author

**Darshan Purohit**  
AI · Trade Intelligence · RAG Systems · LLM Applications  
GitHub: [github.com/darshanpurohit20](https://github.com/darshanpurohit20)

---

*If you found this useful, give it a ⭐ on GitHub!*
