
def tictatoe(plays):
    
    alter_player = True
    player_one = 1
    player_two = 2
    count = 0

    while(count < 8):
    
       
        if (alter_player == True):
            
            alter_player = False
            
            if (plays[count] == "x") or (plays[count] == "o"):
                count = count + 1
                alter_player = True
            else:
                play_of_player_one = int(plays[count])
                play_of_player_one = play_of_player_one - 1
                plays[play_of_player_one] = "x"
        
        else:
        
            alter_player = True
            
        
            if (plays[count] == "x") or (plays[count] == "o"):
                count = count + 1
                alter_player = False
            else:
                
                play_of_player_two = int(plays[count])
                play_of_player_two = play_of_player_two - 1
                plays[play_of_player_two] = "o"
            
      
        if ((plays[0] == "x") and (plays[4] == "x") and (plays[8] == "x")):
            return player_one
        
        if ((plays[0] == "o") and (plays[4] == "o") and (plays[8] == "o")):
            return player_two
        
        count = count + 1 
    
    print(plays)
    
    return 0

plays = [2,1,3,5,6,9,4,7,8]

tictatoe(plays)