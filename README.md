# LangChain Agentic AI Crash Course - Practice Work & Projects

Welcome to the **LangChain Agentic AI Crash Course** repository! This project compiles all the exercises, practical notebooks, and capstone projects developed during the course. The codebase is managed using the [uv package manager](https://docs.astral.sh/uv/) and explores various facets of Generative AI, Retrieval-Augmented Generation (RAG), Autonomous Agents, Multimodality, Guardrails, and Evaluations.

---

## Repository Quick Setup

This repository uses a modern Python setup powered by `pyproject.toml` and `uv`.

### 1. Prerequisites
- Python 3.11+ (configured for 3.14+ in `pyproject.toml`)
- [uv](https://docs.astral.sh/uv/) installed on your machine.
- API Keys:
  - **Groq API Key** (Get it from [Groq Console](https://console.groq.com))
  - **Google Gemini API Key** (Get it from [Google AI Studio](https://aistudio.google.com/))
  - **Hugging Face Token** (Get it from [Hugging Face Settings](https://huggingface.co/settings/tokens))

### 2. Installation
Clone the repository and install all dependencies:
```bash
# Install dependencies using uv
uv sync
```

### 3. Environment Variables
Copy `.env.example` to `.env` and fill in your keys:
```bash
cp .env.example .env
```
Fill in the values:
```env
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
HF_TOKEN=your_huggingface_token_here
```

---

##  Codebase Structure & Directory Walkthrough

Here is a summary of all the lessons and practice exercises:

| # | Topic / Directory | Description & Key Files | Tech Stack Used |
|---|---|---|---|
| **1** | **[Simple LLM Calling](./1._simple-llm-calling)** | Basic LLM invocation using LangChain wrappers, testing different temperatures, and formatting inputs. | `gemini-2.5-flash`, `gemma-4-31b-it`, `qwen/qwen3-32b`, LangChain |
| **2** | **[Health Analysis](./2._health-analysis)** | Sequential pipeline to extract values from text-based blood reports and generate custom Indian diet plans. Includes a web UI. | Streamlit, Google GenAI |
| **3** | **[Vector Database Basics](./3._vector-db)** | Introduction to vector embeddings and in-memory ChromaDB operations including collection management and queries. | ChromaDB |
| **4** | **[RAG Basics](./4._rag-basics)** | End-to-end RAG system that reads a telecom PDF guide, chunks it, embeds it locally, and answers questions. | `sentence-transformers`, Chroma, Groq |
| **5** | **[Single Agent](./5._single-agent)** | Creating a tool-using AI Agent using custom tools and conversational state memory. | LangGraph checkpointer, Groq |
| **6** | **[Agent Memory](./6_memory)** | Deep dive into conversational memory and troubleshooting checkpoint key errors (`thread_id`). | LangGraph `InMemorySaver`, Groq |
| **7** | **[Multi-Modal Agents](./7._multi-modal)** | Direct extraction of blood report data from PNG images and recommending diets based on visual input. | Llama-4 Vision, LangChain |
| **8** | **[Guardrails & Safety](./8_guardrails)** | Integrating PII middleware to mask credit card numbers and redact emails in tool responses. | LangChain PII Middleware, Groq |
| **9** | **[Agent Evaluation](./9_eval)** | Evaluating agent outputs against a dataset in LangSmith using a custom semantic cosine similarity evaluator. | LangSmith, SentenceTransformers |

---

##  Capstone Projects

This repository features two main interactive capstone projects:

### 🛍️ 10. Conversational Shopping Assistant with Image Search
*Located in: [`./10_project_shopping_agent`](./10_project_shopping_agent)*

An intelligent shopping agent that runs as a **Streamlit Web Application** allowing conversational browsing and automated checkout.
* **Database**: SQLite stores products (e.g. honey, oats) and placed orders.
* **Key Features**:
  * **Multimodal Search**: Upload a product photo (e.g. honey or oats). The agent uses **Llama-4 Vision** to extract attributes (such as whether it is organic) and automatically searches the store database.
  * **Reviews API Integration**: Retrieves and displays star ratings for matching items.
  * **Interactive Ordering**: Employs safety logic ensuring orders are only processed upon explicit double-confirmation.
* **Run application**:
  ```bash
  cd 10_project_shopping_agent
  streamlit run app.py
  ```

###  11. Multi-Source RAG Customer Care Chatbot
*Located in: [`./11_project_telecom_chatbot`](./11_project_telecom_chatbot)*

A Retrieval-Augmented Generation (RAG) assistant for telecom support designed to resolve queries using three consolidated knowledge bases.
* **Multi-Source Ingestion**:
  * **FAQ Database**: Loads static CSV entries into Chroma DB.
  * **Support Tickets**: Retrieves and embeds resolved SQLite tickets.
  * **Telecom User Guides**: Chunks and indexes a comprehensive PDF reference manual.
* **Retriever Logic**: Implements a unified retriever that pulls the top 3 matches from each of the 3 collections to build a context window of 9 documents.
* **Interfaces**: Available as a Command Line Interface (CLI) or a clean Streamlit interface.
* **Run application**:
  ```bash
  cd 11_project_telecom_chatbot
  # Ingest data first
  python ingest_faq.py
  python ingest_tickets.py
  python ingest_pdf.py
  # Start app
  streamlit run app.py
  ```

---

##  Technology Stack Detail

* **Orchestration**: LangChain, LangChain Core, LangChain Community, LangGraph
* **LLM Providers**: Groq API (`qwen/qwen3-32b`, `llama-3.3-70b-versatile`), Google GenAI (`gemini-2.5-flash`, `gemma-4-31b-it`)
* **Vision / Multimodality**: `meta-llama/llama-4-scout-17b-16e-instruct` (via Groq)
* **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2` (running locally via HuggingFace)
* **Vector Store**: ChromaDB (locally persisted)
* **Databases**: SQLite (Orders, Products, Support Tickets)
* **Web UI Framework**: Streamlit
* **Environment & Package Management**: `uv`, `python-dotenv`
* **Evaluation Platform**: LangSmith
