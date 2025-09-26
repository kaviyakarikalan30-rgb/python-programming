import random

# Generate a random integer between 1 and 5
a = random.randint (1, 5)

print("Guess the value")
print("You have 3 attempts.")

# Loop for a fixed number of attempts (e.g., 3)
for attempt in range(3):
    try:
        b = int(input("Enter the value: "))
        
        # Check if the guess is correct
        if b == a:
            print("Value matched! ")
            # The game ends if the guess is correct
            break
        # Provide hints based on the guess
        elif b > a:
            print("Your value is greater. Try again.")
        elif b < a:
            print("Your value is lesser. Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# This else block is for the 'for' loop and only runs if the loop completes without a 'break'
else:
    print(f"You lost!  The correct value was {a}.")
