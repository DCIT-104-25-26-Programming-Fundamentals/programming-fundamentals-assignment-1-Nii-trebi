# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in


def calculate_sum(n):
    total = 0
    for x in n:
        total += x
    return total


def calculate_average(n):
    """Return the arithmetic mean of the values in the list."""
    total = calculate_sum(n)
    return total / len(n)


def calculate_maximum(n):
    """Return the largest value in the list using a loop."""
    maximum = n[0]
    for x in n:
        if x > maximum:
            maximum = x
    return maximum


def calculate_minimum(n):
    """Return the smallest value in the list using a loop."""
    minimum = n[0]
    for x in n:
        if x < minimum:
            minimum = x
    return minimum


def main():
    try:
        n = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a valid positive integer.")
        return

    if n <= 0:
        print("Error: Number of values must be a positive integer.")
        return

    numbers = []
    for i in range(1, n + 1):
        number = float(input(f"Enter number {i}: "))
        numbers.append(number)

    print()
    print("Results:")
    print(f"Sum:     {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Maximum: {calculate_maximum(numbers)}")
    print(f"Minimum: {calculate_minimum(numbers)}")


if __name__ == "__main__":
    main()
# =============================================================================
