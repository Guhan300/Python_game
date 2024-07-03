import random

score_player1=0
score_player2=0

for i in range(1,11):
    print("<=========  Round-%d  =========>"%i)
    player1_input=(input("Player-1:Enter to roll the dice"))
    player1_value=random.randint(1,6)
    print("player1:",player1_value)
    player2_input=(input("Player-2:Enter to roll the dice"))
    player2_value=random.randint(1,6)
    print("player2:",player2_value)
    
    if player1_value>player2_value:
        print("Player 1 won this round")   
        score_player1+=1
    elif player2_value>player1_value:
        print("Player 2 won this round")
        score_player2+=1
    else:
        print("This round is draw!")
        
if score_player1>score_player2:
    print("PLAYER-1 WON THE BATTLE :","Score:",score_player1)
else:
    print("PLAYER-2 WON THE BATTLE :","Score:",score_player2)
    
print("***Battle End***")
        
        
    
        
        
    
    
    
    