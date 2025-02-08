# EventFlow

## 📌 Overview
EventFlow is an advanced event management system that leverages **optimized data structures** such as **heap, graph, hash table, and binary tree** to facilitate **scheduling, prioritization, dependency management, and participant tracking**.

## 🔥 Features
- **Add New Event**: Register an event with **name, date, priority, and instructor**.
- **Event Prioritization**: Uses **MinHeap** to manage event execution based on priority.
- **Dependency Management**: Implements a **directed graph** to track event dependencies and prevent incorrect execution.
- **Cycle Detection**: Prevents circular dependencies in event execution using a **graph cycle detection algorithm**.
- **View and Execute Next Event**: Retrieves the next event based on **priority and time** and executes it when conditions are met.
- **Remove Events**: Enables deleting scheduled events from the system.
- **Participant Management**: Uses a **hash table** to store and track event participants.
- **Search Events by Name**: Allows finding a specific event in the system.
- **Event Categorization**: Implements a **binary tree** to organize events based on **date, number of participants, and instructor**.
- **Notify Participants**: Sends notifications to registered participants of each event.
- **Check Event Overlaps**: Identifies events scheduled on the same date.
- **Categorize Events by Status**: Displays lists of **upcoming, ongoing, and completed** events.
- **Rate Events and Instructors**: Enables rating events and instructors on a scale from **1 to 5**.
- **Data Persistence**: Stores event data in a **JSON file** for future use.

## 📂 Technologies Used
- **Programming Language**: Python 🐍
- **Data Structures**: Heap, Graph, Hash Table, Binary Tree

## 🚀 Getting Started
### 1️⃣ Installation
Ensure **Python 3.x** is installed on your system.

### 2️⃣ Run the Application
```sh
python main.py
```

## 👨‍💻 Code Structure
- `event.py` – Defines the **Event** class.
- `heap.py` – Implements **MinHeap** for event prioritization.
- `graph.py` – Implements a **Directed Graph** for dependency tracking.
- `hash_table.py` – Implements a **Hash Table** for participant management.
- `tree.py` – Implements a **Binary Tree** for event categorization.
- `main.py` – **Main script** for system interaction.

## 🎯 Usage
- **Add, view, remove, and execute events.**
- **Track dependencies between events.**
- **Categorize events by date, participants, and instructor.**
- **Detect overlapping events.**
- **Rate events and instructors.**
- **Notify event participants.**
- **Persist event data for future use.**

