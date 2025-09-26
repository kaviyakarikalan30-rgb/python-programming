import random

secret_number = random.randint(1, 100)  # Use random.randint for a secret number
attempts = 3
while attempts > 0:
    enter_input = int(input("enter the number: "))
    # enter_secret_number
    if enter_input == secret_number:
        print("secret number is low. access generated")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"low value.{attempts} attempts(s) left.")
        else:
            print("high value. too many wrong attempts")