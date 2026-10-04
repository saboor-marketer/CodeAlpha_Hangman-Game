import random

def hangman():
    # List of 5 predefined words
    words = ["python", "coding", "gaming", "laptop", "monkey"]
    
    # Select a random word
    secret_word = random.choice(words)
    word_length = len(secret_word)
    
    # Track guessed letters and incorrect guesses
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("Welcome to Hangman!")
    print(f"Guess the word letter by letter. You have {max_incorrect} incorrect guesses allowed.")
    print()
    
    # Main game loop
    while incorrect_guesses < max_incorrect:
        # Display current state of the word
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print(f"Word: {display}")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        # Check if word is complete
        all_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                all_guessed = False
                break
        
        if all_guessed:
            print()
            print(f"Congratulations! You guessed the word: {secret_word}")
            return
        
        # Get user input
        guess = input("Enter a letter: ").lower().strip()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            print()
            continue
        
        # Check if already guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            print()
            continue
        
        # Add to guessed letters
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
        
        print()
    
    # Game over - player lost
    print(f"Game over! The word was: {secret_word}")
    print(f"You made {incorrect_guesses} incorrect guesses.")

if __name__ == "__main__":
    hangman()
