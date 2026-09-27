from menu_resources import menu
from menu_resources import resources , menu , logo

def handle_recipe(user_choice , processed_coins):
    global money
    drink = menu[user_choice]
    ingredients = drink["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}. Money refunded.")
            return
    if processed_coins >= drink["cost"]:
        change = round(processed_coins - drink["cost"] , 2)
        print(f"Here is your {user_choice}☕. Enjoy!")
        money += drink["cost"]
        if change > 0:
            print(f"Here is you change: ${change}.")
        else:
            return
    else:
        print("Sorry that\'s not enough money. Money refunded.")
        return
    
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    


machine_off = False

money = 0

while machine_off == False:
    print(logo)
    user_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()

    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        print("Please insert coins.")
        quarters = float(input("How many quarters? "))
        dimes = float(input("How many dimes? "))
        nickels = float(input("How many nickels? "))
        pennies = float(input("How many pennies? "))
        processed_coins = float((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01))
        handle_recipe(user_choice , processed_coins)
    elif user_choice == "report":
        print(f'''
        Water : {resources["water"]}ml
        Milk : {resources["milk"]}ml
        Coffee : {resources["coffee"]}g
        Money : ${money}
    ''')
    elif user_choice == "off":
        machine_off = True
    else:
        print("Invalid input")
        break