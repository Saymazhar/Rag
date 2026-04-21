import streamlit as st
from Youtube_Transcript_Pipeline import load_data, process_query

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="YouTube RAG", layout="wide")

# -------------------------------
# MODERN UI CSS
# -------------------------------
st.markdown("""
<style>

/* GLOBAL */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #f5f7fb;
    color: #1a1a1a;
    font-family: 'Segoe UI', sans-serif;
}

/* MAIN CARD */
.block-container {
    padding-top: 2rem;
}

/* HEADER */
h1 {
    text-align: center;
    font-weight: 700;
    color: #111;
}

/* SECTION CARDS */
.section-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

/* INPUT */
.stTextInput>div>div>input {
    border-radius: 10px;
    border: 1px solid #ddd;
    padding: 10px;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(45deg, #ff6a00, #ee0979);
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: 600;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
}

/* ALERTS */
[data-testid="stAlert"] {
    border-radius: 10px;
}

/* CHAT */
[data-testid="stChatMessage"] {
    background-color: #ffffff;
    border-radius: 12px;
    padding: 10px;
    margin-bottom: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

/* SUMMARY BOX */
.summary-box {
    background: #ffffff;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #ff6a00;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

/* EXPANDER */
details {
    background: #fafafa;
    padding: 10px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.title("📺 YouTube Transcript RAG App")

# -------------------------------
# SESSION STATE
# -------------------------------
if "processed" not in st.session_state:
    st.session_state.processed = False

if "summary" not in st.session_state:
    st.session_state.summary = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------------
# INPUT SECTION (CARD)
# -------------------------------
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.subheader("🔗 Enter YouTube Video")

    video_url = st.text_input("Paste YouTube URL here")

    if st.button("🚀 Process Video"):
        print("🔹 Button clicked")

        if video_url:
            st.info("⏳ Step 1: Fetching transcript...")

            with st.spinner("Processing video..."):
                try:
                    text = load_data(video_url)

                    st.session_state.processed = True

                    st.success(f"✅ Transcript loaded (length: {len(text)})")

                    with st.expander("📄 Transcript Preview"):
                        st.write(text[:1500])

                    st.info("🧠 Step 2: Generating summary...")

                    summary = process_query("Give a detailed summary of this video")

                    st.session_state.summary = summary

                    st.success("✅ Summary generated 🎉")

                except Exception as e:
                    print("❌ Error:", e)
                    st.error(f"Error: {e}")
        else:
            st.warning("⚠️ Please enter a valid YouTube URL")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# SUMMARY SECTION (CARD)
# -------------------------------
if st.session_state.summary:
    st.markdown('<div class="summary-box">', unsafe_allow_html=True)
    st.markdown("## 📄 Video Summary")
    st.write(st.session_state.summary)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# CHAT SECTION (CARD)
# -------------------------------
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.markdown("## 💬 Ask Questions")

    query = st.chat_input("Ask something about the video...")

    if query:
        print(f"🔹 User query: {query}")

        if not st.session_state.processed:
            st.warning("⚠️ Process video first")
        else:
            with st.spinner("Thinking... 🤖"):
                try:
                    answer = process_query(query)

                    st.session_state.chat_history.append(("user", query))
                    st.session_state.chat_history.append(("bot", answer))

                except Exception as e:
                    print("❌ Query error:", e)
                    st.error(f"Error: {e}")

    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)

    st.markdown('</div>', unsafe_allow_html=True)