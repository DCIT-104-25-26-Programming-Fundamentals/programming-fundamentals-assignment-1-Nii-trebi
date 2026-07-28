# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)  # round division results to 2 decimal places

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def exponent(a, b):
    return a ** b

def get_number(prompt):
    try:
        return float(input(prompt).strip())
    except ValueError:
        print("Error: please enter a valid number.")
        return None

def print_menu():
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")

def format_num(x):
    # Show integer values without ".0", otherwise show reasonable float
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)

def main():
    try:
        while True:
            print()
            print_menu()
            choice = input("Select an operation (1-7): ").strip()
            if choice == "7":
                print("Goodbye!")
                break

            if choice not in {"1","2","3","4","5","6"}:
                print("Error: Invalid choice. Please enter a number 1-7.")
                continue

            a = get_number("Enter first number : ")
            if a is None:
                continue
            b = get_number("Enter second number: ")
            if b is None:
                continue

            if choice == "1":
                res = add(a, b)
                print(f"Result: {format_num(a)} + {format_num(b)} = {format_num(res)}")
            elif choice == "2":
                res = subtract(a, b)
                print(f"Result: {format_num(a)} - {format_num(b)} = {format_num(res)}")
            elif choice == "3":
                res = multiply(a, b)
                print(f"Result: {format_num(a)} * {format_num(b)} = {format_num(res)}")
            elif choice == "4":
                res = divide(a, b)
                if res is None:
                    print("Error: Cannot divide by zero.")
                else:
                    # Always show division rounded to 2 decimal places
                    print(f"Result: {format_num(a)} / {format_num(b)} = {res:.2f}")
            elif choice == "5":
                res = modulus(a, b)
                if res is None:
                    print("Error: Cannot perform modulus by zero.")
                else:
                    print(f"Result: {format_num(a)} % {format_num(b)} = {format_num(res)}")
            elif choice == "6":
                res = exponent(a, b)
                print(f"Result: {format_num(a)} ** {format_num(b)} = {format_num(res)}")
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")

if __name__ == "__main__":
    main()
# =============================================================================

