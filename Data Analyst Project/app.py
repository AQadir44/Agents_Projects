import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from utils import readData , getAgent
# st.sidebar.title("Data Analyst Bot")
# st.title("Data Insights Bot: Your AI-Driven Analytics Assistant")

# st.sidebar.

# Title of the app
st.title("Data Insights Bot: Your AI-Driven Analytics Assistant")

# Description of the app
st.write("""
Welcome to the Data Insights Bot. This tool helps you analyze your data and get insights quickly.
You can upload your data file, and the bot will generate basic statistics and visualizations and also help you further.
""")

# File upload widget
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# Check if the file is uploaded
if uploaded_file is not None:
    # Read the data
    df = readData(uploaded_file) 
    st.sidebar.title("Generate basic statistics and visualizations")
    # Show the data preview
    st.sidebar.write("Data Preview:")
    st.sidebar.dataframe(df.head())
    
    # Show basic statistics
    st.sidebar.write("Basic Statistics:")
    st.sidebar.write(df.describe())
    
    # Show the data types
    st.sidebar.write("Data Types:")
    st.sidebar.write(df.dtypes)
    
    # Generate visualizations
    st.sidebar.write("Data Visualizations:")
    
    # Column selection for plot
    selected_column = st.sidebar.selectbox("Select a column to visualize", df.columns)
    
    # Plot the selected column's histogram
    st.sidebar.bar_chart(df[selected_column].value_counts())
    


    agent = getAgent(df)


    # Get user input
    user_input = st.chat_input("Ask a question about your data:")
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)

    # Generate response
   
        response = agent.run(user_input)
        with st.chat_message("assistant"):
            st.write(response)
    
    # Footer with additional instructions or contact
    st.sidebar.markdown("---")
    st.sidebar.markdown("Built with Streamlit ❤️")