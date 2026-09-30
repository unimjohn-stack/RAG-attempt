def fixed_size_chunks(text: str, chunk_size: int = 200, overlap: int = 0) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    if overlap < 0:
        raise ValueError("overlap cannot be negative")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    step = chunk_size - overlap
    start = 0
    while start < len(text):
        chunk = text[start: start + chunk_size]
        chunks.append(chunk)
        start += step
    return chunks