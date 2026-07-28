# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in

def read_matrix(rows, cols):
    """Read a matrix row by row."""
    matrix = []
    for r in range(rows):
        print(f"Enter row {r + 1}: ", end="")
        parts = input().split()
        row = []
        for c in range(cols):
            row.append(int(parts[c]))
        matrix.append(row)
    return matrix


def print_matrix(matrix, title=""):
    """Print a matrix using nested loops."""
    if title:
        print(title)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]:4}", end="")
        print()


def transpose(matrix):
    """Transpose by swapping row/column indexes."""
    rows = len(matrix)
    cols = len(matrix[0])

    # Create empty result matrix (cols x rows)
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(0)
        result.append(new_row)

    # Fill result using swapped indexes
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(mat_a, mat_b):
    """Add two matrices element by element."""
    rows = len(mat_a)
    cols = len(mat_a[0])
    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        result.append(row)

    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat_a[i][j] + mat_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Multiply A (M x N) by B (N x P)."""
    m = len(matrix_a)
    n = len(matrix_a[0])
    p = len(matrix_b[0])

    # Create empty result matrix (M x P)
    result = []
    for i in range(m):
        row = []
        for j in range(p):
            row.append(0)
        result.append(row)

    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


def part_a():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)
    transposed = transpose(matrix)

    print()
    print_matrix(matrix, "Original Matrix:")
    print()
    print_matrix(transposed, "Transposed Matrix:")


def part_b():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Matrix A:")
    matrix_a = read_matrix(rows, cols)

    print("Matrix B:")
    matrix_b = read_matrix(rows, cols)

    result = add_matrices(matrix_a, matrix_b)

    print()
    print_matrix(result, "Sum:")


def part_c():
    m = int(input("Enter number of rows for matrix A: "))
    n = int(input("Enter number of columns for matrix A: "))

    print("Matrix A:")
    matrix_a = read_matrix(m, n)

    p = int(input("Enter number of columns for matrix B: "))

    print("Matrix B:")
    matrix_b = read_matrix(n, p)

    result = multiply_matrices(matrix_a, matrix_b)

    print()
    print_matrix(result, "Product A x B:")


def main():
    print("1. Transpose")
    print("2. Add")
    print("3. Multiply")
    choice = input("Choose (1/2/3): ")

    if choice == "1":
        part_a()
    elif choice == "2":
        part_b()
    elif choice == "3":
        part_c()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()

# =============================================================================
