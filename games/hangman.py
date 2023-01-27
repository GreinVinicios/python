import requests
import random
from urllib.request import Request, urlopen


def play():
    print("*********************************")
    print("***Welcome to the Hangman game!***")
    print("*********************************")

    url = "https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    words = web_byte.decode('utf-8').splitlines()
    word_index = random.randrange(1, 10001)
    secret_word = words[word_index].lower()

    correct_letters = []
    typed_letters = []

    for i in secret_word:
        correct_letters.append("_")

    print("The secret word have {} characters".format(len(secret_word)))
    print(" ".join(correct_letters))

    hanged = False
    guessed = False
    errors = 0
    number_of_tries = 0

    while not hanged and not guessed:
        guess = input("Type a letter: ").lower().strip()

        if guess in typed_letters:
            print("This letter has already been typed, try another one")
        else:
            if guess in secret_word:
                index = 0
                for letter in secret_word:
                    if guess == letter:
                        correct_letters[index] = letter
                    index += 1
            else:
                errors += 1

        typed_letters.append(guess)
        number_of_tries += 1

        hanged = errors == 10
        guessed = "_" not in correct_letters

        print(correct_letters)
        print("Typed letters: " + str(typed_letters).strip('[]'))

        print("Playing...")

    if guessed:
        print("You win")
    else:
        print("You loose")

    print(f"The secret word was {secret_word}")
    print("Game over")


if __name__ == "__main__":
    play()
