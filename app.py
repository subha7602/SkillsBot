import streamlit as st
from frontend.main_app import render_main_app
from frontend.chat_interface import render_chat_interface

# Set the page layout to wide for better visual presentation
st.set_page_config(page_title="Skills Bot", layout="wide")

def main():
    

    # Sidebar layout
    with st.sidebar:
        st.markdown("<h1 style='text-align: center;font-size:30;'>SKILLS  BOT</h1>", unsafe_allow_html=True)

        # Display logo (if available)
        try:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image("logo.jpg", width=150) 
        except FileNotFoundError:
            st.warning("⚠️ Logo not found! Please add `resume_analyzer_logo.png` to the root folder.")

        st.markdown("---")  # Add a horizontal separator
        st.info("Ask AI-powered queries to analyze employee profiles!")

        render_main_app()

    render_chat_interface()    

# Script execution through the 'main' function
if __name__ == "__main__":
    main()
