import gradio as gr
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Define the prompt template
template = """Question: {question}

Answer: Write a code"""

prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="deepseek-coder")
chain = prompt | model

def generate_code(question):
    response = chain.invoke({"question": question})
    return response

# Create Gradio Interface
iface = gr.Interface(
    fn=generate_code,
    inputs=gr.Textbox(placeholder="Enter your question here..."),
    outputs="text",
    title="Code Generator",
    description="Enter a programming question and get a code response."
)

iface.launch()
