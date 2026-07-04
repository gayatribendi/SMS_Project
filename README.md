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
- Python 3.x installed

### Run
```bash
python3 student_management.py
```

---

## Key Concepts Demonstrated

- **Dictionaries & Lists** — store and manage student records
- **File Handling** — json.load / json.dump for persistent storage
- **String Methods** — partial name search and input sanitization
- **Functions** — modular CRUD functions for clean structure
- **Menu-driven Interface** — while loop with if-elif navigation

---

## Author

**Gayatri Bendi**
B.Tech – Electrical and Electronics Engineering
Lendi Institute of Engineering and Technology, Vizianagaram
gayatribendi9@gmail.com
