# Normal Case #

from booking import book_room
import pytest

def test_book_available_room():
    assert book_room(
        True,
        "2026-08-27",
        "10:00-11:00",
        "Team Meeting"
    ) == True

# Boundary Case #

def test_book_unavailable_room():
    assert book_room(
        False,
        "2026-08-27",
        "10:00-11:00",
        "Team Meeting"
    ) == False


# error Case #

def test_book_without_meeting_details():
    with pytest.raises(ValueError):
        book_room(
            True,
            "",
            "",
            ""
        )