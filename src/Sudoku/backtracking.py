"""!@file backtracking.py
@brief Module containing functions for backtracking algorithm.

@details This module contains functions for backtracking algorithm.
Explain each function in detail here.

# Functions
    check_guess
        Checks the validity of the guess placed in the empty cell.

    find_empty
        Finds the next empty cell in the sudoku.


# Examples
    Say how to use the function here.

@author Created by S.M. Daloglu on 20/11/2023
"""

# Load Modules:
import numpy as np


def check_guess(sudoku: np.ndarray, guess: int, position: tuple) -> bool:
    """!@brief Checks the validity of the guess placed in the empty cell.

    @details This function checks the validity of the guess placed in the empty cell.

    @param sudoku: Sudoku to be solved.
    @param guess: Guess to be checked for validity.
    @param position: Coordinates of the empty cell used for guessing.

    @return True if the guess is valid, False if the guess is invalid.s


    """

    # Checking the validty of the guess in the cell:

    # Extracting the coordinates of the empty cell containing the guess
    x, y = position[0], position[1]

    # Calculating the coordinates of the 3x3 box in which the guess is located
    x_box = (x // 3) * 3
    y_box = (y // 3) * 3
    box_y_range = [y_box, y_box + 1, y_box + 2]
    box_x_range = [x_box, x_box + 1, x_box + 2]

    for i in box_x_range:
        for j in box_y_range:
            if sudoku[i, j] == guess and (i, j) != position:
                return False

    # Checking the validity of the guess in the column:

    for i in range(len(sudoku[0])):
        if sudoku[i, y] == guess and i != x:
            return False

    # Checking the validity of the guess in the row:

    for j in range(len(sudoku)):
        if sudoku[x, j] == guess and j != y:
            return False

    # If the guess is valid then return True
    return True


def find_empty(sudoku: np.ndarray) -> tuple:
    """!@brief Finds the next empty cell in the sudoku.

    @param sudoku: Sudoku to be checked for empty cells


    @return Coordinates of the empty cells
    """
    if isinstance(sudoku, np.ndarray) is False:
        print("->Input must be a numpy array for find_empty function.")
        return 0

    # Looping over the sudoku to find the next empty cell
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i, j] == 0:
                empty_cell = (i, j)
                return empty_cell

    # If no empty cell is found, return None
    return None
