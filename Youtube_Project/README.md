# 🎥 RAG-Based YouTube Question Answering System

A powerful **Retrieval-Augmented Generation (RAG)** pipeline that allows you to ask intelligent questions about any YouTube video using **LLMs + Vector Search**.

---

## 🚀 Features

✨ Extract transcripts directly from YouTube
✨ Convert text into semantic embeddings
✨ Store and search using FAISS vector database
✨ Retrieve relevant context for any query
✨ Generate accurate answers using Groq LLM
✨ Clean and structured output formatting

---

## 🧠 How It Works

```
User Query
    ↓
Retriever (FAISS Vector Search)
    ↓
Relevant Chunks (Context)
    ↓
Prompt Template
    ↓
LLM (Groq - LLaMA3)
    ↓
Final Answer
```

---

## 🏗️ Project Structure

```
Rag/
│
├── Youtube_Project/
│   ├── Youtube_Transcript.ipynb
│   └── faiss_index/        # Ignored
│
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Guide

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd Rag
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

## ▶️ Usage

Run the notebook:

```
Youtube_Project/rag_using_langchain.ipynb
```

Ask questions like:

* “Summarize the video”
* “What is nuclear fusion?”
* “Explain the main idea”

---

## 🧪 Example Output

> The system retrieves relevant chunks from the transcript and generates a structured, meaningful response using the LLM.

---

## ⚠️ Important Notes

🚫 Do NOT push:

* `.env`
* `env/`
* `faiss_index/`
* large model files

---

## 🧠 Tech Stack

* **LangChain** – Pipeline orchestration
* **HuggingFace** – Embeddings
* **FAISS** – Vector search
* **Groq (LLaMA3)** – LLM inference
* **YouTube Transcript API** – Data extraction

---

## 🔮 Future Improvements

* 🌐 Streamlit / Web UI
* 📚 Multi-video support
* 🔍 Hybrid search (BM25 + embeddings)
* 🧠 Better chunking strategies

---

## 👨‍💻 Author

**Mazhar Sayed**
M.Tech CSE – IIIT Delhi

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
