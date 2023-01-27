import random


def play():
    print("*********************************")
    print("Welcome to the guessing game!")
    print("*********************************")

    secret_number = random.randrange(1, 101)
    total_of_tries = 0
    points = 1000

    print("Select the difficult level")
    print("(1) Easy (2) Medium (3) hard")

    level = int(input("Select the level: "))

    if level == 1:
        total_of_tries = 20
    elif level == 2:
        total_of_tries = 10
    else:
        total_of_tries = 5

    for round_number in range(1, total_of_tries + 1):
        print("Try {} of {}".format(round_number, total_of_tries))

        chute_str = input("Type a number between 1 and 100: ")
        print("You typed ", chute_str)
        guess = int(chute_str)

        if guess < 1 or guess > 100:
            print("You must type a number between 1 and 100!")
            continue

        guessed = guess == secret_number
        bigger = guess > secret_number
        smaller = guess < secret_number

        if guessed:
            print("You guessed and won {} points!".format(points))
            break
        else:
            if bigger:
                print("You fail! Try a smaller number.")
            elif smaller:
                print("You fail! Try a bigger number.")
            lost_points = abs(secret_number - guess)
            points = points - lost_points

    print("Game over")


if __name__ == "__main__":
    play()
