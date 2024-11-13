from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = Menu()
machine = CoffeeMaker()
cash = MoneyMachine()
is_on = True

while is_on:
    choice = input(f"What would you like? ({order.get_items()}): ")
    if choice == "off":
        is_on = False
        print("Good bye.")
    elif choice == "report":
        machine.report()
        cash.report()
    else:
        users_choice = order.find_drink(choice)
        if machine.is_resource_sufficient(users_choice):
            transaction_successful = cash.make_payment(users_choice.cost)
            machine.make_coffee(users_choice)
