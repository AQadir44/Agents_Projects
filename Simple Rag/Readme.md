# DeepSeek-Powered Q&A App with Streamlit

This project demonstrates how to build an interactive Q&A app using Streamlit and DeepSeek that allows users to input a URL to a Wikipedia-like article and ask questions about the content. The app processes the article, stores its content in a FAISS index, and answers user queries based on the indexed data.

## Features
Wikipedia URL Input: Users can input a URL to a Wikipedia-like article, and the app will load and process its content.
Efficient Content Retrieval: Using DeepSeek with a FAISS index, the app retrieves the most relevant sections of the article based on user queries.
Q&A Generation: Once the content is loaded, users can ask questions, and the app provides answers using the indexed content.
Session State: The app uses Streamlit’s session state to ensure content is only loaded and processed once, improving performance.
Requirements
To run the project, you need the following Python libraries. Instead of installing manually, you can install them all using requirements.txt:

## Requirements:
streamlit: For building the web interface.
faiss-cpu or faiss-gpu: For indexing and searching the article content.
sentence-transformers: For generating embeddings of article chunks.
requests: For fetching the Wikipedia-like article from the URL.
beautifulsoup4: For HTML parsing if the URL is HTML-based.
transformers: For text generation using models like T5 or GPT-2.

## Installation
Clone the repository to your local machine:


```git clone https://github.com/AQadir44/Agents_Projects.git```

```cd simple-rag```
Install the dependencies from the requirements.txt file:


```pip install -r requirements.txt```

Run the Streamlit app:


```streamlit run app.py ```

Open the app in your browser by navigating to the URL provided by Streamlit (typically http://localhost:8501).

## How It Works
URL Input: Users enter a Wikipedia-like article URL in the input field.
Content Loading: The app fetches and processes the content, chunking it into smaller pieces for better querying.
FAISS Indexing: After the content is split into chunks, FAISS is used to index the chunks for fast retrieval.
Ask Questions: Users can type questions related to the article, and the app uses DeepSeek to find the most relevant content and generate an answer using a T5 or GPT-2 model.
Answer Display: The app displays the generated answer to the user.

Contributing
Feel free to fork the repository and contribute improvements, bug fixes, or new features. Please follow standard GitHub workflows (fork, create a branch, make changes, and create a pull request).