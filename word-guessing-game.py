# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 23:38:10 2021

@author: HgCNO2

Reference for idea https://www.reddit.com/r/learnpython/comments/mdd5sj/pls_help_noob_with_very_basic_question/
"""
import random

candidate_words = ['frog', 'dog', 'fish', 'sailor', 'alligator', 'tail']
game_words = random.sample(candidate_words, k=4)
game_words.insert(0, '')
winning_word = random.sample(game_words[1:], k=1)
guesses = 1
guess = ''

def game_rules():
    global guess
    print('The winning word is one of these:\n1: ' + game_words[1] + '\n2: ' + game_words[2] + '\n3: ' + game_words[3] + '\n4: ' + game_words[4])
        
    guess = input('Choose a number to make guess number ' + str(guesses) + '.\n')
    
    print('You have chosen \'' + game_words[int(guess)] + '\'')
    return guess

def word_guessing_game():
    game_rules()
    global guesses
    while guesses < 5:    
        if game_words[int(guess)] == winning_word[0]:
            print('You guessed correctly in ' + str(guesses) + ' guesses!')
            break
        else:
            guesses += 1
            for i in range(len(game_words[int(guess)])):
                print(game_words[int(guess)][i])
            print('\nTry again! Only ' + str(5 - int(guesses)) + ' guesses remain.\n\n-------\n')
            game_rules()

word_guessing_game()