"""!@file test_check_board.py
@brief Test function to check the functionality of the check_board function in the board module.
@details This function tests the behavior of the check_board function in the board.py module.
    It creates two test sudoku arrays, one valid and one invalid.
    Then, it checks if the check_board function correctly identifies test boards that follow the Sudoku rules,
    which prohibit repeating numbers in rows, columns, or 3x3 boxes.
    This test is successful if the check_board function returns True for the valid board and False for the invalid board.


@author Created by S.M. Daloglu: smd89@cam.ac.uk on 05/12/2023
"""


import numpy as np
from src.sudoku.board import check_board


def test_check_board():
    """!@brief Test for check_board function in board module
    @details This function tests the behavior of the check_board function in the board.py module.
    It creates two test sudoku arrays, one valid and one invalid.
    Then, it checks if the check_board function correctly identifies test boards that follow the Sudoku rules,
    which prohibit repeating numbers in rows, columns, or 3x3 boxes.
    This test is successful if the check_board function returns True for the valid board and False for the invalid board.

    """

    # Creating a valid sudoku board
    valid_board = np.array(
        [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
    )

    # Creating an invalid sudoku board with repeating number 5 in the last column
    invalid_board1 = np.array(
        [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 5],
        ]
    )

    # Creating an invalid sudoku board with repeating number 9 in the last row
    invalid_board2 = np.array(
        [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [9, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
    )

    # Creating an invalid sudoku board with repeating number 5 in the first 3x3 box
    invalid_board3 = np.array(
        [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 5, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
    )

    assert check_board(valid_board)
    assert not check_board(invalid_board1)
    assert not check_board(invalid_board2)
    assert not check_board(invalid_board3)
