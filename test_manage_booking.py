import pytest
from manage_booking import manage_booking

def test_modify_booking():
    assert manage_booking(
        True,
        "modify",
        "2026-08-28",
        "11:00-12:00"
    ) == True



# Boundary Case #

def test_cancel_booking():
    assert manage_booking(
        True,
        "cancel"
    ) == True

# Error Case #

def test_modify_booking_without_details():
    with pytest.raises(ValueError):
        manage_booking(
            True,
            "modify",
            "",
            ""
        )