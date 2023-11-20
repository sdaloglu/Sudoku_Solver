"""!@file sudoku_backtracking.py
@brief Module containing tools for backtracking algorithm in solving sudoku.

@details This module contains tools for backtracking algorithm in solving sudoku.
@author Created by S.M. Daloglu on 20/11/2023
"""


"""
This Module contains functions .... to create ...

Contains:
----------------------------------------
    function name
        What the function does 
    function name
        What the function does
----------------------------------------
        
        
All functions take x arguments:
----------------------------------------
    arg1
        explain arg1
    arg2
        explain arg2
----------------------------------------

Calculation is done by ....

Written by Sabahattin Mert Daloglu: smd89@cam.ac.uk
"""


def check_validity(sudoku):
    """
    !@brief Sudoku solving algorithm using backtracking
    
    Parameters:
    -----------
    @param sudoku: 9x1 numpy array
        Sudoku to be solved
    
        
    Returns:
    --------
    
    @return solved_sudoku: 9x1 numpy array
        Solved sudoku
        
    """
    
    #Finding the next empty box in the sudoku
    empty_box = find_empty(sudoku)
    
    

def find_empty(sudoku):
    """
    !@brief Finds the next empty box in the sudoku
    
    Parameters:
    -----------
    @param sudoku: 9x1 numpy array
        Sudoku to be checked for empty boxes
    
        
    Returns:
    --------
    
    @return empty_box: tuple
        Tuple containing the coordinates of the empty boxes
    """
    
    #Looping over the sudoku to find the next empty box
    for i in range(9):
        for j in range(9):
            if sudoku[i,j] == 0:
                empty_box = (i,j)
                return empty_box
            
    #If there is no empty box, return None
    return None
