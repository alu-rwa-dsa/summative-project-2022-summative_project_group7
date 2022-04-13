import timeit


count = 0


# Function to solve a given sudoku puzzle.
def solve_puzzle(puzzle):

    row, column = find_next_empty(puzzle)
    if row is None:
        return True
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, column):
            puzzle[row][column] = guess
            if solve_puzzle(puzzle):
                return True
        puzzle[row][column] = 0
    return False


# Function to find a blank cell in the grid.
def find_next_empty(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                return row, column
    return None, None


# Function to find the validity of a given number in a particular cell in the grid.
def is_valid(puzzle, guess, row, column):
    # Check row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Check column
    col_vals = [puzzle[i][column] for i in range(9)]

    if guess in col_vals:
        return False
    # Check Boxes
    row_start = (row // 3) * 3
    col_start = (column // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True


# Function to print out sudoku solution on the terminal
def print_puzzle(puzzle):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-------------------")  # Divides the puzzle into rows of 3 with a line separation
        for j in range(9):
            if j % 3 == 0 and j != 0:  # Self Explanatory
                print("|", end="")
            if j == 8:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j]) + " ", end="")


# Function returns the solved puzzle(if solvable) and populates the values on the Sudoku GUI
def solver(puzzle):
    if solve_puzzle(puzzle):
        return puzzle
    else:
        return "no"
