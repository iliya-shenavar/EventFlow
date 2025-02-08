from event import Event
from heap import MinHeap
from graph import DirectedGraph
from hash_table import HashTable
from tree import EventTree
from datetime import datetime
import json


def validate_date(date_str):
    """Validate date format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def save_data(event_list, filename="events.json"):
    """Save event data to a JSON file."""
    data = [event.to_dict() for event in event_list]
    with open(filename, "w") as file:
        json.dump(data, file)


def load_data(filename="events.json"):
    """Load event data from a JSON file."""
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return [Event.from_dict(event) for event in data]
    except FileNotFoundError:
        return []


def log_action(action, filename="event_log.txt"):
    """Log an action to a log file."""
    with open(filename, "a") as log_file:
        log_file.write(f"{datetime.now()}: {action}\n")


def main():
    event_heap = MinHeap()  # Priority queue for event management
    event_graph = DirectedGraph()  # Directed graph for dependencies
    participants = HashTable()  # Hash table for participant management
    instructors = HashTable()  # Hash table for instructor ratings
    event_list = load_data()  # Load events from JSON file
    event_tree = EventTree()  # Tree for event categorization

    # Rebuild data structures from loaded events
    for event in event_list:
        event_heap.insert(event)
        event_graph.add_event(event.name)
        event_tree.insert_by_date(event)
        event_tree.insert_by_participants(event)
        event_tree.insert_by_instructor(event)

    while True:
        print("\n--- Event Management System ---")
        print("1. Add Event")
        print("2. View Next Event")
        print("3. Execute Event")
        print("4. Add Dependency")
        print("5. Check Cycles")
        print("6. Add Participant to Event")
        print("7. Search for Event by Name")
        print("8. Remove Event")
        print("9. Notify Participants")
        print("10. Categorize Events")
        print("11. Check Overlapping Events")
        print("12. View Events by Status")
        print("13. Rate Event")
        print("14. Rate Instructor")
        print("15. View Instructor Ratings")
        print("16. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter event name: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            while not validate_date(date):
                print("Invalid date format. Please enter again in YYYY-MM-DD format.")
                date = input("Enter event date (YYYY-MM-DD): ")

            try:
                priority = int(input("Enter event priority (integer): "))
                instructor = input("Enter the instructor's name: ")
                event = Event(name, date, priority, instructor=instructor)
                event_heap.insert(event)
                event_graph.add_event(name)
                event_list.append(event)
                event_tree.insert_by_date(event)
                event_tree.insert_by_participants(event)
                event_tree.insert_by_instructor(event)
                print(f"Event '{name}' added successfully.")
                log_action(f"Added event: {name}")
            except ValueError:
                print("Priority must be an integer.")

        elif choice == "2":
            next_event = event_heap.peek()
            if next_event:
                print("\nNext Event in Priority Queue:")
                print(next_event)
            else:
                print("No events available.")

        elif choice == "3":
            next_event = event_heap.peek()
            if next_event:
                dependencies = event_graph.graph.get(next_event.name, [])
                unresolved = [dep for dep in dependencies if dep not in [e.name for e in event_list if e.state == "Completed"]]
                if unresolved:
                    print(f"Cannot execute '{next_event.name}'. Pending dependencies: {', '.join(unresolved)}")
                else:
                    next_event = event_heap.extract_min()
                    next_event.update_state("Ongoing")
                    print(f"Notification: Event '{next_event.name}' is now ongoing.")
                    participants_list = participants.get(next_event.name) or []
                    print(f"Executing event: {next_event.name}")
                    print(f"Number of participants: {len(participants_list)}")
                    next_event.update_state("Completed")
                    print(f"Event '{next_event.name}' completed successfully.")
                    log_action(f"Executed event: {next_event.name}")

        elif choice == "4":
            event_a = input("Enter the name of the first event (must happen first): ")
            event_b = input("Enter the name of the second event (depends on the first): ")
            if event_a in [e.name for e in event_list] and event_b in [e.name for e in event_list]:
                event_graph.add_dependency(event_b, event_a)
                print(f"Dependency added: {event_b} -> {event_a}")
                log_action(f"Added dependency: {event_b} -> {event_a}")
            else:
                print("One or both events not found.")

        elif choice == "5":
            if event_graph.has_cycle():
                print("Cycle detected in the dependencies!")
            else:
                print("No cycles detected in the dependencies.")

        elif choice == "6":
            event_name = input("Enter the event name: ")
            participant_name = input("Enter the participant's name: ")
            found_event = next((event for event in event_list if event.name == event_name), None)
            if found_event:
                participants_list = participants.get(event_name) or []
                if participant_name in participants_list:
                    print(f"Participant '{participant_name}' is already registered for event '{event_name}'.")
                else:
                    participants_list.append(participant_name)
                    participants.insert(event_name, participants_list)
                    print(f"Participant '{participant_name}' added to event '{event_name}'.")
                    log_action(f"Added participant '{participant_name}' to event '{event_name}'")
            else:
                print(f"Event '{event_name}' not found.")

        elif choice == "7":
            event_name = input("Enter the event name to search: ")
            found_event = next((event for event in event_list if event.name == event_name), None)
            if found_event:
                participants_list = participants.get(event_name) or []
                print("\nEvent Details:")
                print(found_event)
                print(f"Participants: {', '.join(participants_list) if participants_list else 'None'}")
            else:
                print(f"Event '{event_name}' not found.")

        elif choice == "8":
            event_name = input("Enter the event name to remove: ")
            found_event = next((event for event in event_list if event.name == event_name), None)
            if found_event:
                event_list.remove(found_event)
                event_heap.heap = [event for event in event_heap.heap if event.name != event_name]
                participants.insert(event_name, [])
                print(f"Event '{event_name}' removed successfully.")
                log_action(f"Removed event: {event_name}")
            else:
                print(f"Event '{event_name}' not found.")

        elif choice == "9":
            event_name = input("Enter the event name to notify participants: ")
            participants_list = participants.get(event_name)
            if participants_list:
                print(f"Notifying participants of '{event_name}'...")
                message = input("Enter the message to send: ")
                for participant in participants_list:
                    print(f"Notification sent to {participant}: {message}")
                log_action(f"Notified participants of event '{event_name}'")
            else:
                print(f"No participants found for event '{event_name}'. Check the event name and try again.")

        elif choice == "10":
            print("\nCategorized Events by Date:")
            events_by_date = event_tree.inorder_by_date()
            for event in events_by_date:
                print(f"{event.name} - {event.date}")

            print("\nCategorized Events by Participants:")
            events_by_participants = event_tree.inorder_by_participants()
            for event in events_by_participants:
                print(f"{event.name} - {len(event.participants)} participants")

            print("\nCategorized Events by Instructor:")
            events_by_instructor = event_tree.inorder_by_instructor()
            for event in events_by_instructor:
                print(f"{event.name} - Instructor: {event.instructor}")

        elif choice == "11":
            overlaps = []
            for i, event1 in enumerate(event_list):
                for event2 in event_list[i + 1:]:
                    if event1.date == event2.date:
                        overlaps.append((event1, event2))
            if overlaps:
                print("Overlapping Events Found:")
                for event1, event2 in overlaps:
                    print(f"{event1.name} and {event2.name} overlap.")
                log_action("Detected overlapping events.")
            else:
                print("No overlapping events found.")

        elif choice == "12":
            print("Events by Status:")
            for status in ["Not Started", "Ongoing", "Completed"]:
                print(f"\nStatus: {status}")
                for event in event_list:
                    if event.state == status:
                        print(f"- {event.name} ({event.date})")

        elif choice == "13":
            print("Events eligible for rating (Completed):")
            for event in event_list:
                if event.state == "Completed":
                    print(f"- {event.name}")
            event_name = input("Enter the event name to rate: ")
            found_event = next((event for event in event_list if event.name == event_name), None)
            if found_event and found_event.state == "Completed":
                try:
                    rating = int(input("Enter rating (1-5): "))
                    if 1 <= rating <= 5:
                        found_event.rate_event(rating)
                        log_action(f"Rated event '{event_name}' with {rating}/5")
                        print(f"Event '{event_name}' rated {rating}/5.")
                    else:
                        print("Rating must be between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 5.")
            else:
                print(f"Event '{event_name}' not found or is not completed.")

        elif choice == "14":
            instructor_name = input("Enter the instructor's name to rate: ")
            try:
                rating = int(input("Enter rating (1-5): "))
                if 1 <= rating <= 5:
                    current_rating = instructors.get(instructor_name) or []
                    current_rating.append(rating)
                    instructors.insert(instructor_name, current_rating)
                    print(f"Rated instructor '{instructor_name}' with {rating}/5.")
                    log_action(f"Rated instructor '{instructor_name}' with {rating}/5.")
                else:
                    print("Rating must be between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

        elif choice == "15":
            all_instructors = [(name, sum(ratings) / len(ratings)) for name, ratings in instructors.table if ratings]
            sorted_instructors = sorted(all_instructors, key=lambda x: x[1], reverse=True)
            print("\nInstructors ranked by ratings:")
            for name, avg_rating in sorted_instructors:
                print(f"{name}: {avg_rating:.2f}/5")

        elif choice == "16":
            save_data(event_list)
            print("Data saved. Exiting the system. Goodbye!")
            log_action("System exited and data saved.")
            break


if __name__ == "__main__":
    main()
