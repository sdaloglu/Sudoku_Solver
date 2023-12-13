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

    # Calculating the starting coordinates of the 3x3 box in which the guess is located
    x_box = (x // 3) * 3
    y_box = (y // 3) * 3

    # Checking the validity of the guess in the 3x3 box:
    if np.any(sudoku[x_box : x_box + 3, y_box : y_box + 3] == guess):
        return False

    # Checking the validity of the guess in the column:
    if np.any(sudoku[:, y] == guess):
        return False

    # Checking the validity of the guess in the row:
    if np.any(sudoku[x, :] == guess):
        return False

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
