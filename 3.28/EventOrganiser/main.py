class Event:
    def __init__(self, name: str, location: str, attendees: list) -> None:
        self.name = name
        self.location = location
        self.attendees = attendees

    def __str__(self) -> str:
        return (
            f"Name: {self.name}\nLocation: {self.location}\nAttendees: {self.attendees}"
        )


from datetime import datetime


def validate_datetime(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y %H:%M")
        return True
    except ValueError:
        print("The date entered is not formatted correctly")
        return False


def date_time_input():
    date = input(
        "Enter the date and time of the event in the format DD-MM-YYYY HH:MM\n"
    )
    while not validate_datetime(date):
        date = input(
            "Enter the date and time of the event in the format DD-MM-YYYY HH:MM\n"
        )
    return date


def event_detail_input():
    name = input("Enter the event name\n")
    location = input("Enter the event location\n")
    print(f"{name} will take place at {location}")
    return name, location


def add_attendees():
    attendees = []
    name = input("Enter attendee name or q to exit\n")
    while name != "q" and len(attendees) < 50:
        attendees.append(name)
        if len(attendees) != 50:
            name = input("Enter attendee name or q to exit\n")
        else:
            print("Limit of 50 attendees reached")
    return attendees


def remove_attendee(name: str, attendees: list):
    try:
        attendees.remove(name)
    except ValueError:
        print(f"{name} is not present in the list")
    return attendees


def search_attendee(name: str, attendees: list):
    if attendees.count(name) == 1:
        print(f"{name} is attending")
    else:
        print(f"{name} is not attending")


def classify_event():
    return input("Add a an event tag\n")


def find_event(date: str, categories: dict):
    for tag, events in categories.items():
        if date in events:
            return tag
    return None


def display_events(categories: dict):
    for tag, events in categories.items():
        print(tag.center(20, "-"))
        for date, event in sorted(
            events.items(),
            key=lambda item: datetime.strptime(item[0], "%d-%m-%Y %H:%M"),
        ):
            print(f"Date {date}\n{event}\n")


def events_per_tags(categories: dict):
    return {tag: len(events) for tag, events in categories.items()}


def save_events(categories: dict):
    with open("./events.txt", "w") as file:
        for tag, events in categories.items():
            for date, event in events.items():
                file.write(
                    f"{tag}\t{date}\t{event.name}\t{event.location}\t{','.join(event.attendees)}\n"
                )


def load_events():
    categories = {}
    try:
        with open("./events.txt", "r") as file:
            for line in file:
                tag, date, name, location, attendees = line.strip().split(f"\t")
                categories.setdefault(tag, {})[date] = Event(
                    name, location, attendees.split(",")
                )
    except FileNotFoundError:
        print("No file found")
        return {}
    return categories


def menu():
    return int(
        input(f"1. Add event\n2. Edit event\n3. Save events\n4. Anayltics\n5. Exit\n")
    )


if __name__ == "__main__":
    print("Welcome to the Event Organizer App!")
    categories = load_events()
    display_events(categories)
    menu_action = menu()
    while menu_action != 5:
        match menu_action:
            case 1:
                date = date_time_input()
                tag = find_event(date, categories)
                if tag != None:
                    print(f"{categories[tag][date].name} is already at {date}")
                    date = date_time_input()
                name, location = event_detail_input()
                attendees = add_attendees()
                event = Event(name, location, attendees)
                tag = classify_event()
                categories.setdefault(tag, {})[date] = event
            case 2:
                date = date_time_input()
                tag = find_event(date, categories)
                if tag == None:
                    print("No event found")
                    continue
                event = categories[tag][date]
                print(f"Date {date}\n{event}")
                new_date = date_time_input()
                new_name, new_location = event_detail_input()
                categories[tag].pop(date, {})
                categories.setdefault(tag, {})[
                    new_date if new_date.strip() else date
                ] = Event(
                    new_name if new_name.strip() else event.name,
                    new_location if new_location.strip() else event.location,
                    event.attendees,
                )

            case 3:
                save_events(categories)
            case 4:
                print(f"{events_per_tags(categories)}\n")
            case 5:
                exit()
        display_events(categories)
        menu_action = menu()
