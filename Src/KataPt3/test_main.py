import pytest
from main import tictactoe

def test_tied_game():
    table_ttt = ["1","2","3","4","5","6","7","8","9"]
    assert tictactoe(table_ttt) == 0

def test_player_one_won_in_principal_diagonal():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["x","2","3","4","x","6","7","8","x"]
    assert tictactoe(table_ttt) == 1
    
def test_player_one_won_in_second_diagonal():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["1","2","x","4","x","6","x","8","9"]
    assert tictactoe(table_ttt) == 1

def test_player_one_won_in_firts_row():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["x","x","x","4","5","6","7","8","9"]
    assert tictactoe(table_ttt) == 1
    
def test_player_one_won_in_second_row():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["1","2","3","x","x","x","7","8","9"]
    assert tictactoe(table_ttt) == 1

def test_player_one_won_in_third_row():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["1","2","3","4","5","6","x","x","x"]
    assert tictactoe(table_ttt) == 1

def test_player_one_won_in_firts_column():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["x","2","3","x","5","6","x","8","9"]
    assert tictactoe(table_ttt) == 1
    
def test_player_one_won_in_second_column():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["1","x","3","4","x","6","7","x","9"]
    assert tictactoe(table_ttt) == 1
    
def test_player_one_won_in_third_column():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["1","2","x","4","5","x","7","8","x"]
    assert tictactoe(table_ttt) == 1

#####################

def test_player_two_won_in_principal_diagonal():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["o","2","3","4","o","6","7","8","o"]
    assert tictactoe(table_ttt) == 2
    
def test_player_two_won_in_second_diagonal():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["1","2","o","4","o","6","o","8","9"]
    assert tictactoe(table_ttt) == 2

def test_player_two_won_in_firts_row():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["o","o","o","4","5","6","7","8","9"]
    assert tictactoe(table_ttt) == 2
    
def test_player_two_won_in_second_row():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["1","2","3","o","o","o","7","8","9"]
    assert tictactoe(table_ttt) == 2

def test_player_two_won_in_third_row():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["1","2","3","4","5","6","o","o","o"]
    assert tictactoe(table_ttt) == 2

def test_player_two_won_in_firts_column():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["o","2","3","o","5","6","o","8","9"]
    assert tictactoe(table_ttt) == 2
    
def test_player_two_won_in_second_column():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["1","o","3","4","o","6","7","o","9"]
    assert tictactoe(table_ttt) == 2
    
def test_player_two_won_in_third_column():
    #             0   1   2   3   4   5   6   7   8
    table_ttt = ["1","2","o","4","5","o","7","8","o"]
    assert tictactoe(table_ttt) == 2

