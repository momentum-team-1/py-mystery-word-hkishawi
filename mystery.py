import string
import random

# def display_word(word, guesses):
#     letters = []
#     for letter in word:
#         letters.append(display_letter(letter, guesses))

#     user_display = " ".join(letters)
#     return user.display.upper()


def random_word():
    file = open("words.txt")
    text = file.read()
    words = text.split()
    lowercase_words = []
    for word in words:
        lowercase_words.append(word.lower())
    print(random.choice(lowercase_words[:]))



word = "dinosaur"
current_guesses = []
def display_letter(letter, guesses): 
    if letter in guesses:
        return letter
    else: 
        return "_"
output = []
for letter in word: 
    output.append(display_letter(letter, current_guesses))
print(output)

random_word()

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
