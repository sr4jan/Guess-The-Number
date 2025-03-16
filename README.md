# Guess The Number - Multiplayer Game 🎮

## Description
"Guess The Number" is a fun multiplayer game where two players compete to guess a randomly chosen number between 1 and 100. The player who guesses the number in the fewest attempts wins!

## How to Play
1. Player 1 enters their name and starts guessing a number between 1 and 100.
2. The program provides hints:  
   - "Lower number please" if the guess is too high.  
   - "Higher number please" if the guess is too low.
3. Once Player 1 guesses correctly, their attempt count is recorded.
4. Player 2 then follows the same process with a new random number.
5. After both players have played, the game announces the winner based on the fewest attempts.

## Requirements
- Python 3.x
- No additional libraries required (uses `random` module)

## How to Run
1. Save the script as `guess_the_number.py`
2. Open a terminal or command prompt.
3. Run the script using:
   ```sh
   python guess_the_number.py
   ```

## Example Gameplay
```
*****LET'S PLAY GUESS THE NUMBER*****
Guess a number between 1 to 100
Enter Player 1 name: Alice
Guess the number: 50
Higher number please
Guess the number: 75
Lower number please
Guess the number: 62
Alice has guessed the number correctly in 3 attempts

Enter Player 2 name: Bob
Guess the number: 40
Higher number please
Guess the number: 60
Bob has guessed the number correctly in 2 attempts

Bob wins!!
```

## Features
✔ Random number generation  
✔ Multiplayer mode (2 players)  
✔ Hint system for guidance  
✔ Winner announcement  

Enjoy the game! 🎉
