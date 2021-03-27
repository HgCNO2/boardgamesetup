# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 23:38:10 2021

@author: HgCNO2

Reference for idea https://www.reddit.com/r/learnpython/comments/mdd5sj/pls_help_noob_with_very_basic_question/

candidate words are the top 100 boys names of 2020
"""
import random

candidate_words = ['Oliver', 'Liam', 'Ethan', 'Aiden', 'Gabriel', 'Caleb', 'Theodore', 'Declan', 'Owen', 'Elijah', 'Henry', 'Jackson', 'Grayson', 'Levi', 'Benjamin', 'Finn', 'Miles', 'Alexander', 'Sebastian', 'Leo', 'Landon', 'Emmett', 'Everett', 'Milo', 'Jasper', 'Archer', 'Lucas', 'Noah', 'Harrison', 'Hudson', 'Felix', 'Elliott', 'Jacob', 'Atticus', 'Lincoln', 'Gavin', 'Dominic', 'Jack', 'Atlas', 'Isaac', 'Logan', 'Wyatt', 'Silas', 'Cole', 'Theo', 'Holden', 'Luke', 'William', 'Isaiah', 'Adrian', 'Elias', 'Samuel', 'Arthur', 'Gideon', 'Kaden', 'Arlo', 'James', 'Adam', 'Colton', 'Ronan', 'Roman', 'Asher', 'Nolan', 'Jonah', 'Rhys', 'Nathan', 'Axel', 'August', 'Connor', 'Xavier', 'Charles', 'Eli', 'Daniel', 'Nathaniel', 'Ezra', 'Beau', 'Zachary', 'Tobias', 'Carter', 'Matthew', 'Ian', 'Ezekiel', 'Aaron', 'Thomas', 'Xander', 'Soren', 'Oscar', 'Callum', 'Nicholas', 'Ace', 'Josiah', 'Michael', 'Vincent', 'Edward', 'Lachlan', 'Chase', 'Apollo', 'David', 'Jace', 'Malachi']
game_words = random.sample(candidate_words, k=4)
game_words.insert(0, '')
winning_word = random.sample(game_words[1:], k=1)
guesses = 1
guess = ''
correct_letters = 0

def game_rules():
    global guess
    print('The winning word is one of these:\n1: ' + game_words[1] + '\n2: ' + game_words[2] + '\n3: ' + game_words[3] + '\n4: ' + game_words[4])
    guess = input('Choose a number to make guess number ' + str(guesses) + '.\n')
    print('You have chosen \'' + game_words[int(guess)] + '\'')
    return guess

def word_guessing_game():
    game_rules()
    global guesses, correct_letters
    while guesses < 5:
        correct_letters = 0
        if game_words[int(guess)] == winning_word[0]:
            print('===============\nYou guessed correctly in ' + str(guesses) + ' guesses!\n===============')
            break
        elif guesses != 4:
            guesses += 1
            if len(winning_word[0]) <= len(game_words[int(guess)]):
                for i in range(len(winning_word[0])):
                    if game_words[int(guess)][i] == winning_word[0][i]:
                        correct_letters += 1
            else:
                for i in range(len(game_words[int(guess)])):
                    if game_words[int(guess)][i] == winning_word[0][i]:
                        correct_letters += 1
            print('\nYour guess has ' + str(correct_letters) + ' letters correct.')
            print('\nTry again! Only ' + str(5 - int(guesses)) + ' guesses remain.\n\n-------\n')
            game_rules()
        else:
            guesses += 1
            print('\nYou are out of guesses. The correct word was \'' + winning_word[0] + '\'.')

word_guessing_game()
input('Thanks for playing!\nHit enter to quit.')