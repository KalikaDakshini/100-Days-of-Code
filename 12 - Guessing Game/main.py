import random


def gameloop():
    """Main Game loop"""
    # Pick a random number
    answer = random.randint(1, 100)
    # Prompt player for the game
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty, easy or hard [E/h] ")
    max_count = 10 if difficulty.lower().startswith("e") else 5
    print(f"You have {max_count} attempts to guess the number")
    # Let the player guess
    count = 0
    while count < max_count:
        guess = int(input("Make a guess: "))
        if guess == answer:
            print("You guessed right. Congrats")
            return
        elif guess > answer:
            print("You guessed too high. Try again")
        else:
            print("You guessed too low. Try again")
        count += 1

    print(f"You are out of guesses. The correct answer is {answer}")


if __name__ == "__main__":
    gameloop()
