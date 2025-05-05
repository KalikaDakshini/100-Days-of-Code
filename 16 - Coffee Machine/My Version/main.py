"""Main control unit of the coffee machine"""

from user_interface import UI
from dispenser import Dispenser
from money_collector import MoneyMachine

if __name__ == "__main__":
    # Initialise dispenser
    dispenser = Dispenser()
    dispenser.add_item("Latte", {"milk": 150, "water": 200, "coffee": 24})
    dispenser.add_item("Capuccino", {"milk": 100, "water": 250, "coffee": 24})

    # Initialise menu and add items
    menu = UI(dispenser.item_list())

    # Initialise Money machine
    collector = MoneyMachine()

    # Run game loop
    while True:
        choice = menu.take_order()
        if choice == "off":
            menu.out("Exiting machine...")
            break
        # Report data
        if choice == "report":
            menu.out(dispenser.report())
        # Refill items
        elif choice == "refill":
            dispenser.refill()
        # Serve coffee
        else:
            # Check for ingredients
            STATUS = dispenser.ingredient_check(choice)
            if not STATUS:
                menu.err(
                    f"Not enough ingredients for {choice}\
                        \nRefill cart and try again"
                )
                continue
            change = collector.collect_money(menu.get_price(choice))
            # Check for money
            if change < 0:
                menu.err("Not enough money. Transaction cancelled")
                continue
            menu.out(f"Collect your change: ${change:.2f}")
            menu.out(dispenser.dispense(choice))
