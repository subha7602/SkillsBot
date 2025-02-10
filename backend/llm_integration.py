import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load environment variables (Groq API Key)
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Initialize embeddings model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

FAISS_INDEX_PATH = "faiss_index"  # Ensure this folder exists

# Load FAISS only if the index exists
if os.path.exists(FAISS_INDEX_PATH):
    vector_store = FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
else:
    raise FileNotFoundError("FAISS index not found. Run `python backend/vector_store.py` first.")

def query_resumes(user_query):
    """Retrieves relevant resumes and answers the query."""
    relevant_docs = vector_store.similarity_search(user_query, k=3)
    relevant_text = "\n\n".join([doc.page_content for doc in relevant_docs])

    # AI prompt for resume-based responses
    template = """
    You are an AI assistant specializing in resume analysis. 
    Analyze relevant resumes to answer the user query.

    **Relevant Resume Sections**:
    {resume_data}

    **User Query**:
    {query}

    **Response**:
    """
    
    prompt = PromptTemplate(input_variables=["resume_data", "query"], template=template)

    # Generate AI response
    chain = prompt | ChatGroq(model_name="mixtral-8x7b-32768")
    response = chain.invoke({"resume_data": relevant_text, "query": user_query})

    return response.content
