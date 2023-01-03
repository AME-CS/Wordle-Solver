# Wordle-Solver
A script that solves the Wordle puzzle game optimally.

Requirements
Python 3
Usage
Run the solver.py script and it will play the game optimally.

How it works
The script filters through a list of all valid English words and checks which ones are valid guesses according to the given information in the Wordle puzzle. It then ranks the valid guesses based on their uniqueness and letter frequency scores, and makes the highest ranked guess. If the guess is incorrect, the script updates the list of invalid letters and the correctly placed letters in the puzzle and repeats the process until the correct word is found.
