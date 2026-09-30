import pytest

from app.chunking.strategies import fixed_size_chunks


def test_fixed_size_chunking():
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    chunks = fixed_size_chunks(
        text,
        chunk_size=10,
        overlap=0,
    )

    assert chunks == [
        "ABCDEFGHIJ",
        "KLMNOPQRST",
        "UVWXYZ",
    ]


def test_chunking_with_overlap():
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    chunks = fixed_size_chunks(
        text,
        chunk_size=10,
        overlap=3,
    )

    assert chunks == [
    "ABCDEFGHIJ",
    "HIJKLMNOPQ",
    "OPQRSTUVWX",
    "VWXYZ",
]


def test_overlap_must_be_smaller_than_chunk_size():
    with pytest.raises(ValueError):
        fixed_size_chunks(
            "hello world",
            chunk_size=10,
            overlap=10,
        )


def test_chunk_size_must_be_positive():
    with pytest.raises(ValueError):
        fixed_size_chunks(
            "hello world",
            chunk_size=0,
        )