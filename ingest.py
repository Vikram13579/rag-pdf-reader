import fitz  # PyMuPDF
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./chroma_db")  # persists to disk
collection = client.get_or_create_collection("pdf_rag")

def parse_pdf(path):
    doc = fitz.open(path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk:
            chunks.append(chunk)
    return chunks

def ingest(pdf_path):
    print(f"Parsing {pdf_path}...")
    text = parse_pdf(pdf_path)
    chunks = chunk_text(text)
    embeddings = model.encode(chunks).tolist()

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )
    print(f"Ingested {len(chunks)} chunks.")

if __name__ == "__main__":
    import sys
    ingest(sys.argv[1])  # python ingest.py my_doc.pdf