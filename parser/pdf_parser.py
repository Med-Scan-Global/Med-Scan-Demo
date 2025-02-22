from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document


class PDFParser:

    def load_pdf(self, file_path: str) -> list[Document]:
        '''
        Loads a PDF file and returns a list with all the pages as documents

        '''
        loader = PyMuPDFLoader(file_path)
        return loader.load()

    def split_text(self, documents: list[Document]) -> list[Document]:
        '''
        Splits the text of the documents into chunks of 800 characters with 80 characters of overlap
        '''
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800, chunk_overlap=80)
        return text_splitter.split_documents(documents)
