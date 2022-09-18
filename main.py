import random
import functions

entry_is_number = False
while not entry_is_number:
    secret_number = input("Enter the secret number or R to generate a random secret number between 0 and 100:\n")
    if secret_number == "R" or secret_number == "r":
        secret_number = random.randint(0, 100)
        break
    else:
        secret_number, entry_is_number = functions.validate_input(secret_number)

is_correct_number = False
message_missed_by_little = "You're almost there! Your number is {} than the secret number \n"
message_missed = "Oh no! You missed! Your number is {} than the secret number\n"
print("It's time to guess!\nYou have 5 attempts.")
print("-"*20)
counter = 0

while counter < 5 and not is_correct_number:
    chute = input("Enter a number to guess:\n")
    chute, is_valid_number = functions.validate_input(chute)
    if not is_valid_number:
        print("Try again!")
        continue

    is_correct_number = chute == secret_number
    if is_correct_number:
        print("Congratulations! You discovered the number!")
    else:
        counter += 1
        if chute > secret_number:
            if functions.number_is_close(chute, secret_number):
                print(message_missed_by_little.format("bigger"))
            else:
                print(message_missed.format("bigger"))
        else:
            if functions.number_is_close(chute, secret_number):
                print(message_missed_by_little.format("smaller"))
            else:
                print(message_missed.format("smaller"))

        print("Attempt {} of 5".format(counter))

if counter >= 5 and not is_correct_number:
    print("The secret number is {}".format(secret_number))

