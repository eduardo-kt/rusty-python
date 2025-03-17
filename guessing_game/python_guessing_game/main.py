import random


def py_guessing_game():
    """A python guessing game."""
    secret_number = random.randint(1, 100)

    print("Guess the number!")

    while True:

        try:
            guess_number = int(input("Please input your guess: "))

            print(f"You guessed: {guess_number}")

            if guess_number < secret_number:
                print("Too small!")
            elif guess_number > secret_number:
                print("Too big!")
            else:
                print("You win!")
                break

        except ValueError("Failed to read line"):
            print(ValueError)
            continue


if __name__ == "__main__":
    py_guessing_game()
