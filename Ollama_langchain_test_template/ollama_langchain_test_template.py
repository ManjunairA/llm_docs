from langchain_core.prompts import ChatPromptTemplate # type: ignore
from langchain_ollama.llms import OllamaLLM # type: ignore

template = """
Question : {question}
Answer : Answer
"""
prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model = "llama3")

chain = prompt | model
answer = chain.invoke("Who created you")
print(answer)