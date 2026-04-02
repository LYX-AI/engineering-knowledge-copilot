"""Shared utility helpers.

Planned responsibilities:
- File reading helpers
- Result printing helpers
- General helper utilities
"""
from pathlib import Path

def load_text_documents(doc_dir: str) ->list[dict]:
    docs = []
    for file_path in Path(doc_dir).glob("*.txt"):
        content = file_path.read_text(encoding="utf-8")
        docs.append({"filename": file_path.name, "content": content})
    return docs

def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50) -> list[str]:
    """Splits text into chunks with specified size and overlap."""
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks