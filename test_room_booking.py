import pytest
from room_booking import is_room_available


# 1. Everyday Case
def test_room_available():
    booked_slots = [
        ("2026-08-27", "10:00-11:00")
    ]

    assert is_room_available(
        booked_slots,
        "2026-08-27",
        "11:00-12:00"
    ) == True


# 2. Boundary Condition
def test_room_already_booked():
    booked_slots = [
        ("2026-08-27", "10:00-11:00")
    ]

    assert is_room_available(
        booked_slots,
        "2026-08-27",
        "10:00-11:00"
    ) == False


# 3. Error Case
def test_room_invalid_date_time():
    with pytest.raises(ValueError):
        is_room_available(
            [],
            "",
            ""
        )