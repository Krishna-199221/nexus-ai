import pytest

from app.services.chunking import chunk_text


def test_chunk_text_splits_long_text():
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    chunks = chunk_text(
        text,
        chunk_size=10,
        chunk_overlap=2,
    )

    assert chunks == [
        "ABCDEFGHIJ",
        "IJKLMNOPQR",
        "QRSTUVWXYZ",
    ]


def test_chunk_text_returns_empty_for_empty_text():
    assert chunk_text("") == []
    assert chunk_text("   ") == []


def test_chunk_text_returns_short_text_as_one_chunk():
    result = chunk_text(
        "NEXUS AI",
        chunk_size=100,
        chunk_overlap=20,
    )

    assert result == ["NEXUS AI"]


def test_chunk_text_rejects_invalid_chunk_size():
    with pytest.raises(
        ValueError,
        match="chunk_size must be greater than 0",
    ):
        chunk_text("NEXUS AI", chunk_size=0)


def test_chunk_text_rejects_negative_overlap():
    with pytest.raises(
        ValueError,
        match="chunk_overlap cannot be negative",
    ):
        chunk_text("NEXUS AI", chunk_size=10, chunk_overlap=-1)


def test_chunk_text_rejects_overlap_larger_than_chunk_size():
    with pytest.raises(
        ValueError,
        match="chunk_overlap must be smaller than chunk_size",
    ):
        chunk_text("NEXUS AI", chunk_size=10, chunk_overlap=10)
