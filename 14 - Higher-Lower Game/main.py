"""Main file of the game"""

import os
import random
import terminology as tlgy

from game_data import data
from art import logo, vs


def extract_data() -> dict[str, int]:
    """Extract data from data file into a desirable format for the game."""
    count_dict: dict[str, int] = {}
    for elem in data:
        count_dict[elem["name"]] = elem["follower_count"]
    return count_dict


def get_response(name1: str, name2: str) -> str:
    """Get response from player"""
    print(tlgy.in_blue(f"Compare A: {name1}"))
    print(tlgy.in_cyan(vs))
    print(tlgy.in_blue(f"Compare B: {name2}"))
    response = input(
        tlgy.in_green("Who has more followers? 'A' or 'B': ")
    ).lower()
    return response


def gameloop():
    """Main game loop"""
    # Initialize variables
    player_score = 0
    end_game = False

    # Extract data
    follower_data = extract_data()
    names_data = list(follower_data.keys())

    # Loop the game till failure
    while True:
        os.system("clear")
        print(tlgy.in_cyan(logo).in_bold())

        # End the game on failure
        if end_game:
            print(tlgy.in_blue(f"Wrong Answer! Final Score: {player_score}"))
            break

        # Show player score on subsequent iterations
        print(tlgy.in_magenta("Type 'Ctrl+D' to exit game"))
        if player_score != 0:
            print(
                tlgy.in_green(f"Correct Answer; Current Score: {player_score}")
            )
        else:
            print(tlgy.in_green(f"Current Score: {player_score}"))

        # Get two random elements from the data
        name1, name2 = random.sample(names_data, 2)
        count1, count2 = follower_data[name1], follower_data[name2]
        win_choice = "a"
        if count2 > count1:
            win_choice = "b"

        # Check for player response
        player_response = get_response(name1, name2)

        # Check if the input is valid
        if player_response == win_choice:
            player_score += 1
        else:
            end_game = True


if __name__ == "__main__":
    gameloop()
