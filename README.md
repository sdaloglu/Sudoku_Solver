# C1: Research Computing - Coursework Assignment


## Description

This project contains the code required to answer coursework questions for the Research Computing course. The goal of this project is to demonstrate a well-structured, modular software development of the backtracking algorithm for Sudoku solving. The advantages of the backtracking algorithm include a guaranteed solution for a valid Sudoku and a relatively straightforward code implementation. Although given enough time, the backtracking algorithm provides a solution to every Sudoku board, for the sake of simplicity the software for this coursework was designed to stop after 10<sup>6</sup> recursive iterations. An alternative algorithm is recommended for Sudoku boards that are designed to challenge the backtracking algorithm.

## Problem Setting
The first step is to clone the remote GitLab repository on a local machine. This project does not provide an automated cloning command inside the `Dockerfile` to avoid authentication errors.

To use the software, provide an input text file containing an incomplete 9x9 grid in the following form. The zeros representing unknown values and `|`,`+`,`-` separating cells. The text file should be placed in the `test_boards` directory, before running the software.

```
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
```

## Environment

This project can be easily run inside a Docker container specified with instructions listed inside the Dockerfile provided in the project. To build the docker image from the Dockerfile, run the following at the root directory of the project:

```bash
docker build -t rc .
```

To create the container using the image:

```bash
docker run --rm -ti --name rc_container rc
```

This will create a linux machine with the required conda environment named `rc` activated and a bash terminal open to run the commands below. All the required files inside the project in order to run the software, assuming a local copy was made previously, are copied inside the container ready to be used.


## Running the main algorithm

The main Sudoku solving algorithm is located inside the `solve_sudoku.py` script. The two ways to run the main function inside the container are given below:

```bash
python src/solve_sudoku.py test_boards/input.txt
```
This command should be run from the root directory. The solution to the Sudoku board inside the `input.txt` file is output on the terminal. The solution is also saved as a text file named `$input_file_name$_solved.txt`.

```bash
python ../src/solve_sudoku.py input.txt
```
An alternative way to run the main algorithm is from the `test_boards` directory. Regardless of the choice, the output text file is always saved inside the directory where the input text file is located. One should make sure to place the input text file inside the `test_boards` directory before running the software.



## Documentation
The documentation of this project can be obtained by running the following command on the terminal inside the `docs` directory

```bash
doxygen
```
This command builds the documentation for the project in `html` and `latex` formats. Inside the `html` directory, `index.html` file can be referenced for the documentation.



## Copying files from the container to the local

Files inside the container such as documentation, or solution text files can be transferred to the local filesystem. An example of copying the files inside `test_boards` directory containing the input Sudoku boards and their corresponding solutions is shown below. This command should be run on the local terminal.

```bash
docker cp rc_container:/app/test_boards/. ../
```
`rc_container` should match the name of the container. `../` is the path to the local destination.

## The use of generative A.I.
Generative AI was used during the process of making Sudoku test boards for the validation section. The prompt submitted to ChatGPT 3.5 is given below:

```
Can you generate 10 test sudoku boards as a text file in the following format?

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

Where 0's represent empty cells.

```

```
Generate 5 more test sudoku boards in the same format but this time increase the difficulty of Sudokus, and make them harder especially for a solver using the backtracking algorithm.

```
ChatGPT was also used for suggesting alternative wordings and grammar suggestions while writing the report. The following prompts were used during this process

```
What is another word for <input word>?
```
```
Is this sentence grammatically correct? <input sentence>
```
```
Is this paragraph clear for a reader? <input paragraph>
```
```
How to rephrase this sentence to make it more clear? <input sentence>
```
The outputs were partially adapted in a way that only alternative wordings were used and not the whole output while rephrasing the Introduction and Summary parts of the report.

Furthermore, the suggestions from the autocomplete feature of `GitHub Copilot` were utilized during the documentation of the unit testing functions, and code development of the project.

## Authors
Sabahattin Mert Daloglu

## License
This project is licensed under the BSD-3-Clause  License - see the [LICENSE](LICENSE) for details.
