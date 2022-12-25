import random

names_string = input("Give me everybody's namem, separated by a comma: \n")
names = names_string.split(", ")
people_count = len(names)
random_number = random.randint(0, people_count -1)
person_paying = names[random_number]

print(f"{person_paying} is paying the bill today!")