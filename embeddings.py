from langchain_community.embeddings import HuggingFaceEmbeddings
import os
print("API KEY:", os.getenv("GOOGLE_API_KEY"))

def get_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings