import streamlit as st
from utils import  getAgent



st.title("arXiv Research Paper Summarizer")
st.write("Summarize the Research Paper given the paper number")



paper_number = st.text_input("Enter the paper number", )

if paper_number is not None:
    agent = getAgent()
    response = agent.invoke(
    {
        "input": f"Summarize the paper {paper_number} about?",
    }
)
    st.write(response["output"])