# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in

def display_menu():
    print("===============================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("===============================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")

def get_positive_int(prompt):
    """Prompt until a positive integer is entered, or return None on invalid input."""
    try:
        v = int(input(prompt).strip())
    except ValueError:
        print("Error: please enter a whole number.")
        return None
    if v <= 0:
        print("Error: number must be positive.")
        return None
    return v

def read_score(prompt):
    """Read a numeric score (int or float). Return float or None on invalid input."""
    s = input(prompt).strip()
    try:
        score = float(s)
    except ValueError:
        print("Error: please enter a numeric score.")
        return None
    return score

def format_score(x):
    """Format score for display: no .0 for whole numbers."""
    return str(int(x)) if float(x).is_integer() else f"{x:g}"

def add_student(students):
    """Feature 1: Add a student record."""
    name = input("Student name: ").strip()
    if not name:
        print("Error: name cannot be empty.")
        return

    sid = input("Student ID: ").strip()
    if not sid:
        print("Error: ID cannot be empty.")
        return

    # Check for duplicate ID
    if any(s["id"] == sid for s in students):
        print(f'Error: A student with ID {sid} already exists.')
        return

    n_scores = get_positive_int("How many scores? ")
    if n_scores is None:
        return

    scores = []
    for i in range(1, n_scores + 1):
        while True:
            sc = read_score(f"Enter score {i}: ")
            if sc is None:
                # invalid, ask again
                continue
            scores.append(sc)
            break

    students.append({"name": name, "id": sid, "scores": scores})
    print(f'Student "{name}" added successfully.')

def display_all_students(students):
    """Feature 2: Display a formatted table of all students."""
    if not students:
        print("No student records available.")
        return

    # Prepare table columns
    name_col = "Name"
    id_col = "ID"
    scores_col = "Scores"
    avg_col = "Average"

    # Compute widths
    name_w = max(len(name_col), max(len(s["name"]) for s in students))
    id_w = max(len(id_col), max(len(s["id"]) for s in students))
    scores_strs = []
    for s in students:
        scores_str = ", ".join(format_score(x) for x in s["scores"])
        scores_strs.append(scores_str)
    scores_w = max(len(scores_col), max(len(x) for x in scores_strs))
    avg_w = len(avg_col)

    sep = "-" * (name_w + id_w + scores_w + avg_w + 10)
    print(sep)
    header = f"{name_col.ljust(name_w)}   {id_col.ljust(id_w)}   {scores_col.ljust(scores_w)}   {avg_col.rjust(avg_w)}"
    print(header)
    print(sep)

    for s, scores_str in zip(students, scores_strs):
        scores = s["scores"]
        avg = sum(scores) / len(scores) if scores else 0.0
        avg_str = f"{avg:.2f}"
        line = (
            f"{s['name'].ljust(name_w)}   "
            f"{s['id'].ljust(id_w)}   "
            f"{scores_str.ljust(scores_w)}   "
            f"{avg_str.rjust(avg_w)}"
        )
        print(line)
    print(sep)

def calculate_average_score(students):
    """Feature 3: Calculate average for a specific student by ID."""
    if not students:
        print("No student records available.")
        return

    sid = input("Enter student ID: ").strip()
    if not sid:
        print("Error: ID cannot be empty.")
        return

    student = next((s for s in students if s["id"] == sid), None)
    if student is None:
        print(f"Error: No student found with ID {sid}.")
        return

    scores = student["scores"]
    if not scores:
        print(f"{student['name']} has no scores recorded.")
        return

    avg = sum(scores) / len(scores)
    print(f"{student['name']}'s average score: {avg:.2f}")

def main():
    students = []
    try:
        while True:
            print()
            display_menu()
            choice = input("Enter your choice (1-4): ").strip()
            if choice == "1":
                add_student(students)
            elif choice == "2":
                display_all_students(students)
            elif choice == "3":
                calculate_average_score(students)
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Error: Invalid choice. Please enter 1, 2, 3, or 4.")
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")

if __name__ == "__main__":
    main()
# =============================================================================

