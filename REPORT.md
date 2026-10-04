# Hangman Game - Project Report

## Project Overview

This project implements a classic Hangman game in Python. The game challenges players to guess a hidden word by suggesting letters within a limited number of incorrect attempts.

## Objectives

- Create a text-based interactive game
- Implement core game logic using fundamental Python concepts
- Provide an engaging user experience through console interface
- Demonstrate understanding of control flow and data structures

## Technical Specifications

### Language
- Python 3.x

### Key Concepts Implemented

1. **Random Module**
   - Used for selecting a random word from the predefined list
   - `random.choice()` function selects one word at game start

2. **While Loop**
   - Main game loop continues until player wins or loses
   - Condition: `incorrect_guesses < max_incorrect`
   - Loop also breaks early when word is completely guessed

3. **If-Else Statements**
   - Input validation (single letter check)
   - Checking if letter was already guessed
   - Determining if guess is correct or incorrect
   - Checking win condition

4. **Strings**
   - Word representation with underscores for unguessed letters
   - String manipulation for display
   - Case normalization (`.lower()`)
   - Whitespace removal (`.strip()`)

5. **Lists**
   - Store predefined word list
   - Track guessed letters
   - Dynamic display of guessed letters

## Implementation Details

### Word Selection
- 5 predefined words: "python", "coding", "gaming", "laptop", "monkey"
- Random selection at game initialization
- Word length calculated for display purposes

### Game State Management
- `guessed_letters`: List to track all player guesses
- `incorrect_guesses`: Counter for wrong attempts
- `max_incorrect`: Set to 6 as the game limit

### User Input Handling
- Single character validation
- Alphabet character check
- Case insensitivity (converts to lowercase)
- Duplicate guess prevention

### Display Logic
- Shows current word state with revealed letters and underscores
- Displays incorrect guess count
- Shows list of all guessed letters
- Provides feedback on each guess

### Win/Lose Conditions
- **Win**: All letters in secret word are guessed
- **Lose**: 6 incorrect guesses made

## Code Structure

```
hangman()
├── Initialize game variables
├── Print welcome message
├── while loop (game continues)
│   ├── Display current state
│   ├── Check win condition
│   ├── Get user input
│   ├── Validate input
│   ├── Check for duplicate guesses
│   ├── Add to guessed letters
│   ├── Check if correct/incorrect
│   └── Update game state
└── Display final result
```

## Testing Considerations

### Manual Testing Performed
- Game runs without errors
- Random word selection works correctly
- Correct guesses reveal letters
- Incorrect guesses increment counter
- Duplicate guess detection works
- Input validation prevents invalid entries
- Win condition triggers correctly
- Lose condition triggers at 6 incorrect guesses

### Edge Cases Handled
- Empty input
- Multiple character input
- Non-alphabetic input
- Uppercase letters
- Repeated guesses

## Limitations and Future Enhancements

### Current Limitations
- Only 5 words available
- No difficulty levels
- No persistent high scores
- No word hint system
- Text-only interface

### Potential Enhancements
- Expand word list from external file
- Add difficulty categories
- Implement scoring system
- Add visual hangman display
- Support multiple rounds
- Add timer for competitive play

## Conclusion

The Hangman game successfully demonstrates the use of fundamental Python programming concepts including random selection, control flow, conditional logic, and data structures. The project provides a complete, playable game experience within the specified scope while maintaining clean, readable code structure.

## Files Included

- `hangman.py` - Main game implementation
- `README.md` - User instructions and setup guide
- `report.md` - This project documentation
