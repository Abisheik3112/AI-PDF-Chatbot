import streamlit as st

from utils.helper import save_uploaded_files

from src.pdf_loader import load_pdfs
from src.text_splitter import split_documents
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store
from src.llm import get_llm
from src.summarizer import summarize_document


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI PDF Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

.block-container {
    padding-top: 1rem;
}

[data-testid="stSidebar"] {
    background-color: #161B22;
}

.chat-header {
    text-align: center;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HEADER
# -----------------------------------

st.markdown("""
<div class='chat-header'>
    <h1>🤖 AI PDF Assistant</h1>
    <h4>Chat with your PDF Documents</h4>
</div>
""", unsafe_allow_html=True)

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------------
# SIDEBAR
# -----------------------------------

with st.sidebar:

    st.title("📂 Document Center")

    st.markdown("---")

    uploaded_files = st.file_uploader(
        "Upload PDF Files",
        type=["pdf"],
        accept_multiple_files=True
    )

    process_btn = st.button(
        "🚀 Process Documents",
        use_container_width=True
    )

    st.markdown("---")

    st.info(
        "Upload PDFs and ask questions using AI."
    )

# -----------------------------------
# PROCESS DOCUMENTS
# -----------------------------------

if uploaded_files and process_btn:

    with st.spinner("📚 Processing Documents..."):

        file_paths = save_uploaded_files(uploaded_files)

        docs = load_pdfs(file_paths)

        chunks = split_documents(docs)

        embeddings = get_embeddings()

        vector_store = create_vector_store(
            chunks,
            embeddings
        )

        st.session_state.vector_store = vector_store
        st.session_state.docs = docs
        st.session_state.llm = get_llm()

        st.session_state.chunk_count = len(chunks)
        st.session_state.page_count = len(docs)
        st.session_state.pdf_count = len(uploaded_files)

    st.success("✅ Documents Processed Successfully!")

# -----------------------------------
# WELCOME SCREEN
# -----------------------------------

if "vector_store" not in st.session_state:

    st.markdown("""
    ## 👋 Welcome

    Upload one or more PDF files and click
    **Process Documents**.

    ### Features

    ✅ AI Question Answering

    ✅ PDF Summarization

    ✅ Semantic Search

    ✅ Multi PDF Support

    ---
    """)

# -----------------------------------
# DASHBOARD METRICS
# -----------------------------------

if "vector_store" in st.session_state:

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "📄 PDFs",
        st.session_state.pdf_count
    )

    col2.metric(
        "📚 Pages",
        st.session_state.page_count
    )

    col3.metric(
        "🧩 Chunks",
        st.session_state.chunk_count
    )

# -----------------------------------
# CHAT HISTORY
# -----------------------------------

for role, message in st.session_state.chat_history:

    if role == "User":
        with st.chat_message("user"):
            st.write(message)

    else:
        with st.chat_message("assistant"):
            st.write(message)

# -----------------------------------
# CHAT INPUT
# -----------------------------------

question = st.chat_input(
    "Ask anything about your PDF..."
)

if question:

    if "vector_store" not in st.session_state:

        st.warning(
            "Please process documents first."
        )

    else:

        with st.chat_message("user"):
            st.write(question)

        retriever = (
            st.session_state
            .vector_store
            .as_retriever()
        )

        docs = retriever.invoke(question)

        context = "\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
        Answer the question using the
        provided context.

        Context:
        {context}

        Question:
        {question}
        """

        with st.spinner("🤖 Thinking..."):

            response = (
                st.session_state
                .llm
                .invoke(prompt)
            )

        answer = response.content

        st.session_state.chat_history.append(
            ("User", question)
        )

        st.session_state.chat_history.append(
            ("Assistant", answer)
        )

        with st.chat_message("assistant"):
            st.write(answer)

        with st.expander(
            "📄 Retrieved Context"
        ):

            for i, doc in enumerate(docs):

                st.markdown(
                    f"### Chunk {i+1}"
                )

                st.write(
                    doc.page_content[:500]
                )

# -----------------------------------
# SUMMARY
# -----------------------------------

if (
    "docs" in st.session_state
    and st.button("📝 Generate Summary")
):

    with st.spinner(
        "Generating Summary..."
    ):

        summary = summarize_document(
            st.session_state.llm,
            st.session_state.docs
        )

    st.subheader("📋 Document Summary")

    st.write(summary)

    st.download_button(
        label="⬇ Download Summary",
        data=summary,
        file_name="summary.txt",
        mime="text/plain"
    )

