# Casino Slot Machine Game 🎰

This is a simple console-based casino slot machine game where the player can place bets, spin the slot machine, and win or lose money based on the outcome.

## Features

-   The player can deposit an initial amount of money.
-   The player can choose how many lines to bet on (up to 3).
-   The player can set the amount they want to bet per line.
-   The slot machine generates random symbols for each spin, and winnings are based on matching symbols across the chosen lines.
-   The game continues until the player decides to quit or runs out of money.

## Rules

-   Symbols:
    -   **A**: 2 occurrences
    -   **B**: 4 occurrences
    -   **C**: 6 occurrences
    -   **D**: 8 occurrences
-   Symbol values:
    -   **A**: 5x multiplier
    -   **B**: 4x multiplier
    -   **C**: 3x multiplier
    -   **D**: 2x multiplier
-   The player wins if all symbols in a row match across the selected lines.
-   The bet amount per line is multiplied by the symbol's value if the player wins on that line.

## How to Play

1. Run the game.
2. Deposit an initial amount of money.
3. Choose the number of lines to bet on (between 1 and 3).
4. Enter the amount of money you want to bet per line (between $1 and $100).
5. Spin the slot machine by pressing `Enter`.
6. The game will display the result of the spin, and you will either win or lose money.
7. The game continues until you decide to quit by pressing `q` or when your balance reaches $0.

## Game Flow

1. **Deposit**: The player is prompted to enter an initial deposit.
2. **Place Bet**: The player selects how many lines to bet on and how much to bet per line.
3. **Spin**: The slot machine generates a random result for each column, and winnings are calculated based on matching symbols across the bet lines.
4. **Win/Loss**: The player's balance is updated based on the result of the spin. If they win, the winnings are added to the balance. If they lose, the total bet amount is subtracted.
5. **Quit**: The player can quit the game at any time by pressing `q`.

## Example Gameplay

```bash
How much would you like to deposit? $100
Current balance is $100
How many lines would you like to play? 3
How much money would you like to bet per line? $10
You're betting $10 on 3 lines. Your total bet amount is $30
A | B | C
B | C | A
D | D | D
You won $20.
You won on lines 2
Current balance is $90
```
