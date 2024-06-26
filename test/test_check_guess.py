"""!@file test_check_guess.py
@brief Test function to check the functionality of the check_guess function in the backtracking module.
@details  This function tests the behavior of the check_validity function in the backtracking.py module.
    It creates a test sudoku array and checks the validity of both correct and incorrect guesses placed in empty cells.
    It then asserts the expected results of calling the check_validity function on these inputs.
    This test is successful if the check_validity function returns True for valid guesses and False for invalid guesses.

@author Created by S.M. Daloglu: smd89@cam.ac.uk on 05/12/2023
"""

from src.sudoku.backtracking import check_guess
import numpy as np


def test_check_guess():
    """!@brief Test for check_guess function in backtracking.py
    @details  This function tests the behavior of the check_validity function in the backtracking.py module.
    It creates a test sudoku array and checks the validity of both correct and incorrect guesses placed in empty cells.
    It then asserts the expected results of calling the check_validity function on these inputs.
    This test is successful if the check_validity function returns True for valid guesses and False for invalid guesses.
    """

    # Creating a test sudoku array
    sudoku = np.array(
        [
            [4, 0, 9, 1, 0, 5, 0, 0, 6],
            [0, 0, 1, 0, 7, 4, 9, 8, 2],
            [3, 0, 0, 0, 0, 2, 0, 0, 1],
            [9, 0, 0, 5, 3, 0, 6, 2, 0],
            [0, 5, 0, 0, 0, 9, 0, 1, 0],
            [0, 0, 3, 8, 2, 7, 0, 0, 0],
            [8, 3, 2, 4, 0, 6, 1, 7, 5],
            [0, 0, 0, 0, 1, 8, 0, 0, 9],
            [0, 0, 0, 0, 0, 0, 2, 0, 0],
        ]
    )

    # Testing valid guesses in the column:
    assert check_guess(sudoku, 2, (0, 1))
    assert check_guess(sudoku, 7, (2, 2))
    # Testing invalid guesses in the column:
    assert not check_guess(sudoku, 9, (7, 7))
    assert not check_guess(sudoku, 1, (7, 0))

    # Testing valid guesses in the row:
    assert check_guess(sudoku, 6, (4, 2))
    assert check_guess(sudoku, 3, (7, 7))
    # Testing invalid guesses in the row:
    assert not check_guess(sudoku, 7, (5, 6))
    assert not check_guess(sudoku, 4, (0, 7))

    # Testing valid guesses in sub-boxes:
    assert check_guess(sudoku, 9, (6, 4))
    # Testing invalid guesses in sub-boxes:
    assert not check_guess(sudoku, 6, (2, 7))
