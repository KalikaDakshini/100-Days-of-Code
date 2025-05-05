"""Main logic of the machine"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    ui = Menu()
    dispenser = CoffeeMaker()
    collector = MoneyMachine()

    while True:
        choice = input(f"Enter your choice {ui.get_items()}: ")
        # Handle off
        if choice == "off":
            break
        # Handle report
        if choice == "report":
            dispenser.report()
            collector.report()
            continue
        # Handle invalid inputs
        drink = ui.find_drink(choice)
        if drink is None:
            continue
        # Handle resources
        if not dispenser.is_resource_sufficient(drink):
            print("Not enough items, please pick another one.")
            continue
        SUCCESS = collector.make_payment(drink.cost)
        if SUCCESS:
            dispenser.make_coffee(drink)
