# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python while practicing string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️ Create the Game Logic

#### Description
Develop a playable Hangman game where a player guesses letters to reveal a hidden word before running out of attempts.

#### Requirements
Completed program should:

- Choose a word randomly from a predefined list.
- Display the hidden word using underscores, such as `_ _ _ _ _`.
- Accept a single letter guess from the player.
- Reveal matching letters in the correct positions.
- Track incorrect guesses and remaining attempts.
- End the game when the player either guesses the word correctly or runs out of attempts.

### 🛠️ Add Win/Loss Feedback

#### Description
Improve the game so it clearly communicates the result and keeps the player informed throughout the round.

#### Requirements
Completed program should:

- Display a win message when the full word is guessed.
- Display a lose message when the player has no attempts left.
- Show the final word at the end of the game.
- Use clear prompts and readable output for each turn.
- Example output:
  ```python
  Guess a letter: a
  Current word: _ a _ _ _
  Incorrect guesses: 1/6
  ```
