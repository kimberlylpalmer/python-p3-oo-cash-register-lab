#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0, total=0, items=None, transaction_details=None):
        self.discount = discount
        self.total = total
        self.items = items if items is not None else []
        self.transaction_details = (
            transaction_details if transaction_details is not None else []
        )

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.transaction_details.append((title, price, quantity))

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            if self.total.is_integer():
                print(
                    "After the discount, the total comes to ${:.0f}.".format(self.total)
                )
            else:
                print(
                    "After the discount, the total comes to ${:.2f}.".format(self.total)
                )
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.transaction_details:
            title, price, quantity = self.transaction_details.pop()
            self.total -= price * quantity
            for _ in range(quantity):
                self.items.remove(title)
        else:
            print("no transactions to void.")
