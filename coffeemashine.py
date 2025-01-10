from menu import MENU
from resources import resources


# TODO-6: Verify Transaction:
#    Check if the inserted money is enough to pay for the selected drink.
#    If insufficient funds, print: "Sorry that's not enough money. Money refunded.".
#    If extra money is provided, calculate and return change to the user.

def ver_transaction_espresso(cost_coffee):
    enough_money = 1.5
    if cost_coffee<enough_money:
        print("Sorry that's not enough money. Money refunded.")
    elif cost_coffee>=enough_money:

        money_in_change=cost_coffee-enough_money
        rest=round(money_in_change,1)
        print(f"Here is in change ${rest}")
        print("Here is your espresso ☕️. Enjoy!")


def ver_transaction_latte(cost_coffee):
    enough_money = 2.5
    if cost_coffee<enough_money:
        print("Sorry that's not enough money. Money refunded.")
    elif cost_coffee>=enough_money:

        money_in_change=cost_coffee-enough_money
        rest=round(money_in_change,1)
        print(f"Here is in change ${rest}")
        print("Here is your latte☕️. Enjoy!")


def ver_transaction_cappuccino(cost_coffee):
    enough_money=3.0
    if cost_coffee<enough_money:
        print("Sorry that's not enough money. Money refunded.")
    elif cost_coffee>=enough_money:

        money_in_change=cost_coffee-enough_money
        rest=round(money_in_change,1)
        print(f"Here is in change ${rest}")
        print("Here is your cappuccino ☕️. Enjoy!")


# TODO-5: Process Coins:
#    Create a function to handle coin input from the user.
#    Calculate the total value of the inserted coins.

def count(choose):
    print("Please insert coins")

    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?:"))
    pennies = int(input("how many pennies?:"))

    quarters_sum = quarters * 25
    dimes_sum = dimes * 10
    nickles_sum = nickles * 5
    pennies_sum = pennies * 10

    cost_coffee = (quarters_sum + dimes_sum + nickles_sum + pennies_sum) / 100
    print(cost_coffee)

    if choose=="espresso":
        ver_transaction_espresso(cost_coffee)
    elif choose=="latte":
        ver_transaction_latte(cost_coffee)


#TODO-1: Prompt User for Action:
#     Implement a function to ask the user: "What would you like? (espresso/latte/cappuccino):".
#     Include options for "report" to show the status and "off" to turn off the machine.

def ask(resources):
    choose=input("What would you like? (espresso/latte/cappuccino): ")
    water_add=["water"]
    milk_add=["milk"]
    coffee_add=["coffee"]
    coins=""

    if choose=="report":
        return (f"{water_add},{milk_add},{coffee_add}")
    elif choose=="espresso":
        count()
    elif choose=="latte":
        count()

ask(resources)

#TODO-2: Turn Off the Machine:
#     If the user enters "off", terminate the program.
#
#TODO-3: Generate a Report**:
#     Implement a function to print the current status of resources (water, milk, coffee, money).
#
#TODO-4: Check Resources:
#    Add a function to check if there are enough resources to make the selected drink.
#    If not enough resources, print: "Sorry there is not enough [resource].".

#TODO-7: Make the Coffee:
#    Implement a function to:
#    Deduct the required resources from the machine.
#    Print: "Here is your [drink]. Enjoy!".
#
#TODO-8: Main Program Loop:
#    Organize the logic into a continuous loop until the user enters "off".
#    Repeat the prompt after each action (e.g., making a drink or showing a report).
#
#TODO-9: Data Structure:
#    Store resources and drink recipes in a structured format, like a dictionary.


# TODO-1: Prompt User:
# Ask: "What would you like? (espresso/latte/cappuccino/report/off)".
#
# TODO-2: Turn Off:
# Exit if input is "off".
#
# TODO-3: Show Report:
# Print current resources (water, milk, coffee, money).
#
# TODO-4: Check Resources:
# Ensure enough resources for the selected drink.
# Print: "Sorry, not enough [resource]" if insufficient.
#
# TODO-5: Process Coins:
# Handle coin input and calculate total value.
#
# TODO-6: Verify Transaction:
# Check if money is enough for the drink.
# Refund if insufficient, return change if overpaid.
#
# TODO-7: Make Coffee:
# Deduct resources and print: "Here is your [drink]. Enjoy!".
#
# TODO-8: Main Loop:
# Repeat steps until "off" is entered.
#
# TODO-9: Data Structure:
# Store resources and recipes in a dictionary.
#
# TODO-10: Error Handling:
# Handle invalid input.