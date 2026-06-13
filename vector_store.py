from langchain_chroma import Chroma

def create_vector_store(chunks, embeddings):

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vector_store