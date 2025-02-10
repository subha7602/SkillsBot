import streamlit as st
from backend.llm_integration import query_resumes

def render_chat_interface():
    """
    Renders the chat interface for interacting with the resume AI.
    """
    st.header("💬 Chat with Resume AI")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # User input with a send button
    user_query = st.chat_input("Ask about employee resumes...")

    if user_query:
        response = query_resumes(user_query)
        st.session_state.chat_history.append(("You", user_query))
        st.session_state.chat_history.append(("AI", response))

    # Display chat history
    for sender, message in st.session_state.chat_history:
        with st.chat_message("user" if sender == "You" else "assistant"):
            st.write(message)


