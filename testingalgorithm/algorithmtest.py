import timeit as t
import matplotlib.pyplot as plt
import random as r
import tracemalloc
import numpy as np
from listoftestpuzzles import listOfPuzzles


def solve_puzzle(puzzle):
    start_time = t.default_timer()  # Gets the default time at the start of the program
    row, column = find_next_empty(puzzle)
    if row is None:
        return True
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, column):
            puzzle[row][column] = guess
            if solve_puzzle(puzzle):
                end_time = t.default_timer()
                return True, end_time - start_time  # Check the time taken
        puzzle[row][column] = 0

    # return False


def find_next_empty(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                return row, column
    return None, None


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


if __name__ == "__main__":
    lengthOfEmptyCells = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
    timeTaken = list()
    memoryConsumed = list()  # Storage for memory taken per Puzzle
    for i in range(len(listOfPuzzles)):  # Loop through the list of puzzles
        tracemalloc.start()  # Initializes memory tracing
        val = solve_puzzle(listOfPuzzles[i])
        memory = tracemalloc.get_traced_memory()  # Returns the memory allocations traced
        tracemalloc.stop()
        print(
            f" Puzzle {i + 1} Time complexity: {(val[1]) * 1000} milliseconds\n"
            f" Puzzle {i + 1} Space Complexity:{memory[1] / 1000000} megabytes\n")
        print("---------------------------------------------------------------------")

        timeTaken.append((val[1]) * 1000)
        memoryConsumed.append(memory[1] / 1000000)

    plt.ylim(0.0, 1.00)
    plt.yticks(np.arange(0.0, 1.0, 0.1))
    plt.xlabel('Number of Empty Spaces in the Sudoku Puzzle')
    plt.ylabel("Time/Space  (milliseconds/megabytes)")

    plt.plot(lengthOfEmptyCells, memoryConsumed, label='Space Complexity')

    plt.plot(lengthOfEmptyCells, timeTaken, label='Time Complexity')

    plt.grid()
    plt.legend()
    plt.title('Time and Space Complexity for Backtracking Algorithm')
    plt.show()
