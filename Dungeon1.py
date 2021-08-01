import Beast
import Battle
from random import randint



def Game_Round(player):
 for _ in range(3): #this dungeon has 3 rounds
     round_action = randint(1, 2)
     if(round_action==1):
        print("\n ....you moved deeper into the forrest.... \n")
     elif(round_action==2):
        print("\n You found a monster!\n")
        enemyx=Beast.enemy(randint(1,3)) 
        enemyx.Beast_atr()
        print(enemyx.name,"\n Attack is: ",enemyx.attack,"\n Defence is: ",enemyx.defence,"\n Health is: ",enemyx.health)
        battlex=Battle.char_battle(enemyx,player)
        battlex.battleround() 


