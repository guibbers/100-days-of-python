print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is your crush's name? \n").lower()
both_names = name1 + name2

t = both_names.count('t')
r = both_names.count('r')
u = both_names.count('u')
e = both_names.count('e')

true = t + r + u + e

l = both_names.count('l')
o = both_names.count('o')
v = both_names.count('v')
e = both_names.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and menthos!")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together.")
else: 
    print(f"Your score is {love_score}")