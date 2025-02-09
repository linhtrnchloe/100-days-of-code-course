import random

stages = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)  # Use a list instead of a string
lives = 6

print(f"Here is your word: {' '.join(display)}")

while "_" in display and lives > 0:
    guess = input("Make your guess: ").lower()

    if guess in display:
        print("You already guessed that letter!")
        continue

    correct_guess = False
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            correct_guess = True

    if not correct_guess:
        lives -= 1
        print(stages[6 - lives])
        print(f"There is no '{guess}' in the word. You have {lives} lives left.")

    print(" ".join(display))

if "_" not in display:
    print("🎉 Congratulations! You guessed the word!")
else:
    print(f"💀 You lost! The word was '{chosen_word}'.")
