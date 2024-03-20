
def tictactoe(table_tictactoe):
    
    player_one = 1
    player_two = 2
    count = 0
    players = True
    
    while(count < 8): 
    
        if players == True:
            data_entry = input("Player " + str(player_one) + ": ")
            players = False
        else:
            data_entry = input("Player " + str(player_two) + ": ")
            players = True
        
        table_tictactoe[count] = data_entry
        
        print(" +=====+=====+=====+\n |  "+table_tictactoe[0]+"  |  "+table_tictactoe[1]+"  |  "+table_tictactoe[2]+"  |\n +=====+=====+=====+ \n |  "+table_tictactoe[3]+"  |  "+table_tictactoe[4]+"  |  "+table_tictactoe[5]+"  |\n +=====+=====+=====+\n |  "+table_tictactoe[6]+"  |  "+table_tictactoe[7]+"  |  "+table_tictactoe[8]+"  |\n +=====+=====+=====+")
        
        '''
        firt if is the principal diagonal
        '''
        if ((table_tictactoe[0] == "x" or table_tictactoe[0] == "X") and (table_tictactoe[4] == "x" or table_tictactoe[4] == "X") and (table_tictactoe[8] == "x" or table_tictactoe[8] == "X")):
            return player_one
        
        if ((table_tictactoe[0] == "o" or table_tictactoe[0] == "O") and (table_tictactoe[4] == "o" or table_tictactoe[4] == "O") and (table_tictactoe[8] == "o" or table_tictactoe[8] == "O")):
            return player_two
        
        
        '''
        second if is the second diagonal
        '''
        if ((table_tictactoe[2] == "x" or table_tictactoe[2] == "X") and (table_tictactoe[4] == "x" or table_tictactoe[4] == "X") and (table_tictactoe[6] == "x" or table_tictactoe[6] == "X")):
            return player_one
        
        if ((table_tictactoe[2] == "o" or table_tictactoe[2] == "O") and (table_tictactoe[4] == "o" or table_tictactoe[4] == "O") and (table_tictactoe[6] == "o" or table_tictactoe[6] == "O")):
            return player_two
        
        '''
        third if is the firts column
        '''
        if ((table_tictactoe[0] == "x" or table_tictactoe[0] == "X") and (table_tictactoe[1] == "x" or table_tictactoe[1] == "X") and (table_tictactoe[2] == "x" or table_tictactoe[2] == "X")):
            return player_one
        
        if ((table_tictactoe[0] == "o" or table_tictactoe[0] == "O") and (table_tictactoe[1] == "o" or table_tictactoe[1] == "O") and (table_tictactoe[2] == "o" or table_tictactoe[2] == "O")):
            return player_two
        
        '''
        four if is the second column
        '''
        if ((table_tictactoe[3] == "x" or table_tictactoe[3] == "X") and (table_tictactoe[4] == "x" or table_tictactoe[4] == "X") and (table_tictactoe[5] == "x" or table_tictactoe[5] == "X")):
            return player_one
        
        if ((table_tictactoe[3] == "o" or table_tictactoe[3] == "O") and (table_tictactoe[4] == "o" or table_tictactoe[4] == "O") and (table_tictactoe[5] == "o" or table_tictactoe[5] == "O")):
            return player_two
        
        '''
        if #5 is the third column
        '''
        if ((table_tictactoe[6] == "x" or table_tictactoe[6] == "X") and (table_tictactoe[7] == "x" or table_tictactoe[7] == "X") and (table_tictactoe[8] == "x" or table_tictactoe[8] == "X")):
            return player_one
        
        if ((table_tictactoe[6] == "o" or table_tictactoe[6] == "O") and (table_tictactoe[7] == "o" or table_tictactoe[7] == "O") and (table_tictactoe[8] == "o" or table_tictactoe[8] == "O")):
            return player_two
        
        '''
        if #6 is the firts row
        '''
        if ((table_tictactoe[0] == "x" or table_tictactoe[0] == "X") and (table_tictactoe[3] == "x" or table_tictactoe[3] == "X") and (table_tictactoe[6] == "x" or table_tictactoe[6] == "X")):
            return player_one
        
        if ((table_tictactoe[0] == "o" or table_tictactoe[0] == "O") and (table_tictactoe[3] == "o" or table_tictactoe[3] == "O") and (table_tictactoe[6] == "o" or table_tictactoe[6] == "O")):
            return player_two
        
        
        '''
        if #7 is the second row
        '''
        if ((table_tictactoe[1] == "x" or table_tictactoe[1] == "X") and (table_tictactoe[4] == "x" or table_tictactoe[4] == "X") and (table_tictactoe[7] == "x" or table_tictactoe[7] == "X")):
            return player_one
        
        if ((table_tictactoe[1] == "o" or table_tictactoe[1] == "O") and (table_tictactoe[4] == "o" or table_tictactoe[4] == "O") and (table_tictactoe[7] == "o" or table_tictactoe[7] == "O")):
            return player_two
        
        '''
        if #8 is the third row
        '''
        if ((table_tictactoe[2] == "x" or table_tictactoe[2] == "X") and (table_tictactoe[5] == "x" or table_tictactoe[5] == "X") and (table_tictactoe[8] == "x" or table_tictactoe[8] == "X")):
            return player_one
        
        if ((table_tictactoe[2] == "o" or table_tictactoe[2] == "O") and (table_tictactoe[5] == "o" or table_tictactoe[5] == "O") and (table_tictactoe[8] == "o" or table_tictactoe[8] == "O")):
            return player_two

        count = count + 1

    return 0

table = ["1","2","3","4","5","6","7","8","9"]

tictactoe(table)
