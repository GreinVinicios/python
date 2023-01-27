import hangman
import guessing


def select_game():
    print("*********************************")
    print("*******Choose your game!*******")
    print("*********************************")

    print("(1) Hangman (2) Guessing")

    game = int(input("Which game? "))

    if game == 1:
        print("Playing hangman")
        hangman.play()
    elif game == 2:
        print("Playing guessing")
        guessing.play()


if __name__ == "__main__":
    select_game()
