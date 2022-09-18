import math


def validate_input(secret_number):
    try:
        secret_number = int(secret_number)
        return secret_number, True
    except Exception as e:
        print("Oops, an error occurred while reading your entry. Are you sure you entered a number?")
        print(e.__class__)
        return None, False


def number_is_close(chute, secret_number):
    if 0 <= chute - secret_number <= 5 or 0 <= secret_number - chute <= 5:
        return True
    else:
        return False
