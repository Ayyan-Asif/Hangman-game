import random
# List of words
words = ["python", "computer", "game", "developer", "network"]

# Description shown as a clue for each word
clues = {
    "python": "a programming language",
    "computer": "an electronic device",
    "game": "an activity played for fun",
    "developer": "a person who creates software",
    "network": "a group of connected computers",
}

# Randomly select a word
word = random.choice(words)

guessed_letters = []
incorrect_letters = []
incorrect_guesses = 0
max_attempts = 6

print("======== Welcome to Hangman! ========")

while incorrect_guesses < max_attempts:

    display = ""

    # Display the word
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Clue:", clues[word])
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)
    print("Wrong guesses:", incorrect_letters)

    # Check if player has guessed the word
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Take input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Check if already guessed
    if guess in guessed_letters or guess in incorrect_letters:
        print("You already guessed that letter!")
        continue

    # Check if guess is correct
    if guess in word:
        guessed_letters.append(guess)
        print("✅ Correct!")
    else:
        incorrect_guesses += 1
        incorrect_letters.append(guess)
        print("❌ Wrong!")

else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)