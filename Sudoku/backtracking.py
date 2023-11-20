"""!@file backtracking.py
@brief Module containing functions for backtracking algorithm in solving sudoku.

@details This module contains functions for backtracking algorithm in solving sudoku.
@author Created by S.M. Daloglu on 20/11/2023
"""


"""
This Module contains functions .... to create ...

Contains:
----------------------------------------
    check_validity
        What the function does 
    find_empty
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


def check_validity(sudoku,guess, position):
    """
    !@brief Sudoku solving algorithm using backtracking
    
    Parameters:
    -----------
    @param sudoku: 9x1 numpy array
        Sudoku to be solved
        
    @param guess: int
        Guess to be checked for validity
        
    @param position: tuple
        Tuple containing the coordinates of the empty box used for guessing
    
    
    Returns:
    --------
    
    @return Boolian:
        True if the guess is valid, False if the guess is invalid
    
        
    """
    
    #Checking the validty of the guess in the box:
    
    #Extracting the coordinates of the empty box containing the guees
    x,y = position[0], position[1]
    
    #Caclutaing the coordinates of the box in which the guess is located
    box_y_range = np.array([y-1,y,y+1])
    box_x_range = np.array([x-1,x,x+1])
    
    for i in box_x_range:
        for j in box_y_range:
            if sudoku[i,j] == guess:
                return False
    
    #Checking the validity of the guess in the column:
    
    for i in range(len(sudoku)):
        if sudoku[i,y] == guess:
            return False
    
    #Checking the validity of the guess in the row:
    
    for j in range(len(sudoku)):
        if sudoku[x,j] == guess:
            return False
    
    #If the guess is valid then return True
    return True


    

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
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i,j] == 0:
                empty_box = (i,j)
                return empty_box
            
            
    #If no empty box is found, return None
    return None
