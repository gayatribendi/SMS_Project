import os
import json

FILE_NAME = "students.json"
MAX_STUDENTS = 200

# ─── File I/O ──────────────────────────────────────────────────────────────────
def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_students(students):
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)

# ─── Utility ───────────────────────────────────────────────────────────────────
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def divider():
    print("─" * 58)

def print_header():
    clear_screen()
    divider()
    print("         STUDENT MANAGEMENT SYSTEM")
    divider()

def print_student(s):
    divider()
    print(f"  ID     : {s['id']}")
    print(f"  Name   : {s['name']}")
    print(f"  Branch : {s['branch']}")
    print(f"  Year   : {s['year']}")
    print(f"  CGPA   : {s['cgpa']}")
    print(f"  Email  : {s['email']}")

def pause():
    input("\nPress Enter to continue...")

def next_id(students):
    return 1 if not students else students[-1]["id"] + 1

# ─── CRUD Operations ───────────────────────────────────────────────────────────

# CREATE
def add_student(students):
    print_header()
    print("  ADD NEW STUDENT")
    divider()

    if len(students) >= MAX_STUDENTS:
        print(f"  [ERROR] Maximum limit of {MAX_STUDENTS} students reached.")
        pause()
        return

    s = {}
    s["id"]     = next_id(students)
    s["name"]   = input("  Name       : ").strip()
    s["branch"] = input("  Branch     : ").strip()
    s["year"]   = input("  Year (1-4) : ").strip()
    s["cgpa"]   = input("  CGPA       : ").strip()
    s["email"]  = input("  Email      : ").strip()

    students.append(s)
    save_students(students)
    print(f"\n  [SUCCESS] Student added with ID: {s['id']}")
    pause()

# READ — all
def display_all(students):
    print_header()
    print(f"  ALL STUDENTS ({len(students)} records)")

    if not students:
        print("\n  No records found.")
        pause()
        return

    for s in students:
        print_student(s)
    divider()
    pause()

# SEARCH by ID
def search_by_id(students):
    print_header()
    print("  SEARCH BY ID")
    divider()

    sid = input("  Enter Student ID: ").strip()
    for s in students:
        if str(s["id"]) == sid:
            print("\n  [FOUND]")
            print_student(s)
            divider()
            pause()
            return
    print(f"\n  [NOT FOUND] No student with ID {sid}.")
    pause()

# SEARCH by Name
def search_by_name(students):
    print_header()
    print("  SEARCH BY NAME")
    divider()

    query = input("  Enter Name (or partial name): ").strip().lower()
    results = [s for s in students if query in s["name"].lower()]

    if not results:
        print(f"\n  [NOT FOUND] No student matching '{query}'.")
    else:
        for s in results:
            print_student(s)
        print(f"\n  {len(results)} record(s) found.")
        divider()
    pause()

# UPDATE
def update_student(students):
    print_header()
    print("  UPDATE STUDENT RECORD")
    divider()

    sid = input("  Enter Student ID to update: ").strip()
    for s in students:
        if str(s["id"]) == sid:
            print("\n  Current Record:")
            print_student(s)
            print("\n  Enter new details (press Enter to keep current):\n")

            val = input(f"  Name [{s['name']}]: ").strip()
            if val: s["name"] = val

            val = input(f"  Branch [{s['branch']}]: ").strip()
            if val: s["branch"] = val

            val = input(f"  Year [{s['year']}]: ").strip()
            if val: s["year"] = val

            val = input(f"  CGPA [{s['cgpa']}]: ").strip()
            if val: s["cgpa"] = val

            val = input(f"  Email [{s['email']}]: ").strip()
            if val: s["email"] = val

            save_students(students)
            print(f"\n  [SUCCESS] Record updated for ID: {sid}")
            pause()
            return

    print(f"\n  [NOT FOUND] No student with ID {sid}.")
    pause()

# DELETE
def delete_student(students):
    print_header()
    print("  DELETE STUDENT RECORD")
    divider()

    sid = input("  Enter Student ID to delete: ").strip()
    for i, s in enumerate(students):
        if str(s["id"]) == sid:
            print("\n  Record to delete:")
            print_student(s)
            confirm = input("\n  Confirm delete? (y/n): ").strip().lower()
            if confirm == "y":
                students.pop(i)
                save_students(students)
                print(f"\n  [SUCCESS] Student ID {sid} deleted.")
            else:
                print("\n  Delete cancelled.")
            pause()
            return

    print(f"\n  [NOT FOUND] No student with ID {sid}.")
    pause()

# ─── Main Menu ─────────────────────────────────────────────────────────────────
def main():
    students = load_students()

    while True:
        print_header()
        print(f"  Total Records: {len(students)} / {MAX_STUDENTS}")
        divider()
        print("  1. Add New Student")
        print("  2. Display All Students")
        print("  3. Search by ID")
        print("  4. Search by Name")
        print("  5. Update Student Record")
        print("  6. Delete Student Record")
        print("  0. Exit")
        divider()

        choice = input("  Enter choice: ").strip()

        if   choice == "1": add_student(students)
        elif choice == "2": display_all(students)
        elif choice == "3": search_by_id(students)
        elif choice == "4": search_by_name(students)
        elif choice == "5": update_student(students)
        elif choice == "6": delete_student(students)
        elif choice == "0":
            print("\n  Goodbye!\n")
            break
        else:
            print("\n  Invalid choice.")
            pause()

if __name__ == "__main__":
    main()
