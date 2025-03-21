import random

# Hangman drawings for each life lost
HANGMAN_STAGES = [
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
          |
          |
          |
          |
    =========
    """
]

# Get words from the user
word_list = input("Enter words separated by spaces: ").split()

# Check if the user entered any words
if not word_list:
    print("No words entered! Exiting the game.")
    exit()

# Select a random word
chosen_word = random.choice(word_list).lower()
lives = 6

# Create the blank display
display = ["_"] * len(chosen_word)

print("\nWelcome to Hangman!")
print(" ".join(display))

game_over = False

while not game_over:
    guessed_letter = input("\nGuess a letter: ").lower()

    # Check if the guessed letter is in the word
    if guessed_letter in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guessed_letter:
                display[i] = guessed_letter
    else:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        print(HANGMAN_STAGES[lives])  # Show hangman progress

    # Show current progress
    print(" ".join(display))

    # Check for win or loss
    if "_" not in display:
        print("\n You won! The word was:", chosen_word)
        game_over = True
    elif lives == 0:
        print("\n You lost! The word was:", chosen_word)
        game_over = True
