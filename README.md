# AI PDF Chatbot

## Overview

AI PDF Chatbot is a Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents, extract knowledge, generate summaries, and interact with documents through natural language conversations.

The system combines document processing, embeddings, vector search, and Large Language Models (LLMs) to provide accurate and context-aware answers from uploaded PDFs.

---

## Features

### PDF Upload & Processing

* Upload PDF documents
* Extract text from PDFs
* Automatic document preprocessing

### Text Chunking

* Split large documents into manageable chunks
* Optimized for retrieval and semantic search

### Vector Embeddings

* Generate embeddings from document content
* Store embeddings for efficient retrieval

### Semantic Search

* Retrieve relevant document chunks
* Context-aware information retrieval

### AI Chatbot

* Ask questions about uploaded PDFs
* Receive intelligent answers based on document content
* Conversational document interaction

### AI Summarization

* Generate concise summaries of uploaded documents
* Quickly understand large PDFs

### RAG Pipeline

* Retrieval-Augmented Generation architecture
* Improved answer quality using document context

---

## Tech Stack

* Python
* Streamlit
* LangChain
* Groq LLM
* Vector Embeddings
* RAG (Retrieval-Augmented Generation)
* PDF Processing Libraries

---

## Project Structure

AI-PDF-Chatbot/

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

├── embeddings.py

├── llm.py

├── pdf_loader.py

├── rag_chain.py

├── summarizer.py

├── text_splitter.py

└── vector_store.py

---

## Installation

Clone the repository:

git clone https://github.com/Abisheik3112/AI-PDF-Chatbot.git

Navigate to the project directory:

cd AI-PDF-Chatbot

Install dependencies:

pip install -r requirements.txt

Create a .env file and add your API key:

GROQ_API_KEY=your_api_key

Run the application:

streamlit run app.py

---

## Workflow

1. Upload a PDF document
2. Extract and preprocess text
3. Split text into chunks
4. Generate embeddings
5. Store embeddings in vector database
6. Retrieve relevant context
7. Generate answers using LLM
8. Chat with your PDF

---

## Future Enhancements

* Multi-document support
* Chat history memory
* PDF comparison
* Citation and source highlighting
* Hybrid search
* Cloud deployment

---

## Author

Abisheik K

Aspiring AI Engineer & Data Scientist

Built to demonstrate Retrieval-Augmented Generation (RAG), LLM integration, vector search, embeddings, document intelligence, and conversational AI.
