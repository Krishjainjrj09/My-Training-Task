# Conference Room Booking System

## Project Overview

The Conference Room Booking System is designed to help employees easily check conference room availability, book rooms, and manage their existing bookings.

The system helps prevent double bookings and scheduling conflicts by allowing employees to select a suitable room based on the required date and time.

## Business Objective

- Provide real-time conference room availability.
- Allow employees to book available rooms.
- Prevent double bookings.
- Allow employees to modify or cancel bookings.
- Provide booking confirmation.
- Improve room utilization and save employees' time.

## Epic

**Centralized Conference Room Booking Management**

The epic focuses on enabling employees to efficiently find, book, modify, and cancel conference rooms through a centralized system.

## User Stories

### US-01: View Room Availability

As an employee, I want to view available conference rooms based on date and time so that I can select a suitable room for my meeting.

### US-02: Book a Conference Room

As an employee, I want to book an available conference room by providing meeting details so that I can reserve the room for my meeting.

### US-03: Manage My Booking

As an employee, I want to modify or cancel my existing booking so that I can manage changes to my meeting schedule.

## Unit Testing

Unit testing is performed using **pytest** to verify that individual functions work as expected.

The tests cover scenarios such as:

- Checking room availability.
- Booking an available conference room.
- Preventing booking when a room is unavailable.
- Validating booking details.
- Managing existing bookings.

## Technologies Used

- Python
- Pytest
- Git
- GitHub
- Visual Studio Code

## Project Structure

```text
Conference-Room-Booking/
│
├── booking.py
├── test_booking.py
├── BRD.md
├── README.md
├── .gitignore
└── requirements.txt
