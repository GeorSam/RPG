import Beast
import Battle
from random import randint
import time


def Game_Round(player):
 for _ in range(4): #this dungeon has 3 rounds
     round_action = randint(1, 2)
     item_action = randint(1,2)
     if(round_action==1):
        time.sleep(2) 
        print("\n ....you moved deeper into the forrest....\n")
        if(item_action==1):
         time.sleep(2)   
         print("\n ....you found a health potion....you gain 10 HP!\n")
         time.sleep(2)
         player.health=player.health+10
         time.sleep(2)
         print("\n Your Hero's Health is :",player.health)
         time.sleep(2)          
        elif(item_action==2):     
         time.sleep(2)
         print("\n You found a trap... you lose 10 HP!\n")    
         time.sleep(2)
         player.health=player.health-10    
         time.sleep(2)
         print("\n Your Hero's Health is :",player.health)
         time.sleep(2)
     elif(round_action==2):
        time.sleep(1.5) 
        print("\n You found a monster!\n")
        enemyx=Beast.enemy(randint(1,3)) 
        enemyx.Beast_atr()
        time.sleep(1.5)
        print(enemyx.name,"\n Attack is: ",enemyx.attack,"\n Defence is: ",enemyx.defence,"\n Health is: ",enemyx.health)
        time.sleep(1.5)
        battlex=Battle.char_battle(enemyx,player)
        battlex.battleround() 

