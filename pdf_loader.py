from langchain_community.document_loaders import PyPDFLoader

def load_pdfs(pdf_files):

    documents = []

    for pdf in pdf_files:
        loader = PyPDFLoader(pdf)
        docs = loader.load()
        documents.extend(docs)

    return documents