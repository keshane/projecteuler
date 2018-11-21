import sys
from typing import List
from typing import Set


def print_sudoku(sudoku: List[List]):
    rows = []
    for i in range(len(sudoku)):
        row = sudoku[i].copy()
        row.insert(3, "|")
        row.insert(7, "|")
        rows.append("".join(row))
        if i % 3 == 2 and i // 3 <= 1:
            rows.append("------------")
    grid = "\n".join(rows)
    print(grid)


def find_neighbors_indices(row: int, col: int):
    neighbors = []
    for i in range(9):
        if i != col:
            neighbors.append((row, i))
        if i != row:
            neighbors.append((i, col))
    square_row_low_limit = (row // 3) * 3
    square_col_low_limit = (col // 3) * 3
    for i in range(square_row_low_limit, square_row_low_limit + 3):
        for j in range(square_col_low_limit, square_col_low_limit + 3):
            if not (i, j) in neighbors and (i, j) != (row, col):
                neighbors.append((i, j))

    return neighbors


def eliminate(sudoku: List[List], possibilities: List[List[Set[str]]]):
    for i in range(9):
        for j in range(9):
            element = sudoku[i][j]
            if sudoku[i][j] != "0":
                for neighbor_row, neighbor_column in find_neighbors_indices(i, j):

                    if len(possibilities[neighbor_row][neighbor_column]) > 1:
                        possibilities[neighbor_row][neighbor_column].discard(element)
                    if len(possibilities[neighbor_row][neighbor_column]) == 1 and sudoku[neighbor_row][neighbor_column] == "0":
                        sudoku[neighbor_row][neighbor_column] = min(possibilities[neighbor_row][neighbor_column])


def main():
    file_path = sys.argv[1]
    with open(file_path, "r") as sudoku_file:
        for line in sudoku_file:
            sudoku = [[] for i in range(9)]
            sudoku_id = line.rstrip()
            for i in range(9):
                sudoku_row = sudoku_file.readline()
                sudoku[i] = [c for c in sudoku_row.rstrip()]
            print(sudoku_id)
            print_sudoku(sudoku)
            possibilities = [[{sudoku[row][col] if sudoku[row][col] != "0" else str(i) for i in range(1, 10)} for col in range(9)] for row in range(9)]
            i = 0
            is_done = False
            while not is_done:
                if i >= 10000:
                    print("too many iterations")
                    break
                eliminate(sudoku, possibilities)
                i += 1
                is_done = True
                for row in sudoku:
                    if "0" in row:
                        is_done = False

            print()
            print_sudoku(sudoku)


if __name__ == "__main__":
    main()


