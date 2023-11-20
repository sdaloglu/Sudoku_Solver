import numpy as np
import sys

#Extracting the input and the output file from the command line
input_file = sys.argv[1]
output_file = sys.argv[2]



#Sudoku solving algorithms

#Backtracking algorithm


def sudoku_backtraking(sudoku):
    """
    Sudoku solving algorithm using backtracking
    
    Parameters:
    -----------
    sudoku: 9x1 numpy array
        Sudoku to be solved
        
    Returns:
    --------
    
    solved_sudoku: 9x1 numpy array
        Solved sudoku
        
    """


