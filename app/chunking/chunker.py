from schemas import Document, Chunk

def chunk_document( document: Document, chunk_size: int = 200, overlap: int = 0 ) -> Document:
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")
    
    chunks = []
    start = 0
    while start < len(document.text):
        chunk_text = document.text[start:start + chunk_size]
        chunk = Chunk(
            document_id=document.document_id,
            source=document.source,
            chunk_id=f"{document.document_id}_chunk_{len(chunks)}",
            text=chunk_text,
            metadata=document.metadata,
        )
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks