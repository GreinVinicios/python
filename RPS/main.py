import random

loose = "The computer wins"
win = "You win"
user_lives = 5
computer_lives = 7
score = 0
drew = 0
rps = ""
level = ""

while True:
    print("Welcome to Rock, Paper and Scissors game")
    print("Please select the difficult level:")
    print("Easy - you have 10 lives and computer 3")
    print("Medium - you have 5 lives and computer 5")
    print("Hard - you have 3 lives and computer 7")

    while level not in ("1", "2", "3"):
        level = input("(1) Easy, (2) Medium, (3) Hard: ")

    if level == "1":
        user_lives = 10
        computer_lives = 3
    elif level == "2":
        user_lives = 5
        computer_lives = 5
    elif level == "3":
        user_lives = 3
        computer_lives = 7

    level = ""

    print("Rules:")
    print("You have "+str(user_lives)+" lives")
    print("Every time you win, you won a extra live")
    print("Every time you loose, you loose 1 live")
    print("Computer have "+str(computer_lives)+" lives.")
    print("To win you need to choose the correct hand")
    print("Rock win against scissors but loose against paper")
    print("Paper win against rock but loose against scissors")
    print("Scissors win against paper but loose against rock")
    print("")

    while user_lives > 0 and computer_lives > 0 and rps != "exit":
        while rps != "r" and rps != "p" and rps != "s" and rps != "x" and \
                rps != "rock" and rps != "paper" and rps != "scissors" and rps != "exit":
            rps = input("(R)Rock, (P)Paper, (S)Scissors or (x)Exit? ").lower()

        if rps == "r":
            rps = "rock"
        if rps == "p":
            rps = "paper"
        if rps == "s":
            rps = "scissors"
        if rps == "x":
            rps = "exit"
            continue

        computer = ("rock", "paper", "scissors")
        computer = random.choice(computer)
        print("The computer chose ", computer)

        if rps == computer:
            print("You drew")
            drew += 1
        elif rps == "rock":
            if computer == "paper":
                print(loose)
                user_lives -= 1
            elif computer == "scissors":
                print(win)
                score += 1
                computer_lives -= 1
        elif rps == "paper":
            if computer == "scissors":
                print(loose)
                user_lives -= 1
            elif computer == "rock":
                print(win)
                score += 1
                computer_lives -= 1
        elif rps == "scissors":
            if computer == "rock":
                print(loose)
                user_lives -= 1
            elif computer == "paper":
                print(win)
                score += 1
                computer_lives -= 1

        print("You have "+str(user_lives)+" lives remaining")
        print("The computer have " + str(computer_lives) + " lives remaining")
        rps = ""

    rps = ""
    print("")
    print("")
    print("")
    print("Thanks for playing")
    print("You won ", score, "score")
    print("You drew ", drew, "score")
    print("")
    print("")
