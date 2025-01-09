import os
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.environ.get("GOOGLE_API_KEY"))

def readData(path):
    df = pd.read_csv(path)
    return df


def getAgent(data):
    agent = create_pandas_dataframe_agent(llm, data, verbose=True , allow_dangerous_code=True)
    return agent