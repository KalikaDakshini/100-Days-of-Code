"""Algorithms for Blackjack"""

import random


class Card:
    """Class to hold Card object"""

    def __init__(self, card_str: str) -> None:
        self.card_str = card_str
        self._type = card_str[-1]
        # Assign value to card
        if self.card_str.startswith(("K", "Q", "J")):
            self._value: int = 10
        else:
            self._value: int = int(card_str[:-1])

    @property
    def value(self) -> int:
        """Return the value of the card"""
        return self._value

    def __str__(self) -> str:
        return self.card_str


class Dealer:
    """Class to hold the deck"""

    def __init__(self) -> None:
        """Generate a deck of 52 cards"""
        self.deck: list[Card] = []
        card_values = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
        ]
        for ctype in ["H", "D", "C", "S"]:
            for val in card_values:
                self.deck.append(Card(f"{val}{ctype}"))
        random.shuffle(self.deck)

        self.cards = [self.deck.pop(), self.deck.pop()]
        self._score: int = self.total_value(self.cards)

    @property
    def score(self) -> int:
        """Return the score of dealer"""
        return self._score

    def first_card(self) -> Card:
        """Return the first card of dealer"""
        return self.cards[0]

    def second_card(self) -> Card:
        """Return the first card of dealer"""
        return self.cards[1]

    def deal_starting_cards(self) -> list[Card]:
        """Deal starting cards"""
        return [self.deck.pop(), self.deck.pop()]

    def hit(self):
        """Deal one more card"""
        return self.deck.pop()

    def total_value(self, card_set: list[Card]) -> int:
        """Return the total value of cards"""
        # Add card total
        total_value = 0
        for card in card_set:
            total_value += card.value

        # Treat ace as 11 if not bust
        for card in card_set:
            if card.value == 1 and total_value + 10 < 22:
                total_value += 10
                break

        return total_value
