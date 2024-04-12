import pytest
from main import tictactoe

def test_game_over():
    table = ["x","o","x","o","x","o","o","x","o"]
    assert tictactoe(table) == 0

def test_player_one_won_in_pricipal_diagonal():
    table = ["x","o","o","4","x","6","7","8","x"]
    
    assert tictactoe(table) == 1

def test_player_two_won_in_pricipal_diagonal():
    table = ["o","x","3","x","o","6","x","8","o"]
    
    assert tictactoe(table) == 2