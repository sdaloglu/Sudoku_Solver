"""!@file backtracking.py
@brief Module containing functions for the backtracking algorithm.

@details Functions include finding an empty cell in the Sudoku board and checking the validity of a guess placed in the empty cell.

# Functions

## find_empty
    Finds an empty cell in the Sudoku board.

## check_guess
    Checks if the guess placed in the empty cell follows the Sudoku rules.



# Examples
    A sudoku board can be solved using the backtracking algorithm as follows:
    First an empty cell is found using the find_empty function. An input 2d numpy array is required for this function.
    Then a guess is placed in the empty cell and the validity of the guess is checked using the check_guess function.
    If the guess is valid, the guess is placed in the empty cell and the sudoku board is checked for completion.

@author Created by S.M. Daloglu: smd89@cam.ac.uk on 05/12/2023
"""

# Load Modules:
import numpy as np


def find_empty(sudoku: np.ndarray) -> tuple:
    """!@brief Finds an empty cell in the Sudoku board.
    @details A 2 dimensional search is performed on the Sudoku board to find a cell containing zero as an element.

    @param sudoku: Sudoku to be checked for empty cells (values of zero).

    @return Coordinates of the empty cells
    """
    if isinstance(sudoku, np.ndarray) is False:
        print("->Input must be a numpy array for find_empty function.")
        return 0

    # Find indices of zero elements
    indices = np.where(sudoku == 0)

    # Check if any zero element is found
    if indices[0].size > 0:
        return indices[0][0], indices[1][0]
    else:
        return None


def check_guess(sudoku: np.ndarray, guess: int, position: tuple) -> bool:
    """!@brief Checks if the guess placed in the empty cell follows the Sudoku rules.
    @details An input guess is checked for uniqueness in the 3x3 box, row and column of the empty cell.

    @param sudoku: Sudoku to be solved.
    @param guess: Guess to be checked for validity.
    @param position: Coordinates of the empty cell used for guessing.

    @return True if the guess is valid, False if the guess is invalid.


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
