print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do youu want? S, M or L? ")

if size == "s" or size == "S":
    price = 15
elif size == "m" or size == "M":
    price = 20
elif size == "l" or size == "L":
    price = 25
else:
    print("I didn't understand that, sorry :/")

add_pepperoni = input("Do you want pepperoni? [y/n] ")
if add_pepperoni == "Y" or add_pepperoni == "y":
    if size == "s" or size == "S":
        price += 2
    else: 
        price += 3

extra_cheese = input("Do you want extra cheese? [y/n] ")
if extra_cheese == "Y" or extra_cheese == "y":
    price += 1

print(f"Please pay ${price} for your {size} sized pizza.")
