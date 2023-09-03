# Print Menu
print("Please select one of the following quizzes:")
print("\t1. Number guessing")
print("\t2. Calculate sum")

choice = int(input())

passed = False

import random as r
if choice == 1:
    # Guessing game
    ended = False
    trials = 0
    number = r.randrange(1, 9)
    print(number)
    while not ended:
        trials += 1
        guess = int(input("Enter an integer from 1 to 9:"))
        if trials > 3:
            print("Sorry, you exceed the trial limit. Failed.")
            break
        if guess > number:
            print("guess is high")
        elif guess < number:
            print("guess is low")
        else:
            ended = True
            passed = True
            print("Congratulations. You guessed it by {} trials!".format(trials))
            break
elif choice == 2:
    # Calculate sum of 5 integers
    number = r.randrange(55, 66)
    print("Please calculate the sum of 5 integers start from {}".format(number))
    sum_of_5_integers = 5 * number + 10
    print(sum_of_5_integers)
    answer = int(input("Please enter your answer: "))
    if answer == sum_of_5_integers:
        passed = True
    else:
        print("Sorry, wrong answer. Failed")

if passed:
    print("You can start the game now.")
