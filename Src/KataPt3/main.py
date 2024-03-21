

table_tictactoe = ["1","2","3","4","5","6","7","8","9"]

print("+===+===+===+")
print(f"| {table_tictactoe[0]} | {table_tictactoe[1]} | {table_tictactoe[2]} |")
print("+===+===+===+")
print(f"| {table_tictactoe[3]} | {table_tictactoe[4]} | {table_tictactoe[5]} |")
print("+===+===+===+")
print(f"| {table_tictactoe[6]} | {table_tictactoe[7]} | {table_tictactoe[8]} |")
print("+===+===+===+")

def tictactoe(table):
    counter = 0
    select_position = 0
    alter_player = True
    
    while(counter < 8):
        
        if (alter_player == True):
            
            select_position = int(input("Selecciona la posicion en la que quieres jugar: "))
            select_position = select_position - 1
            table[select_position] = "x"
            alter_player = False
        else:
            
            select_position = int(input("Selecciona la posicion en la que quieres jugar: "))
            select_position = select_position - 1
            table[select_position] = "o"
            alter_player = True
        
        print("+===+===+===+")
        print(f"| {table[0]} | {table[1]} | {table[2]} |")
        print("+===+===+===+")
        print(f"| {table[3]} | {table[4]} | {table[5]} |")
        print("+===+===+===+")
        print(f"| {table[6]} | {table[7]} | {table[8]} |")
        print("+===+===+===+")

        
        
        #region Logic_of_player_X
        # principal diagonal X
        if ((table[0] == "x" or table[0] == "X") and (table[4] == "x" or table[4] == "X") and (table[8] == "x" or table[8] == "X")):
            return 1
        
        # Second diagonal X
        if ((table[2] == "x" or table[2] == "X") and (table[4] == "x" or table[4] == "X") and (table[6] == "x" or table[6] == "X")):
            return 1
        
        #firts row X
        if ((table[0] == "x" or table[0] == "X") and (table[1] == "x" or table[1] == "X") and (table[2] == "x" or table[2] == "X")):
            return 1
        
        #Second row X
        if ((table[3] == "x" or table[3] == "X") and (table[4] == "x" or table[4] == "X") and (table[5] == "x" or table[5] == "X")):
            return 1
        
        #Third row X
        if ((table[6] == "x" or table[6] == "X") and (table[7] == "x" or table[7] == "X") and (table[8] == "x" or table[8] == "X")):
            return 1
    
        #Firts column X
        if ((table[0] == "x" or table[0] == "X") and (table[3] == "x" or table[3] == "X") and (table[6] == "x" or table[6] == "X")):
            return 1
    
        #Second column X
        if ((table[1] == "x" or table[1] == "X") and (table[4] == "x" or table[4] == "X") and (table[7] == "x" or table[7] == "X")):
            return 1
    
        #Third column X
        if ((table[2] == "x" or table[2] == "X") and (table[5] == "x" or table[5] == "X") and (table[8] == "x" or table[8] == "X")):
            return 1
        
        #endregion
        
        #region Logic of Player_O
        
        # principal diagonal O
        if ((table[0] == "o" or table[0] == "O") and (table[4] == "o" or table[4] == "O") and (table[8] == "o" or table[8] == "O")):
            return 2
        
        # Second diagonal O
        if ((table[2] == "o" or table[2] == "O") and (table[4] == "o" or table[4] == "O") and (table[6] == "o" or table[6] == "O")):
            return 2
        
        #firts row O
        if ((table[0] == "o" or table[0] == "O") and (table[1] == "o" or table[1] == "O") and (table[2] == "o" or table[2] == "O")):
            return 2
        
        #Second row O
        if ((table[3] == "o" or table[3] == "O") and (table[4] == "o" or table[4] == "O") and (table[5] == "o" or table[5] == "O")):
            return 2
        
        #Third row O
        if ((table[6] == "o" or table[6] == "O") and (table[7] == "o" or table[7] == "O") and (table[8] == "o" or table[8] == "O")):
            return 2
    
        #Firts column O
        if ((table[0] == "o" or table[0] == "O") and (table[3] == "o" or table[3] == "O") and (table[6] == "o" or table[6] == "O")):
            return 2
    
        #Second column O
        if ((table[1] == "o" or table[1] == "O") and (table[4] == "o" or table[4] == "O") and (table[7] == "o" or table[7] == "O")):
            return 2
    
        #Third column O
        if ((table[2] == "o" or table[2] == "O") and (table[5] == "o" or table[5] == "O") and (table[8] == "o" or table[8] == "O")):
            return 2
        
        #endregion 
        
        counter = counter + 1

    return 0





tictactoe(table_tictactoe)
