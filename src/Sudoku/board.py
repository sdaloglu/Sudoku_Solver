"""!@file board.py
@brief Module containing functions for the Sudoku board manipulation and data parsing.
@details Functions include transforming the sudoku board from numpy array to string and vice versa.
Loading the the input text file containing the Sudoku board and converting it to a string.
Checking if the input Sudoku board is valid according to the Sudoku rules.



# Functions

## load_txt
    Loads the input text file into a string
## check_board
    Checks if the input board is a valid Sudoku board
## board_to_array
    Converts the Sudoku board from string type to 9x9 numpy array
## array_to_board
    Converts 9x9 numpy array to string of a Sudoku board


# Examples
The function load_txt loads an input .txt file in the following form:
```
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
```

and convert it into a string format as follows:
```
000|007|000/n000|009|504/n000|050|169/n---+---+---/n080|000|305/n075|000|290/n406|000|080/n---+---+---/n762|080|000/n103|900|000/n000|600|000
```
The function board_to_array takes the string format of the Sudoku board and converts it to a 9x9 numpy array.

The function array_to_board takes the 9x9 numpy array of the Sudoku board and converts it to a string format.


@author Created by S.M. Daloglu: smd89@cam.ac.uk on 05/12/2023
"""

# Load Modules:
import numpy as np
import sys


def load_txt(input_file) -> str:
    """!@brief Loads the input text file
    @details An input text file containing the Sudoku board is loaded into a string.
    Any possible errors while opening input file are trapped.

    @param input_file: Input text file containing the Sudoku board

    @return Sudoku board as a string
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
    """!@brief Checks if the input board is a valid sudoku board
    @details This function checks if the input board is a valid sudoku board according to the Sudoku rules.

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
    """!@brief Converts the Sudoku board from string type to 9x9 numpy array
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
    """!@brief Converts a 9x9 numpy array to string of a Sudoku board
    @param board: Solved Sudoku board as a 9x9 numpy array

    @return Solved Sudoku board as a string

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

    # Adding vertical spaces between 3 rows
    for i in range(36, 109, 37):
        sudoku_array = np.insert(sudoku_array, i, "\n\n")

    board = "".join(sudoku_array)

    # Adding the separation lines between every 3 rows
    inline = "---+---+---"
    board = board[:36] + inline + board[36:73] + inline + board[73:]

    return board
