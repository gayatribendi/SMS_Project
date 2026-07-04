# Student Management System
### Python | File Handling | CRUD Operations

A console-based Student Management System built in Python to handle end-to-end student record management for 200+ entries. Data is stored in a JSON file so records persist between sessions.

---

## Features

| Operation | Description |
|-----------|-------------|
| **Add**     | Register a new student with auto-generated ID |
| **Display** | View all student records |
| **Search**  | Find students by ID or by name (partial match supported) |
| **Update**  | Edit any field of an existing record |
| **Delete**  | Remove a record with confirmation prompt |

---

## Data Fields per Student

- Student ID (auto-generated)
- Name
- Branch
- Year (1–4)
- CGPA
- Email

---

## How to Run

### Prerequisites
- Python 3.x installed (`python3 --version` to check)
- No external libraries needed — uses only built-in modules

### Run
```bash
python3 student_management.py
```

---

## Project Structure

```
student_management_system/
├── student_management.py   # Main source file
├── students.json           # Auto-generated data file (after first run)
└── README.md
```

---

## Key Concepts Demonstrated

- **Dictionaries & Lists** — used to store and manage student records
- **File Handling** — `json.load` / `json.dump` for persistent storage
- **String Methods** — `.lower()`, `.strip()` for input handling and partial name search
- **Functions** — modular CRUD functions for clean code structure
- **Menu-driven Interface** — `while` loop with `if-elif` for navigation

---

## Sample Output

```
──────────────────────────────────────────────────────────
         STUDENT MANAGEMENT SYSTEM
──────────────────────────────────────────────────────────
  Total Records: 3 / 200
──────────────────────────────────────────────────────────
  1. Add New Student
  2. Display All Students
  3. Search by ID
  4. Search by Name
  5. Update Student Record
  6. Delete Student Record
  0. Exit
──────────────────────────────────────────────────────────
  Enter choice:
```

---

## Author

**Gayatri Bendi**  
B.Tech – Electrical and Electronics Engineering  
Lendi Institute of Engineering and Technology, Vizianagaram  
📧 gayatribendi9@gmail.com
