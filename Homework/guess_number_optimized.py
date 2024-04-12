""" Guess the number
Computer make a wish and guess by itself
"""

import numpy as np

def guess_number(secret_number:int=1, low_bound:int=1, high_bound:int=100) -> int:
    """Guess the number using the binary search

    Args:
        secret_number (int, optional): Wish number. Defaults to 1.
        low_bound (int, optional): lower bound for the guessed number. Defaults to 1.
        high_bound (int, optional): higher bound for the guessed number. Defaults to 100.

    Returns:
        int: number of attempts
    """
    
    # Checking the boundaries of wish number
    if secret_number < low_bound:
        raise ValueError(f"number {secret_number} is less than acceptable {low_bound}")
    elif secret_number > high_bound:
        raise ValueError(f"number {secret_number} is more than acceptable {high_bound}")
    
    attempts = 0
    # Repeat while not guess the correct number
    while True:
        guess = (low_bound + high_bound) // 2
        attempts += 1
        
        # Guess number correct -> end cycle
        # Else moving the boundaries
        if guess == secret_number:
            return attempts
            #break
        elif guess < secret_number:
            low_bound = guess + 1
        else:
            high_bound = guess - 1

def score_game(guess_number) -> int:
    """Whats the avarage times of attempts needs to guess the number from 1 to 100

    Args:
        guess_number (_type_): function for guessing wish number

    Returns:
        int: avarage number of attempts
    """
    
    random_array = np.random.randint(1, 101, size=(1000))
    
    # map faster then 'for' cycle
    count_result = list(map(guess_number, random_array))
    result = int(np.mean(count_result))  
    return f"Your algorithm guess the number avarage for {result} tries"


# Run the program
if __name__ == "__main__":
    print(score_game(guess_number))
