# tests.py
import pytest
from logic import Player, Game

@pytest.fixture
def empty_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def test_empty_board_initialization(empty_board):
    game = Game(Player("Player1", "X"), Player("Player2", "O"))
    assert game.board == empty_board

def test_game_initialization_with_two_players():
    player1 = Player("Player1", "X")
    player2 = Player("Player2", "O")
    game = Game(player1, player2)
    assert len(game.players) == 2
    assert game.players[0] == player1
    assert game.players[1] == player2

def test_game_initialization_with_one_player():
    player1 = Player("Player1", "X")
    player2 = Player("Bot", "O")
    game = Game(player1, player2)
    assert len(game.players) == 2
    assert game.players[0] == player1
    assert game.players[1] == player2

def test_players_assigned_unique_pieces():
    player1 = Player("Player1", "X")
    player2 = Player("Player2", "O")
    assert player1.symbol != player2.symbol

def test_switch_player():
    player1 = Player("Player1", "X")
    player2 = Player("Player2", "O")
    game = Game(player1, player2)
    game.switch_player()
    assert game.current_player == player2
    game.switch_player()
    assert game.current_player == player1

def test_valid_move():
    player1 = Player("Player1", "X")
    player2 = Player("Player2", "O")
    game = Game(player1, player2)
    assert game.is_valid_move(0, 0)
    assert not game.is_valid_move(3, 0)
    assert not game.is_valid_move(0, 3)
    assert not game.is_valid_move(-1, 0)
    assert not game.is_valid_move(0, -1)

    # Make a move before checking validity
    game.make_move(0, 0)

    assert not game.is_valid_move(0, 0)  # Already occupied
