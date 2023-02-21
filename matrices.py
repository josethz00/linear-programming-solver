from typing import Any, Optional

SUB = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')
SUPER = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')

def solve_user_input_matrices():
    print(
'''
ATTENTION: The matrices should have the same number of rows and columns.
If you want to perform a multiplication, the number of columns of the first matrix
should be equal to the number of rows of the second matrix.

'''
    )

    operation = input('What operation do you want to perform? ')

    if operation in ('multiplication', 'addition', 'subtraction'):
        print('-----------------Enter the first matrix -----------------\n')
        rows = int(input('How many rows? '))
        columns = int(input('How many columns? '))
        matrix1 = get_matrix(rows, columns)
        print('-----------------Enter the second matrix-----------------\n')
        rows = int(input('How many rows? '))
        columns = int(input('How many columns? '))
        matrix2 = get_matrix(rows, columns)
        print('-----------------The result is-----------------\n')
        print_matrix(solve_matrices(matrix1, matrix2, operation))
        return

    rows = int(input('How many rows? '))
    columns = int(input('How many columns? '))
    matrice = get_matrix(rows, columns)
    print_matrix(solve_matrices(matrice, None, operation))

def get_matrix(rows: int, columns: int) -> list[list[Any]]:
    matrix = []

    for row in range(rows):
        matrix.append([])
        for column in range(columns):
            matrix[row].append(float(
                input(f'Enter the value for the a({row+1}{column+1}) element: ')
            ))
    print_matrix(matrix)
    return matrix

def print_matrix(matrix: list[list[Any]]):
    for row in matrix:
        print(row)

def solve_matrices(
    matrix1: list[list[float]],
    matrix2: Optional[list[list[float]]],
    operation: str
) -> list[list[float]]:
    if matrix2 is None:
        return solve_single_matrix(matrix1, operation)

    match operation:
        case 'multiplication':
            return multiply_matrices(matrix1, matrix2)
        case 'addition':
            return add_matrices(matrix1, matrix2)
        case 'subtraction':
            return subtract_matrices(matrix1, matrix2)
    return []

def solve_single_matrix(matrice: list[list[float]], operation: str) -> list[list[float]]:
    match operation:
        case 'determinant':
            return determinant(matrice)
        case 'inverse':
            return inverse(matrice)
        case 'transpose':
            return transpose(matrice)
    return []

def multiply_matrices(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    columns = len(matrix1[0])
    rows = len(matrix2)
    result_matrix: list[list[float]] = [[0]*columns for _ in range(rows)]

    for i in range(columns):
        for j in range(rows):
            result_matrix[i][j] = sum(
                [matrix1[i][k] * matrix2[k][j] for k in range(columns)]
            )

    return result_matrix

def add_matrices(matrix1: list[list[float]], matrix2: list[list[float]]):
    for row in range(len(matrix1)):
        for column in range(len(matrix1[row])):
            matrix1[row][column] += matrix2[row][column]
    return matrix1

def subtract_matrices(matrix1: list[list[float]], matrix2: list[list[float]]):
    for row in range(len(matrix1)):
        for column in range(len(matrix1[row])):
            matrix1[row][column] -= matrix2[row][column]
    return matrix1

def determinant(matrix: list[list[float]]) -> list[list[float]]:
    return []

def inverse(matrix: list[list[float]]) -> list[list[float]]:
    return []

def transpose(matrix: list[list[float]]) -> list[list[float]]:
    original_rows = len(matrix)
    original_columns = len(matrix[0])

    rows = original_columns
    columns = original_rows

    result_matrix: list[list[float]] = [[0] * columns for _ in range(rows)]

    for row in range(rows):
        for column in range(columns):
            result_matrix[row][column] = matrix[column][row]

    return result_matrix

if __name__ == '__main__':
    solve_user_input_matrices()