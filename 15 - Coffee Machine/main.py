"""Coffee Machine Simulator"""

from copy import deepcopy

import terminology as tlgy
from resources import MENU, resources as RESOURCE_MAX

# Resources
ingredient_list: list[str] = list(RESOURCE_MAX.keys())


def resource_check(choice: str, resources: dict[str, int]) -> bool:
    """Check if resources are sufficient"""
    # Populate requirement list
    requirements = {val: 0 for val in ingredient_list}
    for ingredient in ingredient_list:
        try:
            requirements[ingredient] = MENU[choice]["ingredients"][ingredient]
        except KeyError:
            requirements[ingredient] = 0
    # Check availability
    for ingredient in ingredient_list:
        if requirements[ingredient] > resources[ingredient]:
            print(tlgy.in_yellow(f"Sorry there is not enough {ingredient}"))
            return False
    # Deduct ingredients
    for ingredient in ingredient_list:
        resources[ingredient] -= requirements[ingredient]
    return True


def money_prompt(choice: str) -> bool:
    """Get money from user, check if valid, and return as a dict"""
    # Read input from user
    amount, price = 0, MENU[choice]["cost"]
    while not amount:
        try:
            amount = float(input(tlgy.in_cyan(f"Enter amount [${price}]: ")))
        # Catch invalid inputs
        except ValueError:
            print("Invalid Input. Enter a numerical amount")
            continue

        if price > amount:
            print("Sorry that's not enough money. Refunded")
            return False
        print(tlgy.in_black(f"Here is your change ${amount - price}"))

    return True


def make_coffee(response: str, resources: dict[str, int]) -> bool:
    """Make coffee noted by the response."""
    # Check if resources are sufficient
    status = resource_check(response, resources)
    if not status:
        return False
    # Prompt user for money
    status = money_prompt(response)
    return status


def interact_prompt() -> str:
    """Prompt the user for input"""
    valid_responses = (
        "espresso",
        "latte",
        "capuccino",
        "off",
        "report",
        "refill",
    )
    # Read and validate user response
    while True:
        response = input(
            tlgy.in_cyan("What would you like (espresso/latte/capuccino): ")
        ).lower()
        if not response.startswith(valid_responses):
            print(tlgy.in_magenta("Invalid response, try again"))
        else:
            return response


def gameloop():
    """Main loop of the coffee machine"""
    resources = deepcopy(RESOURCE_MAX)
    while True:
        try:
            response = interact_prompt()
            # Close the machine
            if response == "off":
                print(tlgy.in_yellow("Exiting machine..."))
                break
            # Generate a report
            if response == "report":
                print(tlgy.in_yellow(resources))
            # Refill Resources
            elif response == "refill":
                print(tlgy.in_yellow("Refilling resources"))
                resources = deepcopy(RESOURCE_MAX)
            # Make and serve coffee
            else:
                status = make_coffee(response, resources)
                if not status:
                    continue
                print(tlgy.in_black(f"Here is your {response}. Enjoy"))
        # Catch ^D
        except EOFError:
            print(tlgy.in_yellow("\nExiting machine..."))
            break
        # Catch ^C
        except KeyboardInterrupt:
            print()
            continue


if __name__ == "__main__":
    gameloop()
