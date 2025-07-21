resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

COIN_VALUES = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins:")
    total = 0
    for coin in COIN_VALUES:
        count = int(input(f"How many {coin}? "))
        total += count * COIN_VALUES[coin]
    return round(total, 2)

def transaction_successful(payment, cost):
    global profit
    if payment < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = round(payment - cost, 2)
    if change > 0:
        print(f"Here is ${change:.2f} in change.")
    profit += cost
    return True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Turning off the coffee machine.")
        break
    elif choice == "report":
        print_report()
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid input. Please choose a valid option.")





# Initial resources
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
#     "money": 0.0
#  }

# # Menu with cost and ingredients
# MENU = {
#     "espresso": {
#         "ingredients": {"water": 50, "coffee": 18},
#         "cost": 1.5
#     },
#     "latte": {
#         "ingredients": {"water": 200, "milk": 150, "coffee": 24},
#         "cost": 2.5
#     },
#     "cappuccino": {
#         "ingredients": {"water": 250, "milk": 100, "coffee": 24},
#         "cost": 3.0
#     }
# }

# # Coin values
# COIN_VALUES = {
#     "quarters": 0.25,
#     "dimes": 0.10,
#     "nickels": 0.05,
#     "pennies": 0.01
# }

# def print_report():
#     print(f"Water: {resources['water']}ml")
#     print(f"Milk: {resources['milk']}ml")
#     print(f"Coffee: {resources['coffee']}g")
#     print(f"Money: ${resources['money']:.2f}")

# def is_resource_sufficient(order_ingredients):
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#     return True

# def process_coins():
#     print("Please insert coins:")
#     total = 0
#     for coin in COIN_VALUES:
#         count = int(input(f"How many {coin}? "))
#         total += count * COIN_VALUES[coin]
#     return round(total, 2)

# def transaction_successful(payment, cost):
#     if payment < cost:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#     change = round(payment - cost, 2)
#     if change > 0:
#         print(f"Here is ${change:.2f} in change.")
#     resources["money"] += cost
#     return True

# def make_coffee(drink_name, order_ingredients):
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name}. Enjoy!")

# # Main program loop
# while True:
#     choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
#     if choice == "off":
#         print("Turning off the coffee machine.")
#         break
#     elif choice == "report":
#         print_report()
#     elif choice in MENU:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
#     else:
#         print("Invalid input. Please choose a valid option.")
