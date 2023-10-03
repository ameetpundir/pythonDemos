from ast import Num
import random


def guessN(x):
    random_number = random.randint(1, x)
    guessN = 0
    while guessN != random_number:
        guessN = int(input("Guess the number : "))
        if guessN < random_number:
            print("guess too small")
        elif guessN > random_number:
            print("guess too big")
    print(f"correct number found : {random_number}")


def computer_guess(x):
    random_number = random.randint(1, x)
    higherLimit = x
    lowerLimit = 1
    computerGuess = random.randint(lowerLimit, higherLimit)

    while computerGuess != random_number:
        if computerGuess < random_number:
            lowerLimit = computerGuess + 1

            # print(f"lowerLimit is {lowerLimit}")
            print(f"computerGuess {computerGuess} is lower")
        elif computerGuess > random_number:
            print(f"computerGuess {computerGuess} is higher")

            higherLimit = computerGuess - 1
            # print(f"higherLimit is {higherLimit}")
        computerGuess = random.randint(lowerLimit, higherLimit)

    print(f"correct number found : {random_number}")


computer_guess(20)
