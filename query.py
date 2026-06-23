import chromadb
from sentence_transformers import SentenceTransformer
import anthropic

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("pdf_rag")
claude = anthropic.Anthropic()

def retrieve(question, top_k=4):
    query_vec = model.encode([question]).tolist()
    results = collection.query(query_embeddings=query_vec, n_results=top_k)
    return results["documents"][0]

def ask(question):
    chunks = retrieve(question)
    context = "\n\n---\n\n".join(chunks)

    response = claude.messages.create(
        model="claude-sonnet-4-6",  # <--- Change this line here
        max_tokens=1000,
        messages=[{
            "role": "user",
            "content": f"""Answer the question using ONLY the context below.
If the answer isn't in the context, say "I don't know based on the document."

Context:
{context}

Question: {question}"""
        }]
    )
    return response.content[0].text

if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or 'quit'): ")
        if q.lower() == "quit":
            break
        print("\n" + ask(q))