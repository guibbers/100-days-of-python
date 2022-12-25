year = int(input("Which year do you want to check? "))

if year % 4 == 0 or year % 400 == 0:
    print("It's a leap year")
else:
    print("It's not a leap year")