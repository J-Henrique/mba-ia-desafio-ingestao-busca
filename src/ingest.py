import os
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

def ingest_pdf():
    document = _load_pdf()
    chunks = _split_document(document)
    store = get_vector_store()
    store.add_documents(chunks)

def get_vector_store():
    return PGVector(
        embeddings=_get_embeddings(),
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True,
    )

def _load_pdf():
    pdf_path = os.getenv("PDF_PATH")
    pdf_full_path = Path(*Path(__file__).parts[:-2]) / pdf_path
    return PyPDFLoader(pdf_full_path).load()

def _split_document(document):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    return splitter.split_documents(document)

def _get_embeddings():
    # return GoogleGenerativeAIEmbeddings(model=os.getenv("GOOGLE_EMBEDDING_MODEL"))
    return OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"))

if __name__ == "__main__":
    ingest_pdf()