import string
import random

def load_words():
    file = open("words.txt")
    text = file.read()
    word_list = text.split()
    lowercase_words = []
    for word in word_list:
        lowercase_words.append(word.lower())
    # print(lowercase_words[:50])
    return word_list
load_words()

word_list = load_words()

def choose_word(wordList):
    return random.choice(word_list)
    print(random.choice(word_list[:]))

def word_guessed(myst_word, letters_guessed):
    
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
