# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random

def startup():
    user_opt1 = input('Do you want to try your luck? [y/n]: ')
    if user_opt1 == 'y':
        Lottery()
    else:
        print('You just missed your chance to win a lot of money.')
        exit()

def Lottery():
    sysnum1 = random.randint(0,9)
    sysnum2 = random.randint(0,9)
    sysnum3 = random.randint(0,9)
    usernum1 = int(input('First Number [0-9]: '))
    usernum2 = int(input('Second Number [0-9]:'))
    usernum3 = int(input('Third Number[0-9]: '))
    usernumbers = (usernum1, usernum2, usernum3)
    sysnumbers = (sysnum1, sysnum2, sysnum3)
    userinput = sorted(usernumbers)
    sysgenerated = sorted(sysnumbers)
    while userinput != sysgenerated:
        print('You loss. Better luck next time.')
        user_opt2 = input('Try again? [y/n]: ')
        if user_opt2 == 'y':
            Lottery()
        else:
            print('Thanks for trying your luck. Better luck next time')
            exit()
    prize()

def prize():
    print('Winnner, Congratulations.')

startup()