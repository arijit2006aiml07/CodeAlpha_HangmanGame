import random

# 5 predefined words
words = ["python", "computer", "programming", "developer", "keyboard"]

# Select a random word
word = random.choice(words)

# Store the letters guessed by the player
guessed_letters = []

# Maximum number of incorrect guesses
max_incorrect_guesses = 6
incorrect_guesses = 0

# Create hidden version of the word
hidden_word = ["_"] * len(word)

print("===================================")
print("          HANGMAN GAME")
print("===================================")
print("Guess the word one letter at a time.")
print("You can make a maximum of 6 wrong guesses.")

# Game loop
while incorrect_guesses < max_incorrect_guesses and "_" in hidden_word:

    print("\nWord:", " ".join(hidden_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Wrong guesses:", incorrect_guesses)
    print("Remaining chances:", max_incorrect_guesses - incorrect_guesses)

    # Get player's guess
    guess = input("Enter a letter: ").strip().lower()

    # Check whether input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter only one letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.")
        continue

    # Add the letter to the guessed letters list
    guessed_letters.append(guess)

    # Check whether the guessed letter is in the word
    if guess in word:
        print("Correct guess!")

        # Reveal the correct letter
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess

    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Check the final result
if "_" not in hidden_word:
    print("\n===================================")
    print("       CONGRATULATIONS!")
    print("       YOU WON THE GAME!")
    print("===================================")
    print("The word was:", word)
    print("Total wrong guesses:", incorrect_guesses)

else:
    print("\n===================================")
    print("          GAME OVER!")
    print("===================================")
    print("The word was:", word)
    print("You used all 6 incorrect guesses.")

print("\nThank you for playing Hangman!")
