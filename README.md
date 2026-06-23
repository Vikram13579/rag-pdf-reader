# Terminal PDF RAG Agent

A lightweight, terminal-based Retrieval-Augmented Generation (RAG) application that allows you to chat with your PDF documents. It uses local embeddings to build a vector database and Anthropic's Claude API to generate answers based strictly on the document context.

## Features
* **Local Document Processing:** Parses and chunks PDFs locally using PyMuPDF.
* **Local Vector Database:** Generates embeddings using `sentence-transformers` and stores them persistently on disk using `ChromaDB`.
* **Terminal Interface:** Simple command-line loop for fast querying.
* **Hallucination Prevention:** Prompts Claude to answer *only* using the retrieved context.

## Prerequisites
* Python 3.8+
* An Anthropic API Key

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install pymupdf chromadb sentence-transformers anthropic
   ```

4. **Set your Anthropic API Key:**
   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```

## Usage

This agent works in two distinct steps: ingesting the knowledge base, and querying it.

### Step 1: Ingest a PDF
Run the ingestion script and pass the path to your PDF file. This parses the text, splits it into overlapping chunks, generates vector embeddings, and saves them to a local `./chroma_db` directory.

```bash
python ingest.py path/to/your_document.pdf
```

### Step 2: Query the Document
Once the document is ingested, start the interactive terminal chat. The script retrieves the most relevant chunks from ChromaDB and sends them to Claude to formulate an answer.

```bash
python ask.py
```
*(Type your questions at the prompt, and type 'quit' to exit).*

## Project Structure
* `ingest.py`: Handles PDF parsing, text chunking, and embedding generation into ChromaDB.
* `ask.py`: The terminal chat interface that retrieves context and queries the Anthropic API.
* `chroma_db/`: Auto-generated directory containing the persistent local vector database.

## Future Improvements
* Add support for multiple document types (TXT, Markdown, Word).
* Implement conversation memory (storing chat history for follow-up questions).
* Add a configuration file to easily tweak chunk sizes, overlap, and model selection.

README.md
Displaying README.md.
