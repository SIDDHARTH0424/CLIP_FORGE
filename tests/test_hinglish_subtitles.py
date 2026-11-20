import pytest

pytest.importorskip("indic_transliteration")

from subtitles import _collect_word_blocks


def _words_from_blocks(blocks):
    return [word for block in blocks for word in block]


def test_hindi_transcript_is_romanized_without_changing_timestamps():
    transcript = {
        "language": "hi",
        "segments": [{
            "words": [
                {"word": " नमस्ते", "start": 1.0, "end": 1.5},
                {"word": " world", "start": 1.5, "end": 2.0},
            ],
        }],
    }

    words = _words_from_blocks(
        _collect_word_blocks(transcript, 0, 5, max_chars=100)
    )

    assert words[0]["word"] == "namaste"
    assert words[1]["word"] == "world"
    assert words[0]["start"] == 1.0
    assert words[0]["end"] == 1.5
    assert words[1]["start"] == 1.5
    assert words[1]["end"] == 2.0


def test_english_transcript_is_not_transliterated():
    transcript = {
        "language": "en",
        "segments": [{
            "words": [
                {"word": " नमस्ते", "start": 1.0, "end": 1.5},
            ],
        }],
    }

    words = _words_from_blocks(
        _collect_word_blocks(transcript, 0, 5, max_chars=100)
    )

    assert words[0]["word"] == "नमस्ते"


def test_manually_edited_hindi_words_are_preserved():
    transcript = {
        "language": "hi",
        "_preserve_word_text": True,
        "segments": [{
            "words": [
                {"word": "Namaste", "start": 1.0, "end": 1.5},
                {"word": " Dosto", "start": 1.5, "end": 2.0},
            ],
        }],
    }

    words = _words_from_blocks(
        _collect_word_blocks(transcript, 0, 5, max_chars=100)
    )

    assert [word["word"] for word in words] == ["Namaste", "Dosto"]
