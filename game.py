""" Guess the number
Computer make a wish and guess by itself"""

import numpy as np

def random_predict(number:int=1) -> int:
    """ Random guess the number

    Args:
        number (int, optional): Wish number. Defaults to 1.

    Returns:
        int: number of tries
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # guess number
        
        if number == predict_number:
            break # End of a cycle
    return count

def score_game(random_predict) -> int:
    """How many times of guesses needed that guess the number for 1000 times

    Args:
        random_predict (_type_): function of guessing

    Returns:
        int: avarage number of tries
    """
    count_ls = []
    np.random.seed(1) # fix the sid for 
    random_array = np.random.randint(1, 101, size=(1000)) # list of number
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"Your algorithm guess the number avarage for {score} tries")
    return score

print(score_game(random_predict))
#print(f"number of tries {random_predict(10)}")
    