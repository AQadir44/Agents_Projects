from langchain_community.llms import LlamaCpp

llm = LlamaCpp(
    model_path="model\deepseek-llm-7b-base.Q4_0.gguf",
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
)

question = """
Question: A rap battle between Stephen Colbert and John Oliver
"""
print(llm.invoke(question))