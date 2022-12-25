import random

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
love_score = random.randint(1, 100)

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and menthos!")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together.")
else: 
    print(f"Your love score is {love_score}")