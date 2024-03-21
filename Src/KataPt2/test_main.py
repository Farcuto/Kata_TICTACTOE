import pytest
from main import tictatoe

def test_tied_game():
    plays = ["1","2","3","4","6","7","8","9"]
    assert tictatoe(plays) == 0

def test_player_one_won_in_principal_diagonal():
    plays = ["1","2","5","3","9","6","4","7","8"]
    assert tictatoe(plays) == 1

def test_player_two_won_in_principal_diagonal():
    plays = ["2","1","3","5","6","9","4","7","8"]
    assert tictatoe(plays) == 2


    
'''
  1 | 2 | 3
  ---------
  4 | 5 | 6
  ---------
  7 | 8 | 9
'''