import torch
from langchain_community.llms import Ollama
from langchain_community.embeddings.ollama import OllamaEmbeddings


class Model:
    def __init__(self):
        self.llm = Ollama(model="deepseek-r1:1.5b")
        self.prompt = "What are the usages of AI?"
        self.device = "mps" if torch.backends.mps.is_available() else "cpu"
        print(f"Using device: {self.device}")

    def query(self) -> str:
        return self.llm.invoke(self.prompt)
