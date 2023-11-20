"""!@file board.py
@brief Module containing functions for building a visual board in .txt format form numpy array or vise verca.

@details This module contains functions for building a visual board in .txt format form numpy array or vise verca.
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

#Load Modules:
import numpy as np

def board_to_array(board):
    
    """
    !@brief Sudoku solving algorithm using backtracking
    
    Parameters:
    -----------
    @param board: string
        Sudoku to be solved in string format
    
    Returns:
    --------
    
    @return sudoku_array: 9x9 numpy array
        Explain parameter
        
    """
    data_array = np.array([])
    numbers = np.array(['0','1','2','3','4','5','6','7','8','9'])
    inside_array = np.array([])

    for value in board:

        if value in numbers:
            inside_array = np.append(inside_array,value)
        
            if len(inside_array) == 9:
            
                data_array = np.append(data_array,inside_array)
                inside_array = np.array([])
    
    
    sudoku_array = np.reshape(data_array,(9,9))
    
    
    return sudoku_array
    
    
    
    
def array_to_board(sudoku_array):
    sudoku_board = sudoku_array
    return sudoku_board