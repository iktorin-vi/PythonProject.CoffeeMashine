from menu import MENU
from resources import resources
profit=0


# TODO-3: Show Report:
# # Print current resources (water, milk, coffee, money).
def resource_sufficient(order_ingredients):
    """Return """
    is_enough=True
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry that's not enough {item}.")
            is_enough=False
    return is_enough


# TODO-5: Process Coins:
# Handle coin input and calculate total value.
def count():
    """Return the total calculated from coins inserted"""
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
    return cost_coffee


# TODO-6: Verify Transaction:
# Check if money is enough for the drink.
# Refund if insufficient, return change if overpaid.
def transaction_successful(money_received,drink_cost):
    if money_received>=drink_cost:
        money_in_change = round(money_received - drink_cost,2)
        print(f"Here is in change ${money_in_change}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO-7: Make Coffee:
# Deduct resources and print: "Here is your [drink]. Enjoy!".
def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}☕️.Enjoy!")


# TODO-8: Main Loop:
# Repeat steps until "off" is entered.
# TODO-1: Prompt User:
# Ask: "What would you like? (espresso/latte/cappuccino/report/off)".
# TODO-2: Turn Off:
# Exit if input is "off".
# TODO-4: Check Resources:
# Ensure enough resources for the selected drink.
# Print: "Sorry, not enough [resource]" if insufficient.
is_on = True
while is_on:
    choose = input("What would you like? (espresso/latte/cappuccino): ")
    if choose=="off":
        is_on=False
    elif choose=="report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffe : {resources['coffee']}ml")
        print(f"Money : {profit}")
    else:
        drink=MENU[choose]
        if resource_sufficient(drink["ingredients"]):
            payment=count()
            if transaction_successful(payment,drink["cost"]):
                make_coffee(choose,drink["ingredients"])
