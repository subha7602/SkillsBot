import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

RESUME_DIRECTORY = "resumes/"  # Path to preloaded resumes

def load_all_resumes():
    """
    Loads all resumes from the 'resumes/' directory, extracts text, and splits into chunks.
    Returns: List of document chunks.
    """
    documents = []
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,  # Define chunk size
        chunk_overlap=20,  # Define overlap for better context retention
        separators=["\n\n", "\n", " ", ""]
    )

    for file_name in os.listdir(RESUME_DIRECTORY):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(RESUME_DIRECTORY, file_name)
            loader = PyPDFLoader(file_path)
            docs = loader.load()
            documents.extend(docs)

    chunks = text_splitter.split_documents(documents)
    return documents, chunks
