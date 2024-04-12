
def tictactoe(table):
    
    if((table[0] == "x") and (table[4] == "x") and (table[8] == "x")):
        return 1
    
    if((table[0] == "o") and (table[4] == "o") and (table[8] == "o")):
        return 2
    
    
    return 0
