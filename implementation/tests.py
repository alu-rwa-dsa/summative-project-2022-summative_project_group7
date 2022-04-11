from sudokusolver import solve_puzzle
import unittest
from puzzle import puzzle, solution
from gui import compareSolution, getValues

cells = {(2, 1): 5, (2, 2): 3, (2, 3): 4,
         (3, 1): 6, (3, 2): 7, (3, 3): 2,
         (4, 1): 1, (4, 2): 9, (4, 3): 8,
         (2, 4): 6, (2, 5): 7, (2, 6): 8,
         (3, 4): 1, (3, 5): 9, (3, 6): 5,
         (4, 4): 3, (4, 5): 4, (4, 6): 2,
         (2, 7): 9, (2, 8): 1, (2, 9): 2,
         (3, 7): 3, (3, 8): 4, (3, 9): 8,
         (4, 7): 5, (4, 8): 6, (4, 9): 7,
         (5, 1): 8, (5, 2): 5, (5, 3): 9,
         (6, 1): 4, (6, 2): 2, (6, 3): 6,
         (7, 1): 7, (7, 2): 1, (7, 3): 3,
         (5, 4): 7, (5, 5): 6, (5, 6): 1,
         (6, 4): 8, (6, 5): 5, (6, 6): 3,
         (7, 4): 9, (7, 5): 2, (7, 6): 4,
         (5, 7): 4, (5, 8): 2, (5, 9): 3,
         (6, 7): 7, (6, 8): 9, (6, 9): 1,
         (7, 7): 8, (7, 8): 5, (7, 9): 6,
         (8, 1): 9, (8, 2): 6, (8, 3): 1,
         (9, 1): 2, (9, 2): 8, (9, 3): 7,
         (10, 1): 3, (10, 2): 4, (10, 3): 5,
         (8, 4): 5, (8, 5): 3, (8, 6): 7,
         (9, 4): 4, (9, 5): 1, (9, 6): 9,
         (10, 4): 2, (10, 5): 8, (10, 6): 6,
         (8, 7): 2, (8, 8): 8, (8, 9): 4,
         (9, 7): 6, (9, 8): 3, (9, 9): 5,
         (10, 7): 1, (10, 8): 7, (10, 9): 9}


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

    # def test_verify_player_solution(self):
    #     playerSolution = [
    #         [5, 3, 4, 6, 7, 8, 9, 1, 2],
    #         [6, 7, 2, 1, 9, 5, 3, 4, 8],
    #         [1, 9, 8, 3, 4, 2, 5, 6, 7],
    #         [8, 5, 9, 7, 6, 1, 4, 2, 3],
    #         [4, 2, 6, 8, 5, 3, 7, 9, 1],
    #         [7, 1, 3, 9, 2, 4, 8, 5, 6],
    #         [9, 6, 1, 5, 3, 7, 2, 8, 4],
    #         [2, 8, 7, 4, 1, 9, 6, 3, 5],
    #         [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    #
    #     sudokuSolution = compareSolution()
    #     self.assertEqual(sudokuSolution, playerSolution)


if __name__ == '__main__':
    unittest.main()
