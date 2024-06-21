import random
import string

from words import words

def get_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word =random.choice(words)

    return word

def hangman():
    word = get_word(words)
    word_letters = set(word)
    guessed_letters = set()
    alphabet = set(string.ascii_lowercase)
    incorrect = 0
    while len(word_letters) > 0:
        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            elif user_letter not in word_letters:
                print("The letter you chose was incorrect")
                incorrect += 1
        elif user_letter in guessed_letters:
            print("Letter has already been used")

        else:
            print("Invalid character")

        word_list =[letter if letter in guessed_letters else '-' for letter in word]
        print(' '.join(guessed_letters))

        print(word_list)
        if incorrect == 6:
            print("You are out of guesses")
            print(f"The correct answer is {word} ")
            break


hangman()