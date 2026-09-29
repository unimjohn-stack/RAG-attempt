from app.ingestion.loader import load_txt_file
from app.chunking.chunker import chunk_document

def main():
    document = load_txt_file("data/documents/networking.txt")

    print("Docuement ID:", document.document_id)
    print("Source:", document.source)
    print("Metadata", document.metadata)
    print("\nCreating chunks...\n")
    chunks = chunk_document(document, chunk_size=200)
    print(f"Total chunks: {len(chunks)}")
    for chunk in chunks:
        print("\n" + "-" * 60)
        print("Chunk ID:", chunk.chunk_id)
        print("Text:")
        print(chunk.text)

if __name__ == "__main__":
    main()