from schemas import Document, Chunk

def chunk_document( document: Document, chunk_size: int = 200, ) -> Document:
    chunks = []
    for start in range(0, len(document.text), chunk_size):
        chunk_text = document.text[start:start + chunk_size]
        chunk = Chunk(
            document_id=document.document_id,
            source=document.source,
            chunk_id=f"document.document_id_chunk_{len(chunks)}",
            text=chunk_text,
            metadata=document.metadata,
        )
        chunks.append(chunk)
    return chunks