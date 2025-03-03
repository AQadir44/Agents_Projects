import streamlit as st
from utils import load_wikipedia, qa_reader , store_wikipedia

# Streamlit interface
st.title("Wikipedia-like Q&A System")

# db = ""
# # Input for the URL
# web_url = st.sidebar.text_input("Enter a URL to Wikipedia-like article")

# Check if content has been loaded before (using session state)
if 'content_loaded' not in st.session_state:
    st.session_state.content_loaded = False

# Input for the URL
web_url = st.text_input("Enter a URL to Wikipedia-like article:")

if web_url and not st.session_state.content_loaded:
    # Load and store the Wikipedia content as soon as the URL is entered
    with st.spinner("Loading and processing content..."):
        all_splits = load_wikipedia(web_url)
        db = store_wikipedia(all_splits)
        st.session_state.db = db  # Store the FAISS database in session state
        st.session_state.content_loaded = True
        st.success("Content loaded and indexed.")

# Only show question input once content is loaded
if st.session_state.content_loaded:
    question = st.text_input("Ask a question related to the article:")

    if question:
        # Generate and display the answer
        with st.spinner("Generating answer..."):
            answer = qa_reader(question, st.session_state.db)
            st.write("Answer: ", answer)
