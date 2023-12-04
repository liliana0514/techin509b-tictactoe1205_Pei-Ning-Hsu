# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

#cli.py

from logic import Player, Game
import random
import os  # Import the os module for directory handling

# Ensure the 'logs' directory exists
log_directory = 'logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

if __name__ == "__main__":
    game_mode = input("Enter game mode (1 for single player, 2 for two players): ")

    if game_mode == '1':
        player1_name = input("Enter name for Player 1: ")
        player1_symbol = input("Enter symbol for Player 1 (X or O): ")
        player1 = Player(player1_name, player1_symbol)

        player2 = Player("Bot", 'O' if player1_symbol.upper() == 'X' else 'X')

    elif game_mode == '2':
        player1_name = input("Enter name for Player 1: ")
        player1_symbol = input("Enter symbol for Player 1 (X or O): ")
        player1 = Player(player1_name, player1_symbol)

        player2_name = input("Enter name for Player 2: ")
        # Automatically assign the opposite symbol to Player 2
        player2_symbol = 'X' if player1_symbol.upper() == 'O' else 'O'
        player2 = Player(player2_name, player2_symbol)

    else:
        print("Invalid game mode. Exiting.")
        exit()

    game = Game(player1, player2)
    

    try:
        while True:
            game.print_board()

            if game.current_player.name == 'Bot':
                row, col = game.current_player.make_move()
            else:
                row = int(input(f"{game.current_player.name}, enter row (0-2): "))
                col = int(input(f"{game.current_player.name}, enter col (0-2): "))

            if game.is_valid_move(row, col):
                game.make_move(row, col)
                print("Updated Board:")
                game.print_board()

                if game.check_winner():
                    print(f"{game.current_player.name} wins!")
                    first_move = f"{row}-{col}"  # assuming row and col are the last valid move
                    outcome = "Win"
                    game.record_winner(first_move, outcome)
                    break
                elif game.is_board_full():
                    print("It's a draw!")
                    first_move = f"{row}-{col}"  # assuming row and col are the last valid move
                    outcome = "Draw"
                    game.record_winner(first_move, outcome)
                    break
                
                game.switch_player()  # Switch player after each move
            else:
                print("Invalid move. Try again.")
                continue

    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting.")
