#1. View Room Availability #

def is_room_available(booked_slots, requested_date, requested_time):

    if requested_date == "" or requested_time == "":
        raise ValueError("Date and time are required")

    requested_slot = (requested_date, requested_time)

    if requested_slot in booked_slots:
        return False
    else:
        return True


