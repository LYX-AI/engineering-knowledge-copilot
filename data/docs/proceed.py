import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.utils import load_text_documents, chunk_text


def build_chunks(docs: list[dict]) -> list[dict]:
    all_chunks = []

    for doc in docs:
        filename = doc["filename"]
        content = doc["content"]
        chunks = chunk_text(content)

        for i, chunk in enumerate(chunks):
            chunk_record = {
                "source": filename,
                "chunk_id": f"{filename.replace('.txt', '')}_{i}",
                "text": chunk,
                "length": len(chunk)
            }
            all_chunks.append(chunk_record)

    return all_chunks


def save_chunks_to_json(chunks: list[dict], output_path: str):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)


def main():
    doc_dir = PROJECT_ROOT / "data" / "docs"
    output_path = PROJECT_ROOT / "data" / "processed" / "chunks.json"

    docs = load_text_documents(str(doc_dir))
    all_chunks = build_chunks(docs)
    save_chunks_to_json(all_chunks, str(output_path))

    print(f"Loaded {len(docs)} documents.")
    print(f"Built {len(all_chunks)} chunks.")
    print(f"Saved chunks to: {output_path}\n")

    for chunk in all_chunks[:3]:
        print("Source:", chunk["source"])
        print("Chunk ID:", chunk["chunk_id"])
        print("Length:", chunk["length"])
        print("Text Preview:", chunk["text"][:150])
        print("-" * 50)


if __name__ == "__main__":
    main()
