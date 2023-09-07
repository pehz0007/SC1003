from lab2 import guessing_game, sum_of_5_int_game
from lab3 import register_new_user, get_new_username, get_new_strong_password, user_login

def getUserChoice():
    choice = int(input('''Please select one of the following
    options:
    1. User registration
    2. User Login
    3. Play the game as a guest\n'''))
    return choice
def guestQuiz():
    quizChoice = chooseQuiz()
    isPass = takeQuiz(quizChoice)
    if isPass:
        print("Congratulations. You can start the game.")
def chooseQuiz():
    choice = int(input('''Dear Guest, you have to pass one quiz to
    play the game.
    Please select one of the following quizzes:
    1. Number guessing
    2. Calculate sum\n'''))
    return choice
def takeQuiz(choice):
    if choice == 1:
        isPass = guessing_game()
    elif choice == 2:
        isPass = sum_of_5_int_game()
    return isPass

def main():
    choice = getUserChoice()
    if choice == 1:
        register_new_user(get_new_username(), get_new_strong_password())
    elif choice == 2:
        user_login()
    elif choice == 3:
        guestQuiz()

main()