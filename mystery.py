#"_" stop appearing after first turn. need to set up levels

import string
import random
random.random()

def load_words():
    file = open("words.txt")
    text = file.read()
    word_list = text.split()
    lowercase_words = []
    for word in word_list:
        lowercase_words.append(word.lower())
    # print(random.choice(lowercase_words[:]))
    return (lowercase_words)
    # return (lowercase_words)

#filter out easy words to use in level 1
def easy_words():
    easy_word_list = []
    for word in load_words():
        if len(word) >= 2 and len(word) <= 6:
            easy_word_list.append(word)
            print(random.choice(easy_word_list[:]))
    return random.choice(easy_word_list)
 

def hard_words():
    hard_word_list = []
    for word in load_words():
        if len(word) >= 7:
            hard_word_list.append(word)
            print(random.choice(hard_word_list[:]))
    return random.choice(hard_word_list)

def choose_level():
    level = input("choose difficulty: (e)asy or (h)ard")
    level = level.lower()
    if level == 'e':
        answer = random.choice(easy_words())
    elif level == 'h':
        answer = random.choice(hard_words())
    return answer
choose_level()

# def choose_level(prompt, options):
#     while True: 
#         try: 
#             str__input = input(prompt)
#             if str_input not in options: 
#                 raise ValueError
#             return_input
#             except ValueError: 
#                 print("input invalid")
# input_option("choose a level: (e)asy or (h)ard?", ["e", "h"]) 

def myst_word_game():
   #store data here 
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = choose_level()
    letters_guessed = []
    tries = 5
    guessed = False #this tells machine that game has not ended until words are solved or out of tries in status 
    # for word in word_list:

    level = choose_level()
    if level == 'e':
        word = easy_words()
    elif level == 'h': 
        word = hard_words()
    
    print("the word contains", len(word), 'letters.')
    print(len(word) * " _ ") #the length of the word will be rep by _
    while guessed == False and tries > 0: #while word is not guessed and player is not out of tries then:
        print('u have' + str(tries) + 'tries')
        guess = input('please enter 1 letter or the full word: ').lower() #input of what the player inputs which is made into lowercase
    #player could guess correct letter, guess word, not input anything, input non-alphabet, input wrong letter
        if len(guess) == 1: #if length of players guess is 1 char
            if guess not in alphabet: 
                print('enter a letter!')
                print('guessed letters: ', letters_guessed)
            elif guess in letters_guessed: #if 
                print('u already used that letter!')
                print('guessed letters: ', letters_guessed)
            elif guess not in word: #guess that's not in word will count as guessed letter and player loses a try
                print('that letter is incorrect')
                print('guessed letters: ', letters_guessed)
                letters_guessed.append(guess)
                tries -= 1
            elif guess in word: #if guess is in the word "the letter guessed is added to letters guessed" UNDERSCORE NEEDS TO UPDATE SOMEHOW!
                print ('letter is in word')
                letters_guessed.append(guess)
                print('guessed letters: ', letters_guessed)
            else: 
                print('placeholder')
        elif len(guess) == len(word): #if lenth of guess = word 
            if guess == word: #and if the guess is in fact the word
                print('word guessed!')
                guessed = True
                print('guessed letters: ', letters_guessed)
            else: #otherwise 
                print('incorrect word!')
                tries -= 1
                print('guessed letters: ', letters_guessed)
        else: #otherwise player entered word that is too long 
            print('incorrect word length')
            tries -= 1
            print('guessed letters: ', letters_guessed)

#This answers the problem to updating the underscore
        game_status = '' #where status will be updated 
        if guessed == False: #if guessed letters is not complete game will be ongoing 
            for letter in word: 
                if letter in letters_guessed: 
                    game_status += letter #this updates the status plus the letter
                else: 
                    game_status += ' _ ' #this will keep the unsolved letters  as"_"
            print(game_status)
        if game_status == word: #however if the word is solved then:
            print ('u win!')
            guessed = True #this ends the game and says the word is solved
        elif tries == 0: #player runs out of turns 
            print('ur out of tries. u lose.')
myst_word_game()


def main():
    answer = choose_level()
    return myst_word_game()

if __name__ == '__main__':
    myst_word_game()

# word_list = load_words()

# def choose_word(wordList):
#     return random.choice(word_list)
#     print(random.choice(word_list[:]))

# def word_guessed(myst_word, letters_guessed):

# def random_word(word_list):
#     file = open("words.txt")
#     text = file.read()
#     words = text.split()
#     lowercase_words = []
#     for word in words:
#         lowercase_words.append(word.lower())
#     print(random.choice(lowercase_words[:]))

# """trying to get random word """
# def random_word(word_list):
#     file = open("words.txt")
#     text = file.read()
#     words = text.split()
#     lowercase_words = []
#     for word in words:
#         lowercase_words.append(word.lower())
#     word_list = lowercase_words
#     return word_list[random.randint(0, len(word_list))].lower()
#     print(random.choice(word_list[:]))
# random_word()

# def level_one(word_list):
# #spits words from random_word that's 2-5 characters long
#     level_one_words = []
#     for word in word_list:
#         if len(word) >= 2 and len(word) <= 5:
#             level_one_words.append(word) 
#     return level_one_words

# def show_guessed(guessed_letters):
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     for char in guessed_letters:
#         if char in letters:
#             letters.append(char)
    
#     print('\n')
#     if len(letters) > 0: 
#         print('guessed letter:     {}'.format(' '.join(sorted(vowels)).lower()))


# def display_word(myst_word, guessed_letters):
# #we want a string to return a guessed letter or a _. 
#     display = []
#     for char in myst_word:
#         if char in gussed_letters:
#             display.append(char.lower())
#         else:
#             display.append('_')
#     return ' '.join(display)

# def display_word(word, guesses):
#     letters = []
#     for letter in word:
#         letters.append(display_letter(letter, guesses))

#     user_display = " ".join(letters)
#     return user.display.upper()

# word = "dinosaur"
# current_guesses = []
# def display_letter(letter, guesses): 
#     if letter in guesses:
#         return letter
#     else: 
#         return "_"
# output = []
# for letter in word: 
#     output.append(display_letter(letter, current_guesses))
# print(output)

# random_word()

# def display_word(word, guesses): 
#     letters = []
#     for letter in word:
#         letter.append(display_letter(letter,guesses))
#     print(letters)
#     return letters

# def print_word(word, guesses):
#     output_letters = [display_letter(letter, guesses) for letter in word]
#     print(" ".join(output_letters))
# print_word(word, guesses)

# create a level (e) with lenth of random word >2 <5
# 
# if __name__ == "__main__":
#     print(get_random_word(min_length = 24))
