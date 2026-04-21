import os
from dotenv import load_dotenv
load_dotenv()

from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# -------------------------------
# Step 1: Get Transcript
# -------------------------------
def get_transcript(video_id):
    try:
        print(f"📥 Fetching transcript for: {video_id}")

        yta = YouTubeTranscriptApi()

        # 🔥 NEW: list available transcripts
        transcript_list = yta.list(video_id)

        print("🌍 Available transcripts:")
        for t in transcript_list:
            print(f" - {t.language} ({t.language_code})")

        # -------------------------------
        # Priority order
        # -------------------------------
        preferred_langs = ["en", "en-IN", "en-US"]

        transcript = None

        # Try preferred English variants
        for lang in preferred_langs:
            try:
                transcript = transcript_list.find_transcript([lang])
                print(f"✅ Using transcript: {lang}")
                break
            except:
                continue

        # If no English found → take any and translate
        if transcript is None:
            print("⚠️ No direct English transcript found, using fallback...")

            transcript = list(transcript_list)[0]

            if transcript.is_translatable:
                print(f"🌐 Translating from {transcript.language_code} → English")
                transcript = transcript.translate("en")

        # Fetch transcript
        transcript_data = transcript.fetch()

        transcript_list_clean = [
            {
                'text': chunk.text,
                'start': chunk.start,
                'duration': chunk.duration
            }
            for chunk in transcript_data
        ]

        text = " ".join([t['text'] for t in transcript_list_clean])

        print(f"✅ Transcript length: {len(text)}")

        return text

    except Exception as e:
        print("❌ Error in transcript:", e)
        return str(e)


# -------------------------------
# Step 2: Build Vector Store
# -------------------------------
def build_vector_store(text):
    print("🔪 Splitting text...")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([text])

    print(f"✅ Total chunks: {len(chunks)}")

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    print("📊 Creating embeddings...")
    vector_store = FAISS.from_documents(chunks, embeddings)

    vector_store.save_local("faiss_index")
    print("💾 FAISS saved")

    return vector_store


# -------------------------------
# Step 3: Load Vector Store
# -------------------------------
def load_vector_store():
    print("📂 Loading FAISS index...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)


# -------------------------------
# Step 4: Query
# -------------------------------
def process_query(query):
    print(f"🤖 Processing query: {query}")

    vector_store = load_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})

    docs = retriever.invoke(query)

    print(f"📄 Retrieved docs: {len(docs)}")

    context = "\n\n".join([doc.page_content for doc in docs])

    print("📌 Context preview:", context[:300])

    llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.2)

    prompt = PromptTemplate(
        template="""
        You are a helpful assistant.

        Use the transcript context below to answer clearly.

        {context}

        Question: {question}
        """,
        input_variables=["context", "question"]
    )

    final_prompt = prompt.invoke({"context": context, "question": query})

    print("📤 Sending to LLM...")

    response = llm.invoke(final_prompt)

    print("✅ Response received")

    return response.content


# -------------------------------
# Step 5: Pipeline
# -------------------------------
def load_data(video_url):
    print("🚀 Starting pipeline...")

    video_id = video_url.split("v=")[-1]
    print(f"🎯 Video ID: {video_id}")

    text = get_transcript(video_id)

    build_vector_store(text)

    print("✅ Pipeline completed")

    return text  # returning transcript for UI debug