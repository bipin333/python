"""
Write a Python program to implement Word Guessing Game: 
The computer selects a word and displays its length as underscores. 
The player guesses letters to reveal the word, with limited attempts.
"""
import random
dictionary = ('nepal','china','india','finland','pakistan','korea','japan','usa','england')
randomWord = random.choice(dictionary)
foundWord = []
incorrectAttempt = 3
while True:
    letter = ''
    for i in randomWord:
        if i in foundWord:
            print(i,end='')
        else:
            print('_',end='')
    print('')
    while len(letter)!=1:
        letter = input('enter possible letter : ')
    if letter in randomWord and letter not in foundWord:
        foundWord.append(letter)
    else:
        incorrectAttempt -= 1
        print('Letter Not Found\nRemaining Attempts =',incorrectAttempt)
    if len(foundWord) == len(randomWord):
        print('Congratulation You Got It All')
        break
    elif incorrectAttempt == 0:
        print('Your Incorrect Limit Reached')
        break
    print('')