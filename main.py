import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def get_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []

    for _ in range(cols):
        all_symbols_copy = all_symbols[:]
        col = []
        for _ in range(rows):
            value = random.choice(all_symbols_copy)
            all_symbols_copy.remove(value)
            col.append(value)
        columns.append(col)

    return columns

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) -1:
                print(col[row], end=" | ")
            else:
                print(col[row])



def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to play? ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be between 1 and ", MAX_LINES)
        else:
            print("Please enter a valid number of lines.")
    return lines

def get_bet():
    while True:
        bet_amount = input("How much money would you like to bet per line? $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if bet_amount >= MIN_BET and bet_amount <= MAX_BET:
                break
            else:
                print(f"Bet amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Enter a valid number")

    return bet_amount

def run_game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet_amount = bet * lines

        if total_bet_amount > balance:
            print(f"You dont have enough balance to bet ${total_bet_amount}, your balance is {balance}")
        else:
            break;            
    
    print(f"You're betting ${bet} on {lines} lines. Your total bet amount is ${total_bet_amount}")

    slots = get_machine_spin(ROWS, COLS, symbols_count)

    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)

    print(f"You won ${winnings}.")
    if winnings > 0: 
        print(f"You won on lines", *winning_lines) # The * is the splat or the unpack operator
    return winnings - total_bet_amount

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("press enter to play or q to stop playing. ")
        if spin == "q":
            break
        else:
            final_winnings = run_game(balance)
            if final_winnings > 0:
                print(f"You won a total of ${final_winnings} in that spin")
            else:
                print(f"You lost ${abs(final_winnings)} in that spin")
            
            balance += final_winnings
    
    print(f"Your final balance is ${balance}")






main()