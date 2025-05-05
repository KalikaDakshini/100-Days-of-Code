"""Coffee Dispenser"""


class Dispenser:
    """Dispenses coffee from the machine"""

    def __init__(self) -> None:
        self._max_capacity = {
            "water": 400,
            "milk": 600,
            "coffee": 100,
        }
        self.resources = self._max_capacity.copy()
        self.ingredients = list(self._max_capacity.keys())

        # Dispenser Recipes
        self.items = {"espresso": {"water": 50, "coffee": 18, "milk": 0}}
        self.item_names: list[str] = list(self.items.keys())

    def add_item(self, name: str, ingredients: dict[str, int]):
        """Add items to the list"""
        name = name.lower()
        self.items[name] = {
            "water": ingredients["water"],
            "coffee": ingredients["coffee"],
            "milk": ingredients["milk"],
        }
        self.item_names.append(name)

    def item_list(self) -> list[str]:
        """Return the list of items available to make"""
        return self.item_names

    def ingredient_check(self, choice: str) -> bool:
        "Check if requested ingredients are available and return the price."
        requirements = self.items[choice]
        # Check ingredients
        for ingredient in self.ingredients:
            if self.resources[ingredient] < requirements[ingredient]:
                return False
        return True

    def dispense(self, choice: str) -> str:
        """Dispense the coffee"""
        requirements = self.items[choice]
        for ingredient in self.ingredients:
            self.resources[ingredient] -= requirements[ingredient]
        return f"Here is your {choice}. Enjoy"

    def report(self) -> str:
        """Return a string containing ingredients"""
        return "; ".join(
            [f"{key}: {value}" for key, value in self.resources.items()]
        )

    def refill(self) -> None:
        """Refill the contents of the machine"""
        self.resources = self._max_capacity.copy()
