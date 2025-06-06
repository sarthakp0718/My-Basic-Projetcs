#Concession Stand Program
#A concession stand program is a system designed to manage food, beverage, and merchandise sales at concession stands, typically found in stadiums, theaters, amusement parks, or school events. These programs help track inventory, sales, pricing, and customer transactions efficiently.
menu = {
    "Pizza": 200,
    "Burger": 50,
    "Cold Brew": 100,
    "Sandwich": 80,
    "French Fries": 70
}

cart = []
total = 0

print("-----------------MENU---------------------")
for key, value in menu.items():
    print(f"{key:10}: ₹{value}")
print("--------------------------------------")

while True:
    food = input("Select an Item (q to quit): ").title()  # Capitalizes first letter
    if food == "Q":
        break
    elif food in menu:
        cart.append(food)  # Fixed the typo

print("-----------------YOUR ORDER-----------")
for food in cart:
    total += menu[food]  # Directly referencing dictionary key
    print(food)

print("--------------------------------------")
print(f"Total amount: ₹{total}")
