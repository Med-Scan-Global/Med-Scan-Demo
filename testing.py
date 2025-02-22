import os

from datetime import datetime
from model_prompting.model import Model
from parser.pdf_parser import PDFParser
from database_handling.vector_db import VectorDatabase


def test_parsing():
    parser = PDFParser()
    pages = parser.load_pdf("test_pdfs/testFile.pdf")

    assert len(pages) > 0
    print("Pages is not empty, loaded successfully")
    print("Number of pages: ", len(pages))
    print('--------------------------------')

    assert pages[0].page_content is not None, "Page has no content"
    print("Page has content, as expected")
    print('--------------------------------')

    # print(pages[0].page_content)

    chunks = parser.split_text(pages)
    assert len(chunks) > 0, "Chunks is empty"
    print("Chunks is not empty, split successfully")
    print("Number of chunks: ", len(chunks))
    print('--------------------------------')

    example_chunk = chunks[0]
    assert example_chunk.metadata is not None, "Chunk has no metadata"
    print("Chunk has metadata, as expected")
    print(example_chunk.metadata)
    print('--------------------------------')

    assert example_chunk.page_content is not None, "Chunk has no content"
    print("Chunk has content, as expected")
    # print(chunks[0].page_content)
    print('--------------------------------')

    print(chunks[0].metadata)

    # chunks = parser.chunk_id_creation(chunks)
    # assert len(chunks) > 0, "Chunks is empty"
    # print("Chunk ID creation successful, len(chunks): ", len(chunks))
    # print('--------------------------------')

    # vector_db = VectorDatabase("chroma_db")
    # vector_db.create_vector_database(chunks)
    # print("Vector Database created successfully")
    # print('--------------------------------')


if __name__ == "__main__":
    test_parsing()
