# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in

def fib_first_n(n):
    """Return a list with the first n Fibonacci numbers (n > 0)."""
    if n <= 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


def is_fibonacci(x):
    """Return True if x is a Fibonacci number (x >= 0), otherwise False."""
    if x < 0:
        return False
    a, b = 0, 1
    while a < x:
        a, b = b, a + b
    return a == x


def main():
    # Part A
    try:
        n = int(input("How many terms? "))
    except ValueError:
        print("Error: please enter a whole number.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        seq = fib_first_n(n)
        print("Fibonacci sequence:", " ".join(str(num) for num in seq))

    # Part B
    try:
        x = int(input("Enter a number to check: "))
    except ValueError:
        print("Error: please enter a whole number.")
        return

    if is_fibonacci(x):
        print(f"{x} is a Fibonacci number.")
    else:
        print(f"{x} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()
# =============================================================================
