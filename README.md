Instructions for running the code:
 - Add pre-comit instructions - running >pre-commit install explain continous integration and git hooks
 - Add doxygen instructions (maybe?) - runing >doxygen in the docs folder and openning index.html


 Instructions for running Docker:
 - from the directory Dockerfile is in, run:

 > docker build -t conda .
 > docker run --rm -ti conda

 Instructions for running the code inside /test_boards directory:
 First place the input .txt file inside /test_boards directory
 >python ../src/solve_sudoku.py input.txt
