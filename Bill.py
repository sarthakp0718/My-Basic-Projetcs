#Simple Billing Software
print("Welcome to Sarthak's Super Mall")
print(input("What do you wanna buy"))
amt=0
milk=40
bread=30
butter=20
ghee=20
paneer=50
chocolate=10
biscuit=20
def qty():
    global quantity
    while True:
        quantity=input("How many?")
        if quantity.isdigit():
            quantity=int(quantity)
            return quantity
        else:
            print("It must be a number")
        
while True:
    category