# Hangman Game

A simple text-based Hangman game implemented in Python where the player guesses a word one letter at a time.

## Features

- 5 predefined words to guess from
- 6 incorrect guesses allowed
- Console-based input/output
- Tracks guessed letters
- Displays word progress with underscores

## Requirements

- Python 3.x

## How to Run

1. Make sure you have Python installed on your system
2. Navigate to the Hangman directory
3. Run the game using the following command:

```bash
python hangman.py
```

## How to Play

1. The game will randomly select a word from a predefined list
2. You have 6 incorrect guesses allowed
3. Enter one letter at a time to guess the word
4. The game will display:
   - The current state of the word (letters revealed or underscores)
   - Number of incorrect guesses made
   - List of letters you've already guessed
5. Win by guessing all letters before running out of attempts
6. Lose if you make 6 incorrect guesses

## Example Gameplay

```
Welcome to Hangman!
Guess the word letter by letter. You have 6 incorrect guesses allowed.

Word: _ _ _ _ _ _
Incorrect guesses: 0/6
Guessed letters: 
Enter a letter: p
Good job! 'p' is in the word.

Word: p _ _ _ _ _
Incorrect guesses: 0/6
Guessed letters: p
Enter a letter: 
```

## Code Concepts Used

- `random` module for word selection
- `while` loop for game continuation
- `if-else` statements for game logic
- Strings for word manipulation
- Lists for tracking guessed letters
