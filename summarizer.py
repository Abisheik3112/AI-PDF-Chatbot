def summarize_document(llm, docs):

    text = ""

    for doc in docs[:10]:
        text += doc.page_content

    prompt = f"""
    Summarize the following document:

    {text}
    """

    response = llm.invoke(prompt)

    return response.content