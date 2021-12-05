# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random

# Steps:
# 1. Call function startup, this will ask if the user is ready to guess the number.
def startup():
    user_opt1 = input('Are you ready to guess the number? [y/n]: ')
    if user_opt1 == 'y': # 'y' = yes, indicates that he or she is ready to guess the number; it will also generate a random number for the user to guess, and the function usernumber will be called along with the random number.
        sysnumber = random.randint(0,100)
        usernumber(sysnumber)
    else: # The user answer isn't ready to guess the number.
        print('Be ready next time.')
        exit()

# 2. This function will ask the user to input a number to guess the secret number. 
def usernumber(sysnumber):
    userguess = int(input('What do you thimk is the number? [0-100]: '))
    if userguess < 0 or userguess > 100: # The user inputted/guessed a number that is less than 0 or greater than 100.
        print('Guess only from 0 to 100')
        usernumber(sysnumber)
    else: # The user inputted/guessed a number within the range from 0 to 100 and the function Guessing will be callled along with the user number and random number.
        Guessing(userguess, sysnumber)

# 3. This function will check if the guessed number of the user is correct or wrong.
def Guessing(userguess, sysnumber):
    while userguess != sysnumber: # The number of the user is wrong, while if the number is correct it will proceed to call the function guessedcorrect.
        print('Wrong.')
        if userguess > sysnumber: # The guessed number of the user is greater than the random number.
            print('Greater than...')
            usernumber(sysnumber)
        else: # The guessed number of the user is less than the random number.
            print('Less than...')
            usernumber(sysnumber)
    guessedcorrect(sysnumber)

# 4. This function will only called if you are correct.
def guessedcorrect(sysnumber):
    print(f'Correct!!! You have guessed the number {sysnumber}.')
    exit()

startup()