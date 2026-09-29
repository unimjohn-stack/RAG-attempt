from pydantic import BaseModel, Field

class Document(BaseModel):
    document_id: str
    source: str
    text: str
    metadata: dict = Field(default_factory=dict)

class Chunk(BaseModel):
    document_id: str
    source: str
    chunk_id: str
    text: str
    metadata: dict = Field(default_factory=dict)

