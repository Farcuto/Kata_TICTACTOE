import pytest
from main import tictactoe
def test_minimun_funcional():
    table_tictactoe = ["","","","","","","","",""]
    assert tictactoe(table_tictactoe) == 0
    

def test_player_one_won_in_diagonal():
    table = list(["x","2","3","4","x","6","7","8","x"])
    assert tictactoe(table) == 1
    
def test_player_one_won_in_diagonal_inverted():
    table = list(["1","2","x","4","x","6","x","8","9"])
    assert tictactoe(table) == 1
    
def test_player_one_won_in_firts_column():
    table = list(["x","x","x","4","5","6","7","8","9"])
    
    assert tictactoe(table) == 1

def test_player_one_won_in_second_column():
    table = list(["1","2","3","x","x","x","7","8","9"])
    
    assert tictactoe(table) == 1

def test_player_one_won_in_third_column():
    table = list(["1","2","3","4","5","6","x","x","x"])
    
    assert tictactoe(table) == 1
    
def test_player_one_won_in_firts_row():
    table = list(["x","2","3","x","5","6","x","8","9"])
    
    assert tictactoe(table) == 1
    
def test_player_one_won_in_second_row():
    table = list(["1","x","3","4","x","6","7","x","9"])
    
    assert tictactoe(table) == 1

def test_player_one_won_in_third_row():
    table = list(["1","2","x","4","5","x","7","8","x"])
    
    assert tictactoe(table) == 1


############################

def test_player_two_won_in_diagonal():
    table = list(["O","2","3","4","O","6","7","8","O"])
    assert tictactoe(table) == 2
    
def test_player_two_won_in_diagonal_inverted():
    table = list(["1","2","O","4","O","6","O","8","9"])
    assert tictactoe(table) == 2
    
def test_player_two_won_in_firts_column():
    table = list(["O","O","O","4","5","6","7","8","9"])
    
    assert tictactoe(table) == 2

def test_player_two_won_in_second_column():
    table = list(["1","2","3","O","O","O","7","8","9"])
    
    assert tictactoe(table) == 2

def test_player_two_won_in_third_column():
    table = list(["1","2","3","4","5","6","O","O","O"])
    
    assert tictactoe(table) == 2
    
def test_player_two_won_in_firts_row():
    table = list(["O","2","3","O","5","6","O","8","9"])
    
    assert tictactoe(table) == 2
    
def test_player_two_won_in_second_row():
    table = list(["1","O","3","4","O","6","7","O","9"])
    
    assert tictactoe(table) == 2

def test_player_two_won_in_third_row():
    table = list(["1","2","O","4","5","O","7","8","O"])
    
    assert tictactoe(table) == 2

def test_tied_game():
    table = list(["o","o","x","x","x","o","o","x","x"])


    