import random

# All The Letters, symbols and numbers
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+']

# prints and inputs at the start of the program
print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like?\n"))
number_of_numbers = int(input("How many numbers would you like?\n"))

# password creation
password = []

for letter in range(0, number_of_letters):
    password += letters[random.randint(1, len(letters) -1)]
for symbol in range(0, number_of_symbols):
    password += symbols[random.randint(1, len(symbols) -1)]
for number in range(0, number_of_numbers):
    password += numbers[random.randint(1, len(numbers) -1)]

# Shuffle the words, symbols and numbers and then turning it into a string
random.shuffle(password)
password = "".join(password)

# print the created password
print(password)