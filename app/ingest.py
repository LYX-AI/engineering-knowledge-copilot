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


def main():
    doc_dir = "data/docs"
    docs = load_text_documents(doc_dir)
    all_chunks = build_chunks(docs)

    print(f"Loaded {len(docs)} documents.")
    print(f"Built {len(all_chunks)} chunks.\n")

    for chunk in all_chunks[:3]:
        print("Source:", chunk["source"])
        print("Chunk ID:", chunk["chunk_id"])
        print("Length:", chunk["length"])
        print("Text Preview:", chunk["text"][:150])
        print("-" * 50)


if __name__ == "__main__":
    main()
