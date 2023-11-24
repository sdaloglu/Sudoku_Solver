from src.sudoku import backtracking as bt
import numpy as np


def test_find_empty():
    """
    Test for find_empty function in backtracking.py

    This function tests the behavior of the find_empty function in the backtracking.py module.
    It creates two test sudoku arrays, one with no empty boxes and one with one empty box.
    It then asserts the expected results of calling the find_empty function on these arrays.

    """

    # Creating a test sudoku array with no empty boxes (0 as an element)
    sudoku1 = np.array([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])

    # Creating a test sudoku array with one empty box at index (2,2)
    sudoku2 = np.array([[1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1]])

    assert bt.find_empty(sudoku1) is None
    assert bt.find_empty(sudoku2) == (1, 2)
