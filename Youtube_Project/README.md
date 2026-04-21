Here’s your **updated, polished, modern README** based on everything you’ve built (Streamlit UI + RAG + YouTube + debugging + improvements). This will make your repo look **serious + production-ready** 👇

---

# 📺 YouTube Transcript RAG App

A modern **Retrieval-Augmented Generation (RAG)** system that lets you **chat with any YouTube video** using LLMs.

Ask questions, get summaries, and explore video content intelligently — all through a clean Streamlit UI.

---

## 🚀 Features

✨ Extract transcripts from any YouTube video
🌍 Automatic language handling (en, en-IN, en-US, fallback + translation)
🧠 Semantic search using embeddings (HuggingFace)
⚡ Fast retrieval with FAISS vector database
🤖 Intelligent answers using Groq LLM (LLaMA-based)
📄 Auto video summary generation
💬 Chat interface for follow-up questions
🎨 Modern Streamlit UI (clean + responsive)
🔍 Debug visibility (see pipeline steps + logs)

---

## 🧠 How It Works

```
YouTube Video
     ↓
Transcript Extraction (multi-language support)
     ↓
Text Chunking
     ↓
Embeddings (HuggingFace)
     ↓
FAISS Vector Store
     ↓
User Query
     ↓
Retriever (Top-k chunks)
     ↓
Prompt Template
     ↓
LLM (Groq)
     ↓
Final Answer / Summary
```

---

## 🖥️ Demo UI

* 📄 Transcript preview
* 🧠 Auto-generated summary
* 💬 Chat-based Q&A
* 🔎 Expandable debug info

---

## 🏗️ Project Structure

```
Rag/
│
├── Youtube_Project/
│   ├── app.py                         # Streamlit UI
│   ├── Youtube_Transcript_Pipeline.py # Core RAG pipeline
│   ├── Youtube_Transcript_Pipeline.ipynb
│   ├── faiss_index/                   # (ignored)
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Rag.git
cd Rag/Youtube_Project
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
.\env\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 💬 Example Queries

* “Give a detailed summary of this video”
* “What are the key concepts discussed?”
* “Explain nuclear fusion in simple terms”
* “What did the speaker say about AI?”

---

## ⚠️ Important Notes

🚫 Do NOT push these files:

```
.env
env/
faiss_index/
__pycache__/
*.faiss
*.pkl
```

---

## 🧠 Tech Stack

* **LangChain** – RAG pipeline orchestration
* **HuggingFace** – Embeddings
* **FAISS** – Vector similarity search
* **Groq (LLaMA models)** – LLM inference
* **YouTube Transcript API** – Transcript extraction
* **Streamlit** – UI

---

## 🔥 Key Improvements You Added

✔ Multi-language transcript handling (auto-detect + translate)
✔ Fixed API compatibility issues (`fetch()` vs `get_transcript`)
✔ Debug logging (terminal + UI)
✔ Auto summary generation
✔ Clean modular pipeline design
✔ Modern UI with cards + chat interface

---

## 🔮 Future Enhancements

* 🎥 Embed YouTube player inside app
* ⏱️ Timestamp-based navigation
* 📚 Multi-video RAG support
* ⚡ Caching for faster responses
* 🧠 Conversational memory
* 🔍 Hybrid search (BM25 + vector)

---

## 👨‍💻 Author

**Mazhar Sayed**
M.Tech CSE – IIIT Delhi

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it really helps!

---

If you want, I can next:
👉 make this README **with badges + demo GIF + deploy link (super pro level)**
