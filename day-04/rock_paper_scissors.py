import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. \n"))
computer_choice = random.randint(0, 2)
result = ""

if your_choice == 0:
    print(rock)
elif your_choice == 1:
    print(paper)
elif your_choice == 2:
    print(scissors)

print("Computer chose: \n")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if your_choice == 0 and computer_choice == 0:
    result = "It's a draw!"
elif your_choice == 0 and computer_choice == 1:
    result = "You lose :("
elif your_choice == 0 and computer_choice == 2:
    result = "You win! Yay!"

if your_choice == 1 and computer_choice == 0:
    result = "You win! Yay!"
elif your_choice == 1 and computer_choice == 1:
    result = "It's a draw!"
elif your_choice == 1 and computer_choice == 2:
    result = "You lose :("

if your_choice == 2 and computer_choice == 0:
    result = "You lose :("
elif your_choice == 2 and computer_choice == 1:
    result = "You win! Yay!"
elif your_choice == 2 and computer_choice == 2:
    result = "It's a draw!"

print(result)