print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm? '))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input ("What is your age? "))
    if age <12:
        answer = input("Do you want a photo for $3? [y/n]")
        if answer == "y" or answer =="Y":
            print("Please pay 8$")
        else:
            print("Please pay $5")
    elif age <= 18:
        answer = input("Do you want a photo for $3? [y/n]")
        if answer == "y" or answer =="Y": 
            print("Please pay 10$")
        else:
            print("Please pay $7")
    else:
        answer = input("Do you want a photo for $3? [y/n]")
        if answer == "y" or answer =="Y":
            print("Please pay 15$")
        else:
            print("Please pay $12")
else:
    print("Sorry, you have to be taller to ride the rollercoaster.")