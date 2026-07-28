# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in


def print_table(number):
    """Print the multiplication table for one number from 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        product = number * i
        if i < 10:
            print(f"{number}  x  {i}  =  {product}")
        else:
            print(f"{number}  x  {i} =  {product}")


def part_a_single_table():
    """Part A: print one multiplication table."""
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    print()
    print_table(number)


def part_b_tables_to_n():
    """Part B: print multiplication tables for 1 through N."""
    try:
        n = int(input("Enter N: "))
    except ValueError:
        print("Error: Please enter a valid positive integer.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    print()
    for number in range(1, n + 1):
        if number > 1:
            print("---------------------------")
        print_table(number)


def main():
    print("Multiplication Table Generator")
    print("1. Single table (Part A)")
    print("2. Tables from 1 to N (Part B)")
    choice = input("Choose an option (1/2): ")

    print()
    if choice == "1":
        part_a_single_table()
    elif choice == "2":
        part_b_tables_to_n()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()

# =============================================================================
