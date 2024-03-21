
def tictactoe(table):
    
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
    
    #endregion 
    return 0

