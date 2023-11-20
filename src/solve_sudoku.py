"""
    This code solves a sudoku puzzle using backtracking algorithm.
    
    Explain how it works step by step
    
    Backtracking algorithm is a brute force method which tries all possible values for the empty boxed until it finds the correct one.
    The algorithm reverts back to the previous configuration of the sudoku table as soon as a contradiction is found with the current configuration.
    
    
    
    
    Written by Sabahattin Mert Daloglu: smd89@cam.ac.uk
"""


#Load Modules:
import numpy as np
import sys
from Sudoku import backtracking as bt
from Sudoku import board as bd

#bt.check_validity

#bt.find_empty

#bd.array_to_board



#Extracting the input and the output file from the command line
input_file = sys.argv[1]
f = open(input_file, "r")
data = f.read()   #Read the text file into a string


#output_file = sys.argv[2]
#f.close()


#Reading the input txt file and converting it to a 9x9 numpy array
sudoku_array = bd.board_to_array(data)


print(sudoku_array)


#Sudoku solving algorithms

#Backtracking algorithm



    


