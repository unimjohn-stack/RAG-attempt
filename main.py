from app.ingestion.loader import load_txt_file
from app.chunking.chunker import chunk_document
from app.chunking.strategies import ( fixed_size_chunks, sentence_aware_chunks)

def main():
    document = load_txt_file("data/documents/networking.txt")

    print("\n== FIXED SIZE ==\n")
    fixed_chunks = fixed_size_chunks(document.text, chunk_size=200, overlap=50,)
    for index, chunk in enumerate(fixed_chunks):
        print(f"\n--- Chunk {index} ---")
        print(chunk)
    print("\n\n=== SENTENCE AWARE === \n")
    sentencechunks = sentence_aware_chunks(document.text, chunk_size=200)
    for index, chunk in enumerate(sentencechunks):
        print(f"\n--- Chunk {index} ---")
        print(chunk)
    # print("Docuement ID:", document.document_id)
    # print("Source:", document.source)
    # print("Metadata", document.metadata)
    # print("\nCreating chunks...\n")
    # chunks = chunk_document(document, chunk_size=200, overlap=50,)
    # print(f"Total chunks: {len(chunks)}")
    # for chunk in chunks:
    #     print("\n" + "-" * 60)
    #     print("Chunk ID:", chunk.chunk_id)
    #     print("Text:")
    #     print(chunk.text)

if __name__ == "__main__":
    main()