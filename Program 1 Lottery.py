# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random

# Steps
# 1. Ask the user if he/she wants to try his/her luck.
def startup():
    user_opt1 = input('Do you want to try your luck? [y/n]: ')
    if user_opt1 == 'y': # 'y' = yes, then it will run the function userfirstnumb(). 
        userfirstnumb()
    else: # The user answer is no.
        if user_opt1 == 'n':
            print('You just missed your chance to win a lot of money.')
            exit()

# 2. This function ask the user to input the first number.
def userfirstnumb():
    usernum1 = int(input('First Number [0-9]: '))
    while usernum1 < 0 or usernum1 > 9: # The user inputted a number that is less than 0 or greater than 9.
        print('Only pick number from 0 to 9.')
        userfirstnumb()
    # If the user inputted a number within the range from 0 to 9, it will run the function usersecondnumb together with the value of the fist number.
    usersecondnumb(usernum1)

# 3. This function ask the user to input the second number.
def usersecondnumb(usernum1):
    usernum2 = int(input('Second Number [0-9]: '))
    while usernum2 < 0 or usernum2 > 9: # Same comment like in the second step in the if statement.
        print('Only pick number from 0 to 9.')
        usersecondnumb(usernum1) 
    if usernum2 == usernum1: # The user inputted a number within the range 0 to 9 but the user already picked that number. We cannot picked a number with the same value in a lottery game. 
        print('You have already picked that number. Pick another number from 0 to 9.')
        usersecondnumb(usernum1)
    # The user entered a number between 0 and 9 and not the same value as the first number, the function userthirdnumb will be called along with the values of the first, second numbers.
    userthirdnumb(usernum1, usernum2)

# 4. This function ask the user to input the second number.
def userthirdnumb(usernum1, usernum2):
    usernum3 = int(input('Third Number [0-9]: '))
    while usernum3 < 0 or usernum3 > 9: # Same comment like in the second and third step in the first if statement.
        print('Only pick number from 0 to 9.')
        userthirdnumb(usernum1, usernum2)
    if usernum3 == usernum1 or usernum3 == usernum2: # Same comment like in the thirrd step in the second if statement.
        print('You have already picked that number. Pick another number from 0 to 9.')
        userthirdnumb(usernum1, usernum2)
    # Because the user entered a number between 0 and 9 and not the same value as the first and second number, the function sysfirstnumb will be called along with the variable that stores the three numbers inputted by the user.
    usernumbers = (usernum1, usernum2, usernum3)
    sysfirstnumb(usernumbers)

# 5. This function generate the first random number and the function syssecondnumb will be called along the three numbers inputted by the user.
def sysfirstnumb(usernumbers):
    sysnum1 = random.randint(0,9)
    syssecondnumb(usernumbers, sysnum1)

# 6. This function generate the second random number and the function systhirdnumb will be called along the three numbers inputted by the user and first random number.
def syssecondnumb(usernumbers, sysnum1):
    sysnum2 = random.randint(0,9)
    while sysnum2 == sysnum1: # If the value of sysnum2 (second random number) is the same as the value of sysnum1 (first random number), the function syssecondnumb will be called again until the second and first random numbers are not the same.
        syssecondnumb(usernumbers, sysnum1)
    systhirdnumb(usernumbers, sysnum1, sysnum2)

# 7. This function generate the third random number and the function Lottery will be called along the three numbers inputted by the user and three random numbers.
def systhirdnumb(usernumbers, sysnum1, sysnum2):
    sysnum3 = random.randint(0,9)
    while sysnum3 == sysnum1 or sysnum3 == sysnum2: # Same comment like in the six step in the while loop.
        systhirdnumb(usernumbers, sysnum1, sysnum2)
    sysnumbers = (sysnum1, sysnum2, sysnum3)
    Lottery(usernumbers, sysnumbers)

# 8. This function will run the lottery game and in this part we will know if the user win or loss. 
def Lottery(usernumbers, sysnumbers):
    userinput = sorted(usernumbers)
    sysgenerated = sorted(sysnumbers)
    while userinput != sysgenerated: # The three number picked by the user is incorrect, while if the three numbers that user picked matched the three random numbers it will now proceed to call the function prize.
        print('You loss. Better luck next time.')
        user_opt2 = input('Try again? [y/n]: ')
        if user_opt2 == 'y': # The user answer yes and he/she will try again.
            userfirstnumb()
        else: # The user answer is no.
            if user_opt2 == 'n':
                print('Thanks for trying your luck. Better luck next time')
                exit()
    prize()

# 9. This function will only called if you are a winner.
def prize():
    print('Winnner, Congratulations.')

startup()