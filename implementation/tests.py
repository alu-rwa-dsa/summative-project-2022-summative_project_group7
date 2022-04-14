from sudokusolver import solve_puzzle
import unittest
from puzzle import puzzle, solution
from gui import validateNumber, compareSolution, getValues
from tkinter import *


class TestSudoku(unittest.TestCase):

    def test_if_solvable(self):
        solvable_sudoku = puzzle
        solvable = solve_puzzle(solvable_sudoku)
        self.assertTrue(solvable, True)

    def test_if_not_solvable(self):
        unsolvable_sudoku = [[5, 1, 6, 8, 4, 9, 7, 3, 2],
                             [3, 0, 7, 6, 0, 5, 0, 0, 0],
                             [8, 0, 9, 7, 0, 0, 0, 6, 5],
                             [1, 3, 5, 0, 6, 0, 9, 0, 7],
                             [4, 7, 2, 5, 9, 1, 0, 0, 6],
                             [9, 6, 8, 3, 7, 0, 0, 5, 0],
                             [2, 5, 3, 1, 8, 6, 0, 7, 4],
                             [6, 8, 4, 2, 0, 7, 5, 0, 0],
                             [7, 9, 1, 0, 5, 0, 6, 0, 8]]
        solvable = solve_puzzle(unsolvable_sudoku)
        self.assertFalse(solvable, False)

    def test_accept_correctInput(self):
        self.assertEqual(validateNumber("1"), 1)

    #
    def test_accept_letter(self):
        self.assertEqual(validateNumber("a"), False)

    def test_with_twoDigit_number(self):
        self.assertEqual(validateNumber("22"), False)

    def test_when_number_is_zero(self):
        self.assertEqual(validateNumber("0"), False)

    def test_number_of_rows(self):
        self.assertEqual(len(getValues()), 9)

    def test_number_of_columns(self):
        self.assertEqual(len(getValues()[1]), 9)


if __name__ == "__main__":
    # Set up Tk(), instantiate the application and close it right away.
    root = Tk()
    

    # Start the actual tests
    unittest.main(verbosity=2)
    root.destroy()
