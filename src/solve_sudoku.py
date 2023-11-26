"""
    This code solves a sudoku puzzle using backtracking algorithm.

    Explain how it works step by step

    Backtracking algorithm is a brute force method which tries
    all possible values for the empty cells until it finds the correct one.

    The algorithm reverts back to the previous configuration of the sudoku
    table as soon as a contradiction is found with the current configuration.




    Written by Sabahattin Mert Daloglu: smd89@cam.ac.uk
"""


# Load Modules:
import sys
from sudoku import backtracking as bt
from sudoku import board as bd


# Extracting the input and the output file from the command line
input_file = sys.argv[1]

# Trapping files that can not be opened

try:
    f = open(input_file, "r")
except IOError:
    print("->Input file could not be opened. Please input a valid .txt file.")
else:
    print("->Input file opened successfully.")

    # Read the text file into a string
    data = f.read()


# Reading the input txt file and converting it to a 9x9 numpy array
sudoku_array = bd.board_to_array(data)


def solve_sudoku(sudoku_array):
    if bt.find_empty(sudoku_array) is None:
        return True

    else:
        empty_cell = bt.find_empty(sudoku_array)

    for guess in range(1, 10):
        valid = bt.check_validity(sudoku_array, guess, empty_cell)
        if valid:
            sudoku_array[empty_cell[0], empty_cell[1]] = guess

            # Recursive call to solve_sudoku function
            if solve_sudoku(sudoku_array):
                return True

            # Sequence of guesses is not valid, revert back
            sudoku_array[empty_cell[0], empty_cell[1]] = 0

    return False


f.close()

# Solving the sudoku
solved_bool = solve_sudoku(sudoku_array)

if solved_bool is False:
    print("->Sudoku could not be solved.")
elif solved_bool is True:
    print("->Sudoku solved successfully.")
    print("->Please see the output.txt file for the solution.")
    print("_______________________________________________\n")
    # Converting the solution numpy array into a .txt file
    board = bd.array_to_board(sudoku_array)
    print(board)
    print("_______________________________________________")


# Writing the solution to a .txt file
try:
    output = open("output.txt", "x")
except IOError:
    print("Output file could not be created")
else:
    output.write(board)
    output.close()
