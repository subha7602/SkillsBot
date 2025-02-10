import streamlit as st
import os
import shutil
from backend.load_resumes import load_all_resumes
from backend.vector_store import create_resume_vector_store
from backend.llm_integration import query_resumes

# Preload and index resumes when the app starts
if "vector_store" not in st.session_state:
    st.session_state.vector_store = create_resume_vector_store()

def render_main_app():
    """
    Renders the main UI for resume upload and analysis.
    """
   

    # Sidebar for uploading resumes
    # with st.sidebar:
    #     st.subheader("📤 Upload New Resume")
    #     uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])

    #     if uploaded_file:
    #         temp_dir = "temp"
    #         os.makedirs(temp_dir, exist_ok=True)
    #         resume_path = os.path.join(temp_dir, uploaded_file.name)

    #         with open(resume_path, "wb") as f:
    #             f.write(uploaded_file.getbuffer())

    #         st.success(f"✅ {uploaded_file.name} uploaded successfully!")

    #         # Move the file to the resumes directory
    #         shutil.move(resume_path, os.path.join("resumes", uploaded_file.name))

    #         # Reprocess resumes
    #         st.session_state.vector_store = create_resume_vector_store()
    #         st.experimental_rerun()  # Refresh UI



