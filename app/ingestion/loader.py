from pathlib import Path
from schemas import Document

def load_txt_file(file_path: str) -> Document:
    path = Path(file_path)
    text = path.read_text(encoding="utf-8")

    return Document(
        document_id=path.stem,
        source=str(path),
        text=text,
        metadata={ "filename": path.name, "file_type": path.suffix, },
    )