"""!@file test_find_empty.py
@brief Test function to check the functionality of the find_empty function in the backtracking module.
@details  This function tests the behavior of the find_empty function in the backtracking.py module.
    It creates two test sudoku arrays, one with an empty cell and one with no empty cells (0 as an element).
    It then asserts the expected results of calling the find_empty function on these arrays.
    This test is successful if the find_empty function returns the correct coordinates of the empty cell when called on the array with an empty cell,
    and returns None when called on the array with no empty cells.


@author Created by S.M. Daloglu: smd89@cam.ac.uk on 05/12/2023
"""


from src.sudoku import backtracking as bt
import numpy as np


def test_find_empty():
    """!@brief Test for find_empty function in backtracking.py
    @details This function tests the behavior of the find_empty function in the backtracking.py module.
    It creates two test sudoku arrays, one with an empty cell and one with no empty cells (0 as an element).
    It then asserts the expected results of calling the find_empty function on these arrays.
    This test is successful if the find_empty function returns the correct coordinates of the empty cell when called on the array with an empty cell,
    and returns None when called on the array with no empty cells.
    """

    # Creating a test sudoku array with no empty boxes (0 as an element)
    sudoku1 = np.array([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])

    # Creating a test sudoku array with one empty box at index (2,2)
    sudoku2 = np.array([[1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1]])

    assert bt.find_empty(sudoku1) is None
    assert bt.find_empty(sudoku2) == (1, 2)
