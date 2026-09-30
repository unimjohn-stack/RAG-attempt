from schemas import Document, Chunk
from app.chunking.strategies import fixed_size_chunks

def chunk_document( document: Document, chunk_size: int = 200, overlap: int = 0 ) -> list[Chunk]:
    text_chunks = fixed_size_chunks( document.text, chunk_size=chunk_size, overlap=overlap)
    chunks = []
    start = 0
    for index, text in enumerate(text_chunks):
        chunk = Chunk(
            document_id=document.document_id,
            source=document.source,
            chunk_id=f"{document.document_id}_chunk_{len(chunks)}",
            text=text,
            metadata=document.metadata,
        )
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks