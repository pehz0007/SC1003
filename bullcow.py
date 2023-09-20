import random as r


def get_digits(digits_allowed, width):
    return r.sample(digits_allowed, width)


def check_guess(guessList, answerList):
    bulls = 0
    cows = 0

    for i in range(len(guessList)):
        for j in range(len(answerList)):
            if guessList[i] == answerList[j]:
                if i == j:
                    bulls += 1
                else:
                    cows += 1

    return (bulls, cows)


digits_allowed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
width = 4

attempts = 0
answerList = get_digits(digits_allowed, width)
# print(answerList)
while True:
    attempts += 1
    guessList = [int(i) for i in list(input("Please input 4 digits: "))]

    bulls, cows = check_guess(guessList, answerList)
    print("{} A (Bulls) {} B (Cows)".format(bulls, cows))
    if bulls == width:
        print("You Win !!")
        print("Attempts: {}".format(attempts))
        break
