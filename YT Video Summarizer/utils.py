from langchain_community.document_loaders import YoutubeLoader
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             verbose=True,
                             temperature=0.0,
                             google_api_key=os.environ.get("GOOGLE_API_KEY"))




def get_video_transcript(url):
    loader = YoutubeLoader.from_youtube_url(
      url, add_video_info=False,language=['en' , 'urdu']
  )
    content = loader.load()[0].page_content
    return content


# Summarization chain
prompt_template = "Summarize the following content:\n{content}\nSummary:"
prompt = PromptTemplate(input_variables=["content"], template=prompt_template)
chain = LLMChain(llm=llm, prompt=prompt)

# Function to summarize text
def summarize_text(text):
    summary = chain.run(text)
    return summary


# Complete function for summarizing YouTube videos
def summarize_youtube_video(url):
    # Step 1: Get Transcript
    transcript = get_video_transcript(url)
    
    # Step 2: Summarize Transcript
    summary = summarize_text(transcript)
    
    return summary