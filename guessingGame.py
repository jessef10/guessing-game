# This program will play a guessing game with the user. The user
# can guess the computers word one letter at a time until running
# out of attempts.
import sys, random

dictionary = ['age', 'art', 'axe', 'air', 'ant', 'bag', 'bat', 'bot', 'boy',
              'bug', 'bus', 'car', 'cat', 'day', 'dog', 'ear', 'eat', 'fog',
              'fox', 'gym', 'ice', 'jam', 'jar', 'kid', 'log', 'map' 'mug',
              'oil', 'pea', 'pen', 'pin', 'sky', 'tea', 'toy']
letters_wrong = []
letters_right = []
word = dictionary[random.randint(0, len(dictionary) - 1)] # picks word for the game
num_guesses = 0;


# Provides a description for how the game is played
def tutorial():
    print('To play, I think of a word and you guess one letter in my word.')
    print('Every time you guess wrong you get one less try and I draw some robots')
    print('to show you how you are doing. Once the figure is complete you loose :(')
    print('However if you guess all letters in my word you win :)')

# Prompts the user to start playing
def is_ready():
    user_input = ''
    while not user_input.isalpha():
        print('Would you like to play? (type YES or NO)')
        user_input = input()
    if user_input[0].upper() != 'Y':
        print('Okay maybe another time.')
        sys.exit()

# Shows a drawing to represent the users winning/loosing status
# parameter:
#    tries (int): number of attempts that were wrong
def figure(tries):
    print('your incorrect guessed letters: ' + ', '.join(letters_wrong))
    guesses_left = 5 - tries
    print(str(guesses_left) + ' tries left\n')

    all_upper = ''
    all_middle = ''
    all_lower = ''

    upper_robot = '+[O_O]+'
    middle_robot = '\[   ]/'
    lower_robot = '  | |   '
    bad_up_robot = ',[x_x],'
    bad_mid_robot = '/[   ]\\'
    bad_low_robot = '  | }   '
    for tri in range(tries):
        all_upper = all_upper + bad_up_robot + '  '
        all_middle = all_middle + bad_mid_robot + '  '
        all_lower = all_lower + bad_low_robot + ' '
    for left in range(guesses_left):
        all_upper = all_upper + upper_robot + '  '
        all_middle = all_middle + middle_robot + '  '
        all_lower = all_lower + lower_robot + ' '
    print(all_upper + '\n' + all_middle + '\n' + all_lower + '\n')

    game_words = ['_', '_', '_']
    index = 0
    for letter in word:
        if letter in letters_right:
            game_words[index] = letter + ' '
        index = index + 1
    print('my word: ' + str(' '.join(game_words)) + '\n')

# Exits game on word 'exit'
# parameter:
#    user_input (string): a word used for matching 'exit'
def check_for_exit(user_input):
    if user_input.upper() == 'EXIT':
        print('Goodbye +[~_~]+')
        sys.exit()

# Determnines wether a letter is in the chosens games word
# parameter:
#    letter (string): a single character in the alphabet
def check_guess(letter):
    if letter in word:
        print('Yes, ' + str(letter) + ' is there')
        global letters_right
        letters_right = letters_right + [letter]
    else:
        print('Sorry ' + str(letter) + ' is not in my word')
        global letters_wrong
        letters_wrong = letters_wrong + [letter]

    global num_guesses
    num_guesses = num_guesses + 1

# Determines wether the game is finished and shows game results (win/loss)
def check_game_won():
    if (len(letters_wrong) >= 5):
        print('Game over, you lost :(')
        stats()
        sys.exit()
    letter_count = 0
    for letter in letters_right:
        if letter in word:
            letter_count = letter_count + 1
    if letter_count == len(word):
        print('AWESOME! You won')
        stats()
        sys.exit()

# Shows game statistics
def stats():
    print('My word was ' + str(word))
    print('Here is how you did:')
    print(' number of guesses: ' + str(num_guesses))
    all_letters = letters_right + letters_wrong
    print(' your letters: ' + str(', '.join(sorted(all_letters))))

# Plays a game with the user
def play():
    print('Hi there, this is my Guessing Game.')
    is_ready()
    # knows rules
    print('Awesome! Do you know how to play? (type YES or NO)')
    user_input = input()
    while not user_input.isalpha():
        print('Ooops didn\'t get that')
        print('Do you know how to play? (type YES or NO)')
        user_input = input()
    if user_input[0].upper() != 'Y':
        tutorial()
        is_ready()

    print('\nIm thinking of a word with 3 letters')
    figure(num_guesses)
    while True:
        print('Guess a letter (type one letter, or EXIT)')
        letter = input()
        while len(letter) != 1 or not letter.isalpha():
            check_for_exit(letter)
            print(str(letter) + ' is not one letter')
            print('Try again (type one letter, or EXIT)')
            letter = input()
        check_guess(letter)
        figure(len(letters_wrong))
        check_game_won()

play()
