# Guess the number

This program allows computer to guess the number from 1 to 100 by itself using binary search

## Description

The computer selects a number, and then uses binary search to guess it. This method quickly declining
the range of possible numbers. It means that program achives the optimal result for searching the quess
number in minimal number of attempts.

## Functions

### guess_number

The **guess_number** function takes the desired number (**secret_number**) and the bounds of the range (**low_bound** and **high_bound**) as input, 
and returns the number of attempts needed to guess the number.

Arguments **low_bound** and **high_bound** are not neccesary --> 1 and 100 by default

### score_game

The **score_game** function calculates the avarage number of attempts needed to guess a number from 1 to 100 using the **guess_number** function

## Example Usage

import numpy as np

# Load funcitons from main program
from guess_number_optimized import guess_number
from guess_number_optimized import score_game

# Print the results
print(score_game(guess_number))