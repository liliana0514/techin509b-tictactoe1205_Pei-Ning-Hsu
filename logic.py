# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import random
import csv
from datetime import datetime

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self):
        if self.name == 'Bot':
            row = random.randint(0, 2)
            col = random.randint(0, 2)
        else:
            row = int(input(f"{self.name}, enter row (0-2): "))
            col = int(input(f"{self.name}, enter col (0-2): "))
        return row, col

class Game:
    def __init__(self, player1, player2):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.players = [player1, player2]
        self.current_player = self.players[0]  # Set an initial value
        self.winner = None

    def print_board(self):
        for row in self.board:
            print("|".join(row))
        print()

    def start_game(self):
        self.current_player = self.players[0]
        while True:
            self.print_board()

            # ... other code ...

            if self.is_valid_move(row, col):
                self.switch_player()  # Add this line to switch players before the move
                self.make_move(row, col)
                print("Updated Board:")
                self.print_board()
            else:
                print("Invalid move. Try again.")
                continue

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player.symbol
            first_move = f"{row}-{col}"  # Format the first move
            outcome = "Win" if self.check_winner() else ("Draw" if self.is_board_full() else "Continue")
            self.record_winner(first_move, outcome)
        else:
            print("Invalid move. Try again.")

    def switch_player(self):
        current_index = self.players.index(self.current_player)
        next_index = (current_index + 1) % len(self.players)
        self.current_player = self.players[next_index]

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                self.winner = self.current_player
                return True

            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                self.winner = self.current_player
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.winner = self.current_player
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.winner = self.current_player
            return True

        return False

    def is_board_full(self):
        return all(all(cell != ' ' for cell in row) for row in self.board)

    def is_valid_move(self, row, col):
        print(f"Checking validity for ({row}, {col})")
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def get_winner(self):
        return self.winner
    def announce_winner(self, winner):
        print(f"{winner.name} wins!")
    def record_winner(self, first_move, outcome):
        with open('logs/game_log.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            winner_name = self.get_winner().name if self.get_winner() else 'Draw'
            writer.writerow([timestamp, self.players[0].name, self.players[1].name, winner_name, first_move, outcome])

    def record_winner(self, first_move, outcome):
        with open('logs/game_log.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            winner_name = self.get_winner().name if self.get_winner() else 'Draw'
            writer.writerow([timestamp, self.players[0].name, self.players[1].name, winner_name, first_move, outcome])
