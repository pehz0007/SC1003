registered_users = {
    'Test': 'Test12345',
    'Jack': 'Test12345',
    'Tom': 'Password1'
}


def contains_special(text):
    """
    Check if the text contains any special characters
    :param text:
    :return: True if the text contains at least one special character(s)
    """
    valid_symbols = "!@#$%^&*()_-+={}[]"
    for i in range(len(text)):
        if text[i] in valid_symbols:
            return True
    return False


def check_user_exists(username):
    """
    Check if the username is registered in the :registered_users:
    :param username:
    :return: True if the username exists in the dict
    """
    return username in registered_users.keys()


def contains_upper(text):
    """
    Check if the text contains any upper character(s)
    :param text:
    :return: True if text have at least one upper character(s)
    """
    for i in range(len(text)):
        if text[i].isupper():
            return True
    return False


def contains_lower(text):
    """
    Check if the text contains any lower character(s)
    :param text:
    :return: True if text have at least one lower character(s)
    """
    for i in range(len(text)):
        if text[i].islower():
            return True
    return False


def contains_digit(text):
    """
    Check if the text contains any digit(s)
    :param text:
    :return: True if text have at least one lower digit(s)
    """
    for i in range(len(text)):
        if text[i].isdigit():
            return True
    return False


def password_is_correct(username, password):
    """
    Check that the password for the user is correct
    :param username: The username of the user.
    :param password: The password to be checked.
    """
    if not check_user_exists(username):
        print("User does not exists!")
    elif registered_users[username] != password:
        new_password = input("Wrong password, input again: ")
        password_is_correct(username, new_password)
    else:
        print("Welcome back, {}, You can start the game".format(username))


def is_password_strong(password):
    """
    Check if a password meets the criteria for a strong password.

    :param password: The password to be checked.
    :return: True if the password is strong, False otherwise.
    """
    password_is_strong = False
    if len(password) < 8:
        print("Your password need at least 8 letters")
    elif not contains_upper(password):
        print("Your password need at least 1 upper case letter")
    elif not contains_lower(password):
        print("Your password need at least 1 lower case letter")
    elif not contains_digit(password):
        print("Your password need at least 1 digit")
    elif not contains_special(password):
        print("Your password need at least 1 special letter")
    else:
        password_is_strong = True
        print("Your password is strong enough. User registered.")
    return password_is_strong


def get_new_username():
    """
    Prompt the user to input a new username and check if it already exists.

    This function continuously prompts the user to input a new username until a unique one is provided.

    :return: A unique username entered by the user.
    """
    while True:
        username = input("Input your user name: ")
        if check_user_exists(username):
            print("The user exists. Please choose another user name.")
        else:
            return username


def get_new_strong_password():
    """
    Prompt the user to input a new strong password.

    This function continuously prompts the user to input a new password until a strong one is provided,
    according to the criteria specified in the is_password_strong function.

    :return: A strong password entered by the user.
    """
    while True:
        print("Input your password:")
        password = input()
        if is_password_strong(password):
            return password


def user_register(username, password):
    """
    Register a new user with the provided username and password.

    :param username: The username of the new user.
    :param password: The password of the new user.
    """
    registered_users[username] = password


def user_registration():
    """
    Perform user registration.

    This function prompts the user to input a new username and a strong password and registers the user.

    """
    print("User registration:")

    username = get_new_username()
    password = get_new_strong_password()
    user_register(username, password)

    print("The users in system")
    print(registered_users)


def user_login():
    """
    Perform user login.

    This function prompts the user to input their username and password, and it checks if the provided
    username and password are correct using the password_is_correct function.

    """
    username = input("Input user name: ")
    password = input("Input password: ")
    password_is_correct(username, password)


def print_menu():
    print("Please select one of the  following options:")
    print("\t1. User Registration")
    print("\t2. User Login")


if __name__ == '__main__':
    print_menu()

    choice = int(input())

    if choice == 1:
        user_registration()
    elif choice == 2:
        user_login()
