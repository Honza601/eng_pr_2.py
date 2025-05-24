"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jan Čambor
email: jan.cambor@gmail.com
"""

import random

line = "-" * 47

def greet():
    """
    This function greets the user.
    """
    print("Hi there!", line, """I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""",line,"Enter a number:", line, sep="\n")

def generate_random_number():
    """
    This function generates a unique 4-digit number
    that must not start with 0.
    """
    digits = list("123456789")
    first_digit = random.choice(digits) 
    remaining_digits = list(set("0123456789")- {first_digit})
    other_digits = random.sample(remaining_digits,3) 
    print("\"Secret\" number - ",first_digit + "".join(other_digits))   #print of secret number for testing purposes
    return first_digit + "".join(other_digits)

def guess_rules(guess):
    """
    This function checks the rules for the 
    guessed number. 
    """
    if len(guess)!= 4:
        print("Please enter 4 digits.")
        return False
    if not guess.isdigit():
        print("Please enter only digits.")
        return False
    if guess[0] == "0":
        print("The first digit cannot be 0.")
        return False
    if len(set(guess)) != 4:
        print("The digits must be unique.")
        return False
    return True

def plural(count, word):
    """
    This function adds an "s" ending to distinguish
    between singular and plural.
    """
    if count == 1:
        return word
    else:
        return word + "s"

def game(secret_number):
    """
    This function evaluates the user's guess.
    """
    
    attempts = 0
    while True:
        guess = input(">>> ")
        if not guess_rules(guess):
            continue

        attempts += 1
        bulls = sum(guess[i] == secret_number[i] for i in range(4))
        cows = sum(c in secret_number for c in guess) - bulls
        
        if bulls == 4:
            print(f"""Correct, you've guessed the right number
in {attempts} guesses! 
{line}
That's amazing!
""") 
            break
        else:
            print(f"{bulls} {plural(bulls, "bull")}, {cows} {plural(cows, "cow")}")
            print(line)

if __name__ == "__main__":
    greet()
    secret = generate_random_number()
    game(secret)