"""!@file sudoku
@brief Package containing backtracking module and board module.

@details Package containing backtracking module and board module.

>>> import sudoku as sdk


# Modules
    backtracking
        Module containing functions for backtracking algorithm:
        check_guess
            Checks the validity of the guess placed in the empty cell.
        find_empty
            Finds the next empty cell in the sudoku.

    board
        Module containing functions for building a visual board in .txt format form numpy array or vise verca:
        board_to_array
            Converts .txt file of a sudoku board to 9x9 numpy array
        array_to_board
            Converts 9x9 numpy array to .txt file of a sudoku board



@author Created by S.M. Daloglu on 20/11/2023
"""
