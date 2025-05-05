"""Money Machine"""


class MoneyMachine:
    """Collects and validates money"""

    def __init__(self) -> None:
        self.wallet = 0.0

    def collect_money(self, price) -> float:
        """Collect money needed for the purchase"""
        while True:
            try:
                coin_list = input(
                    "Deposit quarters, dimes, nickels,"
                    f"and pennies [${price}]: "
                ).split(",")
                q, d, n, p = [float(val) for val in coin_list]
                amount = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
                return amount - price
            except ValueError:
                print("Invalid Input, try again")
                continue

    def update_wallet(self, amount: float):
        """Update amount in the wallet"""
        self.wallet += amount
