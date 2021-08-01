import Beast
import Battle
import Items
from random import randint
import time


def Game_Round(player):
 for _ in range(3): #this dungeon has 3 rounds
     round_action = randint(1, 5)
     if(round_action==1 or round_action==4 or round_action==5):
        time.sleep(2) 
        print("\n ....you moved deeper into the forrest....\n")
        Items.items_found(player)
     elif(round_action==3 or round_action==2):
        print("\n You found a monster!\n")
        enemyx=Beast.enemy(randint(1,3)) 
        enemyx.Beast_atr()
        time.sleep(1.5)
        print(enemyx.name,"\n Attack is: ",enemyx.attack,"\n Defence is: ",enemyx.defence,"\n Health is: ",enemyx.health)
        time.sleep(3)
        battlex=Battle.char_battle(enemyx,player)
        battlex.battleround() 


