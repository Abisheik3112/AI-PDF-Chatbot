from langchain_core.prompts import ChatPromptTemplate

def build_rag_chain(llm, vector_store):

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 4}
    )

    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question using the provided context only.

        Context:
        {context}

        Question:
        {question}
        """
    )

    return {
        "retriever": retriever,
        "prompt": prompt,
        "llm": llm
    }