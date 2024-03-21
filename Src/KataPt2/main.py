
def tictatoe(plays):
    
    alter_player = True
    player_one = 1
    player_two = 2
    select_position = 0
    count = 0

    while(select_position < 9):
    
       
        if (alter_player == True):
            alter_player = False
            select_position = positions[0]
            plays[select_position] = "x"
            select_position = select_position + 1
        else:
            alter_player = True
            plays[select_position] = "o"
            select_position = select_position + 1
        
        print(plays)
        if ((plays[0] == "x") and (plays[4] == "x") and (plays[8] == "x")):
            return player_one
        
        if ((plays[0] == "o") and (plays[4] == "o") and (plays[8] == "o")):
            return player_two
        
        count = count + 1 
    
    
    return 0

plays = ["2","1","3","5","6","9","4","7","8"]

tictatoe(plays)