def retrieve_resumes(query, top_k=5):
    """
    Searches FAISS vector store for relevant resumes based on user query.
    Args:
        query (str): User's search query.
        top_k (int): Number of relevant results to retrieve.
    Returns:
        List of retrieved document chunks.
    """
    return vector_store.similarity_search(query, k=top_k)
