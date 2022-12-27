import random
import hangman_art
import hangman_words

display = []
end_of_game = False
lives = 6

word = random.choice(hangman_words.word_list)

for letter in word:
    display += "_"

print(hangman_art.logo)
print(f"pssst, the solution is {word}")

print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You've already guessed {guess}")

    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] = guess

    if guess not in word:
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      lives -= 1      

    print(f"{' '.join(display)}")    
    
    print(hangman_art.stages[lives])
    if lives == 0:
        end_of_game = True
        print("You lose.")
    if "_" not in display:
        end_of_game = True
        print("You win!")