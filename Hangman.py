from itertools import count
import time
import os
import random
from threading import Thread
from threading import Timer
import sys

clear = lambda: os.system('cls')

def timer():
    global time_count
    global stop_time
    stop_time = False
    for i in range(time_count):
        time.sleep(1)
        time_count -= 1

    if (stop_time == False):
        print("\nTime's up!")
        os._exit(1)

#### Introduction ###

start_game = True

while start_game: 
    country_list = ['Brazil', 'Cambodia', 'Philippines', 'Yemen', 'China', 'France', 'Indonesia', 'Japan', 'Mexico', 'Singapore']
    fruit_list = ['Guava', 'Apple', 'Banana', 'Dragonfruit', 'Orange', 'Kiwi', 'Cherry', 'Blackberry', 'Date', 'Jackfruit']
    planet_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    topic_list = {'1':'Countries', '2':'Fruits', '3':'Planets'}
    clear()
    print('******************************')
    print('*                            *')
    print('*          HANGMAN           *')
    print('*                            *')
    print('******************************')
    print('\nSelect your topic:\n')
    print('1. Countries')
    print('2. Fruits')
    print('3. Planets\n')

    start = False

    while start == False:
        topic = input('Enter the number: ')
        if topic in topic_list.keys():
            start = True
        else:
            print('Wrong entry. Please try again')

    print("\nOk let's start!")
    time.sleep(3)

    ### Game ###

    guessed_answer = False
    guessed_letters = []

    correct_word = ''
    if (topic == '1'):
        correct_word = random.choice(country_list)
    elif (topic == '2'):
        correct_word = random.choice(fruit_list)
    elif (topic == '3'):
        correct_word = random.choice(planet_list)

    hangman_word = "_ " * len(correct_word)
    word_count = len(hangman_word)
    spaces_to_add = (40 - word_count) // 2
    display_word = (' ' * spaces_to_add) + hangman_word + (' ' * spaces_to_add)

    lives = 5
    print_message = ''

    #countdown_thread = threading.Thread(target = countdown)
    #countdown_thread.start()
    t1 = Thread(target=timer)
    time_count = 30
    stop_time = False
    t1.start()
    
    while guessed_answer == False and lives > 0 and time_count > 0:
        clear()
        hangman_word_list = list(hangman_word)
        for guesses in guessed_letters:
            indices = [i for i, letter in enumerate(correct_word) if letter.upper() == guesses.upper()]
            for index in indices:
                hangman_word_list[(index * 2)] = guesses
        hangman_word = "".join(hangman_word_list)
        display_word = (' ' * spaces_to_add) + hangman_word + (' ' * spaces_to_add)
        print('****************************************')
        print('|                                      |')
        print(display_word)
        print('|                                      |')
        print('****************************************')
        print('Lives:', lives, '\t\t\tTimer:', time_count)
        print('\n')
        print(print_message)

        if "_" not in hangman_word:
            guessed_answer = True
            print_message = 'Congratulations! You guessed the word!'
            break

        # timeout = 5
        # t = Timer(timeout, print, ["Time's up"])
        # t.start()
        # t.cancel()

        guess = input('Enter letter or word: ').upper()
        if guess.isalpha():
            if len(guess) == 1:
                if guess in correct_word.upper():
                    guessed_letters.append(guess)
                    print_message = str(guess) + ' is in the word.'
                else:
                    lives -= 1
                    print_message = str(guess) + ' is not in the word.'
            else:
                if guess == correct_word.upper():
                    guessed_answer = True
                    print_message = 'Congratulations! You guessed the word!'
                else:
                    lives -= 1
                    print_message = 'Incorrect word.'
        else:
            print_message = 'Not a valid letter or word.'

        if lives == 0:
            print_message = "Game over! Correct answer is " + correct_word
    
    stop_time = True
    print(print_message)
    end_question = True
    while end_question:
        end_game = input('Would you like to play again (Y/N)? ')
        if (end_game.lower() == 'n' or end_game.lower() == 'y'):
            if (end_game.lower() == 'n'):
                start_game = False
                break
            end_question = False

    ### TODO: TIMER