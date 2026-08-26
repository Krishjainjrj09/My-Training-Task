# manage booking #

def manage_booking(booking_exists, action, new_date="", new_time=""):

    if not booking_exists:
        return False

    if action == "modify":
        if new_date == "" or new_time == "":
            raise ValueError("New date and time are required")

        return True

    elif action == "cancel":
        return True

    else:
        raise ValueError("Invalid action")