import random as r


def print_menu():
    print("Please select one of the following quizzes:")
    print("\t1. Number guessing")
    print("\t2. Calculate sum")


def guessing_game():
    """
    A number guessing game.

    The function generates a random number between 1 and 9 and prompts the user to guess it.
    The user has a limit of 3 trials to guess the number correctly.

    :return: True if the user wins the game, False if they fail to guess within 3 trials.
    """
    game_won = False
    trials = 0
    number_to_guess = r.randrange(1, 9)
    print(number_to_guess)
    while True:
        trials += 1
        guess = int(input("Enter an integer from 1 to 9:"))
        if trials > 3:
            print("Sorry, you exceed the trial limit. Failed.")
            break
        if guess > number_to_guess:
            print("guess is high")
        elif guess < number_to_guess:
            print("guess is low")
        else:
            game_won = True
            print("Congratulations. You guessed it by {} trials!".format(trials))
            break
    return game_won


def sum_of_5_int_game():
    """
    A game where the user needs to calculate the sum of 5 integers starting from a random number.

    The function generates a random number between 55 and 66 and calculates the sum of 5 integers
    starting from that number. It then asks the user to input their answer, and if the answer is correct,
    the user wins the game.

    :return: True if the user's answer is correct, False otherwise.
    """
    game_won = False
    number = r.randrange(55, 66)
    print("Please calculate the sum of 5 integers start from {}".format(number))
    sum_of_5_integers = 5 * number + 10
    print(sum_of_5_integers)
    answer = int(input("Please enter your answer: "))
    if answer == sum_of_5_integers:
        game_won = True
    else:
        print("Sorry, wrong answer. Failed")
    return game_won


if __name__ == '__main__':
    print_menu()
    choice = int(input())
    game_won = False
    if choice == 1:
        game_won = guessing_game()
    elif choice == 2:
        game_won = sum_of_5_int_game()

    if game_won:
        print("You can start the game now.")
