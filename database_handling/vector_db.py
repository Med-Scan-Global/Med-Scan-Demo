from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma


class VectorDatabase:
    def __init__(self, define_path: str):
        self.path = define_path

    def create_vector_db(self, chunks_with_ids: list[Document]):
        '''
        Creates a vector database from a list of documents with ids

        '''
        db = Chroma(persist_directory=self.path,
                    embedding_function=get_embedding_function())
