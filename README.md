# EventFlow

# EventFlow

## 📌 Overview
EventFlow is an advanced event management system that efficiently handles **scheduling, prioritization, dependency management, and participant tracking** using optimized **data structures** such as **heaps, graphs, hash tables, and binary trees**.

## 🔥 Features
- **Event Prioritization**: Uses a **MinHeap** for managing event priority.
- **Dependency Management**: Implements a **Directed Graph** to track event dependencies.
- **Cycle Detection**: Prevents circular dependencies in event execution.
- **Participant Tracking**: Uses a **Hash Table** for storing event participants.
- **Event Categorization**: Implements a **Binary Tree** for organizing events by date, participants, and instructor.
- **Event Execution & Notification**: Ensures structured execution of events and notifies participants.
- **Rating System**: Allows rating of events and instructors.
- **Persistence**: Stores event data in a JSON file for future access.

## 📂 Technologies Used
- **Programming Language**: Python 🐍
- **Data Structures**: Heap, Graph, Hash Table, Binary Tree

## 🚀 Getting Started
### 1️⃣ Installation
Make sure you have **Python 3.x** installed.

### 2️⃣ Running the Application
```sh
python main.py
```

## 👨‍💻 Code Structure
- `event.py` – Defines the **Event** class.
- `heap.py` – Implements a **MinHeap** for event prioritization.
- `graph.py` – Implements a **Directed Graph** for dependency tracking.
- `hash_table.py` – Implements a **Hash Table** for participant management.
- `tree.py` – Implements a **Binary Tree** for event categorization.
- `main.py` – The **core script** for interacting with the system.

## 🎯 Usage
- Add, execute, and manage events.
- Track dependencies between events.
- Categorize events based on different criteria.
- Rate events and instructors.
- Persist event data for future use.

## 💡 Contribution
Feel free to fork the repository, submit issues, and contribute to improving **EventFlow**! 🚀

## 📜 License
This project is licensed under the **MIT License**.

