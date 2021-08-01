from random import randint
import time
from Equipment import equipment

class char_battle:
    def __init__(self, beast, character):
        self.beast= beast
        self.character= character

    
    def battleround(self):
        time.sleep(1.5)
        print(self.character.Char_name+" Your inventory contains: ",self.character.equip)
        time.sleep(2)
        use=input("Do you wish to use any of these? (Y/N)")
        if use=="Y":
         item_used=input("...which one will you use..? ")   
         EQU=equipment(self.character)
         EQU.Eq_used(item_used)
    
        while ((self.beast.health>0) & (self.character.health >0)):
                time.sleep(1)
                move= input("...Do you raise your weapon or do you stand still??? (ATTACK or DEFENCE ?) ")
                monmove=randint(1, 2)# if 1 it attacks you if 2 it defends itself
                if move=="ATTACK":
                   if monmove==1:
                       self.character.health=self.character.health-self.beast.attack
                       self.beast.health=self.beast.health-self.character.attack
                       if self.beast.health<=0:
                           self.beast.health=0
                       print("...you hit the foul beast but it hits you back...")
                       time.sleep(1.5)
                       print("\n Hero's Health is :",self.character.health)
                       print("\n Beast's Health is :",self.beast.health)
                       time.sleep(1.5)
                   elif monmove==2:
                       self.beast.health=self.beast.health-((self.character.attack-self.beast.defence) if (self.beast.defence<=self.character.attack) else 0)
                       self.character.health=self.character.health
                       if self.beast.health<=0:
                           self.beast.health=0
                       print("...you hit the foul beast and it defends itself...")
                       time.sleep(1.5)
                       print("\n Hero's Health is :",self.character.health)
                       print("\n Beast's Health is :",self.beast.health)   
                       time.sleep(1.5)
                elif move=="DEFENCE":
                   if monmove==1:
                       self.character.health=self.character.health-((self.beast.attack-self.character.defence) if (self.beast.attack>=self.character.defence) else 0)
                       self.beast.health=self.beast.health
                       if self.beast.health<=0:
                           self.beast.health=0
                       print("...you defend yourself while the beast hits you...")
                       time.sleep(1.5)
                       print("\n Hero's Health is :",self.character.health)
                       print("\n Beast's Health is :",self.beast.health)  
                       time.sleep(1.5)
                   elif monmove==2:
                       self.beast.health=self.beast.health
                       self.character.health=self.character.health
                       print("...you defend yourself and the beast does the same...")
                       time.sleep(1.5)
                       print("\n Hero's Health is :",self.character.health)
                       print("\n Beast's Health is :",self.beast.health)
                       time.sleep(1.5)
        print("YOU HAVE DEFEATED THE EVIL.....for now...")
    