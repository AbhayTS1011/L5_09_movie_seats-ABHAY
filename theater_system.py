"""Manage seat reservations for a small movie theater."""

import hashlib
import json

SHOWS = {
    "SHOW-1": {"title": "Interstellar", "seats": 20, "booked": []},
    "SHOW-2": {"title": "Dangal", "seats": 10, "booked": []},
}


def reserve_seat(show_id, seat_number, system_logs=None):
    """Reserve a valid seat and record the result in the supplied log."""
    if system_logs is None:
        system_logs = []
    show = SHOWS.get(show_id)
    if show is None or not isinstance(seat_number, int):
        return False
    if seat_number < 1 or seat_number > show["seats"]:
        return False
    if seat_number in show["booked"]:
        system_logs.append(f"Seat {seat_number} already taken for {show_id}")
        return False
    show["booked"].append(seat_number)
    system_logs.append(f"Reserved seat {seat_number} for {show_id}")
    return True


def release_seat(show_id, seat_number):
    """Release a booked seat, returning whether a seat was released."""
    show = SHOWS.get(show_id)
    if show is None:
        return False
    try:
        show["booked"].remove(seat_number)
    except ValueError:
        return False
    return True


def ticket_code(show_id, seat_number):
    """Return a short deterministic code for a show and seat."""
    ticket_data = f"{show_id}{seat_number}".encode("utf-8")
    return hashlib.sha256(ticket_data).hexdigest()[:8]


def dump_reservations(file_path="seats.json"):
    """Save the current seating plan as JSON."""
    with open(file_path, "w", encoding="utf-8") as reservation_file:
        json.dump(SHOWS, reservation_file, indent=2)


def load_reservations(file_path="seats.json"):
    """Load a seating plan from a JSON file into the current show mapping."""
    with open(file_path, "r", encoding="utf-8") as reservation_file:
        loaded_shows = json.load(reservation_file)
    SHOWS.clear()
    SHOWS.update(loaded_shows)


def print_seating_summary():
    """Print the number and list of booked seats for every show."""
    for show in SHOWS.values():
        free_seats = show["seats"] - len(show["booked"])
        print(
            f"{show['title']}: {free_seats} seats free, "
            f"booked = {show['booked']}"
        )


def main():
    """Run a short reservation demonstration and save its seating plan."""
    reserve_seat("SHOW-1", 5)
    reserve_seat("SHOW-1", 5)
    reserve_seat("SHOW-1", 25)
    reserve_seat("SHOW-2", -1)
    print("Ticket code:", ticket_code("SHOW-1", 5))
    seat_input = input("Seat number to book for SHOW-2 (Enter for 4): ") or "4"
    try:
        seat_number = int(seat_input)
    except ValueError:
        print("Seat number must be an integer.")
    else:
        reserve_seat("SHOW-2", seat_number)
    dump_reservations()
    load_reservations()
    print_seating_summary()


if __name__ == "__main__":
    main()
