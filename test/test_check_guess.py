from src.sudoku.backtracking import check_validity
import numpy as np


def test_check_guess():
    """
    Test for check_guess function in backtracking.py

    This function tests the behavior of the check_validity function in the backtracking.py module.
    It creates a test sudoku array and checks the validity of different guesses in different positions.
    It then asserts the expected results of calling the check_validity function on these inputs.

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
    assert check_validity(sudoku, 2, (0, 1))
    assert check_validity(sudoku, 7, (2, 2))
    # Testing invalid guesses in the column:
    assert not check_validity(sudoku, 9, (7, 7))
    assert not check_validity(sudoku, 1, (7, 0))

    # Testing valid guesses in the row:
    assert check_validity(sudoku, 6, (4, 2))
    assert check_validity(sudoku, 3, (7, 7))
    # Testing invalid guesses in the row:
    assert not check_validity(sudoku, 7, (5, 6))
    assert not check_validity(sudoku, 4, (0, 7))

    # Testing valid guesses in sub-boxes:
    assert check_validity(sudoku, 9, (6, 4))
    # Testing invalid guesses in sub-boxes:
    assert not check_validity(sudoku, 6, (2, 7))
