import torch
from langchain_community.llms import Ollama
from langchain_community.embeddings.ollama import OllamaEmbeddings


PROMPT_TEMPLATE = '''
You are a helpful assistant that can answer questions and help with tasks.
Answer the question based only on the following context:
{context}

---
Answer the question based on the above context. {question}
'''


class Model:
    def __init__(self):
        self.llm = Ollama(model="deepseek-r1:1.5b")
        self.prompt = "What are the usages of AI?"
        self.device = "mps" if torch.backends.mps.is_available() else "cpu"
        print(f"Using device: {self.device}")

    def query(self) -> str:
        return self.llm.invoke(self.prompt)
