import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Define paths
RESUME_FOLDER = "resumes"  # Folder with preloaded resumes
FAISS_INDEX_PATH = "faiss_index"  # Storage path for FAISS index

# Initialize embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

def create_resume_vector_store():
    """Loads resumes, processes them, and creates a FAISS vector store."""
    all_chunks = []
    
    # Ensure the resumes folder exists
    if not os.path.exists(RESUME_FOLDER):
        raise FileNotFoundError(f"Folder '{RESUME_FOLDER}' not found. Please add resumes.")

    # Process each resume
    for filename in os.listdir(RESUME_FOLDER):
        if filename.endswith(".pdf"):
            file_path = os.path.join(RESUME_FOLDER, filename)
            loader = PyPDFLoader(file_path)
            documents = loader.load()

            # Split text into chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=500, chunk_overlap=50, separators=["\n\n", "\n", " ", ""]
            )
            chunks = text_splitter.split_documents(documents)
            all_chunks.extend(chunks)

    if not all_chunks:
        raise ValueError("No valid resume data found in 'resumes' folder.")

    # Create FAISS index
    vector_store = FAISS.from_documents(all_chunks, embeddings)
    vector_store.save_local(FAISS_INDEX_PATH)
    print(f"FAISS index saved at: {FAISS_INDEX_PATH}")

if __name__ == "__main__":
    create_resume_vector_store()
