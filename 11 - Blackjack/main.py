"""Game loop file for Blackjack"""

import os

from dealer import Dealer, Card


def show_cards(dealer, cards: list[Card]) -> None:
    """Print the cards"""
    print(f"\tPlayer Cards: {cards[0]}", end="")
    for card in cards[1:]:
        print(f", {card}", end="")
    player_score = dealer.total_value(cards)
    print(f"; Player Score: {player_score}")


def game_info(dealer, cards: list[Card]) -> None:
    """Print the information for the Player"""
    # Player Cards and Score
    show_cards(dealer, cards)
    # Dealer's First Card
    print(f"\tDealer First Card: {dealer.first_card()}")


def finalize(dealer, player_cards):
    """Finish the game"""
    show_cards(dealer, player_cards)
    player_score = dealer.total_value(player_cards)
    print(
        f"\tDealer Cards: {dealer.first_card()}, {dealer.second_card()}; \
Dealer Score: {dealer.score}"
    )
    if player_score > dealer.score:
        print("\tYou win :)")
    else:
        print("\tYou lose :(")


def gameloop():
    """Main game loop"""
    while True:
        os.system("clear")
        print("BLACKJACK GAME")
        # Things needed for the game
        dealer = Dealer()
        game_end = False

        # Deal cards
        player_cards = dealer.deal_starting_cards()
        game_info(dealer, player_cards)

        while True:
            # Prompt player to choose
            player_input = input("Hit or Stand? [H/s] ")
            # Hit
            if player_input.lower().startswith("h"):
                # Get new card
                player_cards.append(dealer.hit())
                game_info(dealer, player_cards)
                # End the game if the player hits or goes over 21
                player_score = dealer.total_value(player_cards)
                if player_score == 21:
                    print("\tBLACKJACK!!!")
                    game_end = True
                    break
                elif player_score > 21:
                    print("\tGone bust D:")
                    game_end = True
                    break
            # Stand
            else:
                break

        # If the game isn't finished in the last check, check again
        if not game_end:
            finalize(dealer, player_cards)

        # Start a new game
        continue_prompt = input("\nPlay Again? [Y/n] ")
        if not continue_prompt.lower().startswith("y"):
            break


if __name__ == "__main__":
    gameloop()
