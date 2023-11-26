# Load Modules:
import numpy as np

"""!@file board.py
@brief Module containing functions for building a visual board
in .txt format form numpy array or vise verca.

@details This module contains functions for building a visual board
in .txt format form numpy array or vise verca.
@author Created by S.M. Daloglu on 20/11/2023
"""


"""
This Module contains functions .... to create ...

Contains:
----------------------------------------
    board_to_array
        What the function does
    array_to_board
        What the function does
----------------------------------------


All functions take x arguments:
----------------------------------------
    arg1
        explain arg1
    arg2
        explain arg2
----------------------------------------

The function board_to_array takes a .txt file such as:

000|007|000
000|009|504
000|050|169
---+---+---
080|000|305
075|000|290
406|000|080
---+---+---
762|080|000
103|900|000
000|600|000

and converts it to a 9x9 numpy array in the form of:

[[0,0,0,0,0,7,0,0,0],[0,0,0,0,0,9,5,0,4],[0,0,0,0,5,0,1,6,9],[0,8,0,0,0,0,3,0,5],[0,7,5,0,0,0,2,9,0],[4,0,6,0,0,0,0,8,0],[7,6,2,0,8,0,0,0,0],[1,0,3,9,0,0,0,0,0],[0,0,0,6,0,0,0,0,0]]

Written by Sabahattin Mert Daloglu: smd89@cam.ac.uk
"""


def board_to_array(board):
    """
    !@brief Converts .txt file of a sudoku board to 9x9 numpy array

    Parameters:
    -----------
    @param board: string
        Sudoku to be solved in string format

    Returns:
    --------

    @return sudoku_array: 9x9 numpy array
        Explain parameter

    """
    # Creating the outer array of the 2D sudoku which will store 9 row (inner)arrays
    data_array = np.array([])

    # Creating the inner array of the 2D sudoku which will store 9 numbers
    row_array = np.array([])

    # Creating an array of sudoku numbers to search for in the board
    sudoku_numbers = np.array(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

    for value in board:
        if value in sudoku_numbers:
            row_array = np.append(row_array, value)

            if len(row_array) == 9:
                data_array = np.append(data_array, row_array)

                # Emptying the row_array for the next row
                row_array = np.array([])

    # Converting elements in the array from string to integer
    data_array = [eval(i) for i in data_array]

    try:
        # Reshaping the array into a 9x9 numpy array
        sudoku_array = np.reshape(data_array, (9, 9))
    except ValueError:
        print(
            "->You have entered an invalid sudoku board."
            "\n->Please check your input text file is in the following format"
            "\n->0 representing empty cells and numbers representing filled cells"
            "\n->81 cells in total, separated by |, + and - as shown below:"
        )
        print(
            "\n000|007|000\n000|009|504\n000|050|169\n---+---+---\n080|000|305\n075|000|290\n406|000|080\n---+---+---\n762|080|000\n103|900|000\n000|600|000"
        )
    else:
        return sudoku_array


def array_to_board(sudoku_array):
    """
    !@brief Converts 9x9 numpy array to .txt file of a sudoku board

    Parameters:
    -----------
    @param sudoku_array: 9x9 numpy array
        Sudoku board represented as a 9x9 numpy array

    Returns:
    --------

    @return sudoku board: .txt file of a sudoku board
        Sudoku board represented as a .txt file such as:
        000|007|000
        000|009|504
        000|050|169
        ---+---+---
        080|000|305
        075|000|290
        406|000|080
        ---+---+---
        762|080|000
        103|900|000
        000|600|000

    """

    # Flatten out the input array into a one dimensional array
    sudoku_array = np.reshape(sudoku_array, (1, 81))[0]

    # Convert the array into a list of strings
    sudoku_array = [str(i) for i in sudoku_array]

    wall_index = [3, 6, 12, 15, 21, 24, 30, 33, 39, 42, 48, 51, 57, 60, 66, 69, 75, 78]
    sudoku_array = np.insert(sudoku_array, wall_index, "|")

    # Adding new lines to the array
    for i in range(11, 109, 12):
        sudoku_array = np.insert(sudoku_array, i, "\n")

    # Adding spaces between 3 rows
    for i in range(36, 109, 37):
        sudoku_array = np.insert(sudoku_array, i, "\n\n")

    board = "".join(sudoku_array)

    inline = "---+---+---"
    board = board[:36] + inline + board[36:73] + inline + board[73:]

    return board
