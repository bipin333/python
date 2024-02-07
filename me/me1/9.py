"""
Write a program to guess a number. generate a random number between, 
lets say, 0 and 100. The player then needs to guess what that number is. 
The program should respond by telling them their guess is either too low or too high. 
When the user guesses right, your program should ask them if they want to play again. 
Limit the number of guesses to 5, for example.
"""
import random;
while True:
    choice = 'n'
    attempt = 0
    rand_num = random.randint(0,100)
    while attempt < 5:
        guess = int(input('Guess : '))
        attempt += 1
        if guess == rand_num:
            print('Congratulation you got it at',attempt,'attempt')
            choice = input('Do you want to play again [y/n] : ')
            if choice == 'y':
                break
        elif guess < rand_num:
            print('too low')
        elif guess > rand_num:
            print('too high')
    if choice != 'y':
        break