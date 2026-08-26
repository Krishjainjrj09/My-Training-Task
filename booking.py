# booking.py #

def book_room(room_available, date, time, meeting_details):

    if date == "" or time == "" or meeting_details == "":
        raise ValueError("All meeting details are required")

    if room_available == True:
        return True
    else:
        return False