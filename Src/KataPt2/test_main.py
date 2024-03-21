import pytest
from main import tictatoe

def test_tied_game():
    plays = ["x","x","o","o","o","x","x","x","o"]
    assert tictatoe(plays) == 0

def test_player_one_won_in_principal_diagonal():
    plays = ["x","o","x","o","o","6","o","o","o"]
    assert tictatoe(plays) == 1

def test_player_two_won_in_principal_diagonal():
    plays = ["x","o","x","o","x","x","x","x","x"]
    assert tictatoe(plays) == 2


    
'''
  1 | 2 | 3
  ---------
  4 | 5 | 6
  ---------
  7 | 8 | 9
'''