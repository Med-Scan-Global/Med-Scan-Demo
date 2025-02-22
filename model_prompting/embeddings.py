from langchain_community.embeddings.ollama import OllamaEmbeddings


def get_embedding_function():
    return OllamaEmbeddings(model='nomic-embed-text')


if __name__ == "__main__":
    embeddings = get_embedding_function()
    test_embedding = embeddings.embed_query("Test text")
    print(f"Embedding dimension: {len(test_embedding)}")
