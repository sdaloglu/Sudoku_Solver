Instructions for running the code:
 - Add pre-comit instructions - running >pre-commit install explain continous integration and git hooks
 - Add doxygen instructions (maybe?) - runing >doxygen in the docs folder and openning index.html


 Instructions for running Docker:
 - from the directory Dockerfile is in, run:

 > docker build -t conda .
 > docker run --rm -ti conda

 Instructions for running the code at root level directory:

 >python src/solve_sudoku.py test_boards/input.txt
