from random import randint
import time
from Equipment import equipment

def items_found(player):
      HeroEq=equipment(player) 
      item_action = randint(1,20)
      if (item_action==1 or item_action==10 or item_action==20):
        time.sleep(2)           
        print("\n ....you found a health potion....you gain 10 HP!\n")
        time.sleep(2)
        if (player.health+10)<100:
         player.health=player.health+10
        else:
         player.health=100   
        time.sleep(2)
        print("\n Your Hero's Health is :",player.health)
        time.sleep(2)          
      elif(item_action==2 or item_action==11 or item_action==19 ):
        time.sleep(2)
        print("\n You found a trap... you lose 10 HP!\n")    
        if (player.health-10)>0:
         player.health=player.health-10
        else:
         player.health=0
        time.sleep(2)
        print("\n Your Hero's Health is :",player.health)
        time.sleep(2)         
      elif(item_action==3 or item_action==12 or item_action==18):  
        time.sleep(2)           
        SW=input("\n ....you found a SWORD...do you wish to keep it?(Y/N) ")
        if (SW=="Y"):
         HeroEq.invent("SWORD")
        elif (SW=="N"):
         print("you leave the treasure...") 
        time.sleep(2)                 
      elif(item_action==4 or item_action==13 or item_action==17): 
        time.sleep(2)           
        BW=input("\n ....you found a BOW...do you wish to keep it?(Y/N) ")
        if (BW=="Y"):
         HeroEq.invent("BOW")
        elif (BW=="N"):
         print("you leave the treasure...") 
        time.sleep(2)           
      elif(item_action==5 or item_action==14 or item_action==9): 
        time.sleep(2)           
        SD=input("\n ....you found a SHIELD...do you wish to keep it?(Y/N) ")
        if (SD=="Y"):
         HeroEq.invent("SHIELD")
        elif (SD=="N"):
         print("you leave the treasure...") 
        time.sleep(2)                   
      elif(item_action==6 or item_action==15 or item_action==8): 
        time.sleep(2)           
        HAM=input("\n ....you found a HAMMER...do you wish to keep it?(Y/N) ")
        if (HAM=="Y"):
         HeroEq.invent("HAMMER")
        elif (HAM=="N"):
         print("you leave the treasure...") 
        time.sleep(2)          
      elif(item_action==7 or item_action==16):
        time.sleep(2)           
        H=input("\n ....you found a HELMET...do you wish to keep it?(Y/N) ")
        if (H=="Y"):
         HeroEq.invent("HELMET")
        elif (H=="N"):
         print("you leave the treasure...") 
        time.sleep(2)
     