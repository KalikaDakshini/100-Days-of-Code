"""User Interface for the coffee machine"""

import terminology as tlgy


class UI:
    """Class to hold the Menu"""

    def __init__(self, items: list[str]) -> None:
        # Diagnostic data
        self.admin_commands = ["off", "report", "refill"]
        self.item_names = items.copy()
        self.prices = {"espresso": 1.5, "latte": 2.5, "capuccino": 3.0}

    def take_order(self):
        """Take order from the user"""
        while True:
            try:
                # Take input from the user
                choice = input(
                    f"Enter an input ({"/".join(self.item_names)}): "
                ).lower()
                if choice in self.item_names or choice in self.admin_commands:
                    return choice
                self.err("Invalid Input. Try Again")
                continue
            except (EOFError, KeyboardInterrupt):
                print()
                return "off"

    def get_price(self, choice: str) -> float:
        """Return the price of the choice"""
        return self.prices[choice]

    def out(self, msg: str):
        """Report the contents as output"""
        print(tlgy.in_cyan(msg))

    def err(self, msg: str):
        """Report the contents as error"""
        print(tlgy.in_red(msg))
