import random


def rps():
    # r rock, p paper, s scissor
    computerPick = random.choice(["r", "p", "s"])
    print(computerPick)

    myChoice = input("r/p/s : ").lower()
    print(myChoice)

    # p > r, s > p, r > s
    def whoWins(x, y):
        if x == y:
            return f"user value {x} and computer value {y} tied"
        elif (
            (x == "p" and y == "r")
            or (x == "s" and y == "p")
            or (x == "r" and y == "s")
        ):
            return f"user won with value {x} over computer value {y}"

        return f"computer won with value {y} over user value {x}"

    msg = whoWins(myChoice, computerPick)
    print(msg)


rps()
