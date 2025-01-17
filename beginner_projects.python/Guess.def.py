import random


def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("I have selected a number between 1 and 100. Try to guess it!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break


number_guessing_game()