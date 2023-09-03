
registered_users = {
    'Test': 'Test12345',
    'Jack': 'Test12345',
    'Tom': 'Password1'
}

def contains_special(text):
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
    if not check_user_exists(username):
        print("User does not exists!")
    elif registered_users[username] != password:
        new_password = input("Wrong password, input again: ")
        password_is_correct(username, new_password)
    else:
        print("Welcome back, {}, You can start the game".format(username))


# Menu

print("Please select one of the  following options:")
print("\t1. User Registration")
print("\t2. User Login")

choice = int(input())

if choice == 1:
    print("User registration:")
    username = None
    password = None
    username_verify = False
    password_verify = False

    while not username_verify:
        username = input("Input your user name: ")
        if check_user_exists(username):
            print("The user exists. Please choose another user name.")
        else:
            username_verify = True

    while not password_verify:
        print("Input your password:")
        password = input()
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
            password_verify = True
            registered_users[username] = password
            print("Your password is strong enough. User registered.")

    print("The users in system")
    print(registered_users)
elif choice == 2:
    username = input("Input user name: ")
    password = input("Input password: ")
    password_is_correct(username, password)
