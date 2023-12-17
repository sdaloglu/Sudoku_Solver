"""!@file solve_sudoku.py
@brief Main Python script for the Sudoku solving algorithm.

@details This script takes a text file containing a Sudoku board as an input and outputs the solution to another text file named "input_file_name"_solved.txt.
A recursive backtracking algorithm is used to solve the Sudoku board.
The backtracking algorithm is a brute force method which tries
all possible values for the empty cells until it finds the correct one.
The algorithm reverts back to the previous configuration of the sudoku
table as soon as a contradiction is found with the current configuration.

# Examples
```
python src/solve_sudoku.py test_board/test_board_1.txt
```


@author Created by S.M. Daloglu: smd89@cam.ac.uk on 05/12/2023
"""

# Load Modules:
import sys
import os
import numpy as np
from sudoku import backtracking as bt
from sudoku import board as bd

# Extracting the input text file from the command line
input_file = sys.argv[1]

# Loading the input text file into a string, also returning the file object so it can be closed later
data, f = bd.load_txt(input_file)

# Converting the board from a string into to a 9x9 numpy array
sudoku_array = bd.board_to_array(data)

# Checking if the input board obeys sudoku rules
if bd.check_board(sudoku_array) is False:
    sys.exit(1)

# Create a count variable to keep track of the number of iterations in recursion
count = 0


def solve_sudoku(sudoku_array: np.ndarray) -> bool:
    """!@brief Solves Sudoku using the backtracking algorithm.
    @details Finds an empty cell in the sudoku board with the use of find_empty function.
    Then places a guess in the empty cell and checks if the guess is valid using the check_guess function.
    If the guess is valid, it is placed in the empty cell and the sudoku board is checked for completion.
    If the sudoku is not solved, the algorithm reverts back to the previous configuration of the Sudoku.
    The algorithm is repeated recursively until the Sudoku is solved.

    @param sudoku_array: Sudoku to be solved.

    @return True if the sudoku is solved, False if the sudoku is not solved.
    """

    global count
    count += 1

    if count == 1e6:
        # This implies that the backtracking algorithm is taking too long to solve
        print(
            "Backtracking algorithm is taking too long to solve this sudoku, no solution is found."
        )
        print("Please refer to other algorithms available online.")
        raise SystemExit

    if bt.find_empty(sudoku_array) is None:
        # This implies that the sudoku is solved
        return True

    else:
        empty_cell = bt.find_empty(sudoku_array)

    for guess in range(1, 10):
        # Make a guess and check if it is valid
        valid = bt.check_guess(sudoku_array, guess, empty_cell)
        if valid:
            # Assign the guess to the empty cell
            sudoku_array[empty_cell[0], empty_cell[1]] = guess

            # Recursive call to solve_sudoku function
            if solve_sudoku(sudoku_array):
                return True

            # Last assignment is not valid, revert back
            sudoku_array[empty_cell[0], empty_cell[1]] = 0

    return False


f.close()

# Solving the sudoku
solved_bool = solve_sudoku(sudoku_array)

if solved_bool is False:
    print("->Sudoku could not be solved.")
    print("->Sudoku is invalid.")
elif solved_bool is True:
    # Converting the solution numpy array into a string
    board = bd.array_to_board(sudoku_array)

    # Writing the solution to a .txt file
    # Split the input filename into file name and extension
    input_name, extension = os.path.splitext(input_file)

    # Script can be run both in the test_boards directory or the root directory.
    # Either way since the input_name includes the path to the input file,
    # the output file will be saved in the same directory as the input_file
    output_dir = "."
    output_name = input_name + "_solved.txt"

    # Save the solution to the output file in the same directory as the input file
    with open(os.path.join(output_dir, output_name), "w") as file:
        file.write(board)

    print("->Sudoku solved successfully.")
    print(f"->Please see the {input_name}_solved.txt file for the solution.")
    print("_______________________________________________\n")
    print(board)
    print("_______________________________________________")
