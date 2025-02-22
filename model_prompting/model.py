import torch
from langchain_community.llms import Ollama


class Model:
    def __init__(self):
        self.llm = Ollama(model="deepseek-r1:8b")
        self.prompt = "What are the usages of AI in medicine?"

    def query(self) -> str:
        return self.llm.invoke(self.prompt)
