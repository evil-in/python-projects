#A guess the number game

import random

#Introduction
print('Hi!, what is your name?')
name = input()
print('Alright', name, 'let\'s play a guess the number game.')
print('I\'m going to think of a number and you guess it.')
n = random.randint(1,20)
print('Okay, I\'m thinking of a number between', n-6, 'and', n+6)

#Function to check the guesses
def guesses(num):
    if num == n:
        print('Congratulations, you got it!')
    elif num>n:
        print('No, your guess is too high')
    elif num<n:
        print('No, your guess is too low')


for i in range(0,6): #for loop to call the check the guess function
    print('Take your guess')
    guess_num = int(input())
    guesses(guess_num)
    if guess_num == n:
        print('You got it in', str(i), 'guesses')
        break        
    elif i == 4:
        print('Last chance!', end = '')
    elif i == 5:
        print('Nope, the number was actually',n,'. Better luck next time.')
    else:
        continue



