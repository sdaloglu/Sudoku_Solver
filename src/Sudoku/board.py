"""!@file board.py
@brief Module containing functions for sudoku board manipulation.

the input text file and transforming the sudoku board between numpy array to .txt file.

@details Functions include transforming the sudoku board from numpy array to string and vice versa.
Loading the the input text file containing the sudoku board and converting it to a string.

in .txt format form numpy array or vise verca.

This Module contains functions .... to create ...

# Contains
    board_to_array
        What the function does
    array_to_board
        What the function does


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

@author Created by S.M. Daloglu on 20/11/2023
"""

# Load Modules:
import numpy as np
import sys


def load_txt(input_file) -> str:
    """!@brief Loads the input text file

    @details This function loads the input text file from the command line
    and reads the text file into a string

    @return
    """

    # Trapping files that can not be opened
    try:
        f = open(input_file, "r")
    except IOError:
        print("->Input file could not be opened. Please input a valid .txt file.")
    else:
        print("->Input file opened successfully.")

        # Read the text file into a string
        data = f.read()

        return data, f


def check_board(board: np.ndarray) -> bool:
    """!@brief Checking if the input board is a valid sudoku board

    @param board: Input Sudoku board to be checked for validity

    @return True if the board is valid, False if the board is invalid
    """
    # Writing a function to check if all numbers in a given sudoku obeys the sudoku rules
    # Checking if all rows are valid
    for row in range(9):
        row_array = board[row, :]
        row_array = row_array[row_array != 0]
        size = len(row_array)
        if len(np.unique(row_array)) != size:
            print("Repeating numbers were found in row {}".format(row + 1))
            print("Please enter a valid sudoku board")
            return False
    # Checking if all columns are valid
    for col in range(9):
        col_array = board[:, col]
        col_array = col_array[col_array != 0]
        size = len(col_array)
        if len(np.unique(col_array)) != size:
            print("Repeating numbers were found in column {}".format(col + 1))
            print("Please enter a valid sudoku board")
            return False

    # Checking if all 3x3 boxes are valid
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            box_array = board[row : row + 3, col : col + 3]

            # Flatten the box array
            box_array = box_array.flatten()
            box_array = box_array[box_array != 0]
            size = len(box_array)
            if len(np.unique(box_array)) != size:
                print(
                    "Repeating numbers were found in the box whose top left element has coordinates {}".format(
                        (row + 1, col + 1)
                    )
                )
                print("Please enter a valid sudoku board")
                return False
    return True


def board_to_array(board: str) -> np.ndarray:
    """!@brief Converts sudoku board from string type to 9x9 numpy array

    @details This function converts .txt file of a sudoku board to 9x9 numpy array

    @param board: Sudoku to be solved in string format


    @return Sudoku to be solved as a 9x9 numpy array


    """
    # Creating the outer array of the 2D sudoku which will store 9 row (inner)arrays
    data_array = np.array([])

    # Creating the inner array of the 2D sudoku which will store 9 numbers
    row_array = np.array([])

    # Creating an array of sudoku numbers as string type to search for in the board
    sudoku_numbers = np.arange(0, 10, 1).astype(str)

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
        sys.exit(1)
    else:
        return sudoku_array


def array_to_board(sudoku_array: np.ndarray) -> str:
    """!@brief Converts 9x9 numpy array to string of a sudoku board

    @details This function converts 9x9 numpy array to .txt file of a sudoku board
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

    @param sudoku_array: 9x9 numpy array
        Sudoku board represented as a 9x9 numpy array

    @return string file of a sudoku board


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
