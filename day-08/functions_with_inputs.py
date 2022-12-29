def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

name = input("Hello, what is your name? ")
location = input(f"Okay {name}, where are you from? ")

greet_with(name, location)
