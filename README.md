# Agentic AI & LangChain Practice

A collection of my practice notebooks, scripts, and applications exploring LangChain, Retrieval-Augmented Generation (RAG), autonomous agents, memory, guardrails, and evaluations.

## Setup

1. **Prerequisites**: Python 3.11+, [uv](https://docs.astral.sh/uv/) package manager.
2. **Install dependencies**:
   ```bash
   uv sync
   ```
3. **Environment**: Copy `.env.example` to `.env` and add your `GROQ_API_KEY`, `GOOGLE_API_KEY`, and `HF_TOKEN`.

## Practice Work Overview

- **[1. Simple LLM Calling](./1._simple-llm-calling)**: Direct model calls using Google Gemini and Groq via LangChain.
- **[2. Health Analysis](./2._health-analysis)**: Extractor and Indian diet advisor pipeline from blood report text files (includes a Streamlit UI).
- **[3. Vector DB Basics](./3._vector-db)**: Basic document ingestion and semantic query operations using ChromaDB.
- **[4. RAG Basics](./4._rag-basics)**: Document loader and text splitter pipeline for answering questions from a PDF using local embeddings.
- **[5. Single Agent](./5._single-agent) & [6. Memory](./6_memory)**: Implementing tools and conversational memory checkpointers.
- **[7. Multi-Modal](./7._multi-modal)**: Interacting with images using Llama-4 Vision to run visual diagnosis and diet recommendations.
- **[8. Guardrails](./8_guardrails)**: Masking and redacting PII (emails, credit cards) using LangChain middleware.
- **[9. Evaluation](./9_eval)**: Automated semantic evaluation of agent runs using LangSmith datasets and cosine similarity.

## Projects

### 🛍️ [10. Conversational Shopping Assistant](./10_project_shopping_agent)
A Streamlit app querying a product SQLite database. Features:
- "Shop by Image" via Llama-4 Vision to identify items.
- Rating lookup via reviews API.
- Double-confirmation checkout.

**Run**: `cd 10_project_shopping_agent && streamlit run app.py`

### 📞 [11. Multi-Source RAG Customer Care Chatbot](./11_project_telecom_chatbot)
A support bot combining FAQ CSV entries, resolved support ticket databases, and user guides to answer customer support queries.

**Run**: Ingest databases and run `streamlit run app.py` in the project folder.
