from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import ArxivAPIWrapper
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent 
from langchain_core.tools import Tool
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             verbose=True,
                             temperature=0.0,
                             google_api_key=os.environ.get("GOOGLE_API_KEY"))

arvix_tool = ArxivAPIWrapper()

tools = [
  
    Tool(
        name="Research Summarizer",
        func=arvix_tool.run,
        description="useful for when you need to summarize the paper",
    )
]

prompt = hub.pull("hwchase17/react")

def getAgent():
    
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor