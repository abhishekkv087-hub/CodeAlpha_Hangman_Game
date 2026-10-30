import random

WORDS = ["python", "laptop", "college", "coding", "project"]
MAX_WRONG_GUESSES = 6


def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    print("=" * 35)
    print("       WELCOME TO HANGMAN")
    print("=" * 35)
    print("Guess the hidden word one letter at a time.")
    print(f"You can make up to {MAX_WRONG_GUESSES} incorrect guesses.")
    print("Word:", " ".join("_" for _ in secret_word))

    while wrong_guesses < MAX_WRONG_GUESSES:
    
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )
        print("\nWord:", display_word)
        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")
        print(f"Incorrect guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")

        guess = input("Enter one letter: ").strip().lower()

    
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
            if all(letter in guessed_letters for letter in secret_word):
                print("\nCongratulations! You guessed the word:", secret_word)
                break
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    else:
        print("\nGame over! The word was:", secret_word)

    print("\nThanks for playing!")


if __name__ == "__main__":
    play_hangman()
