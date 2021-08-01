from random import randrange

class ch:
    def __init__(self, Char_name, Char_race):
        self.Char_name= Char_name
        self.Char_race= Char_race
        self.attack=0
        self.defence=0
        self.health=100
        self.equip= []
        
    def Attributes(self):
        if(self.Char_race=="HUMAN"):
           self.attack=randrange(3,7)
           self.defence=6
        elif(self.Char_race=="ELF"):
           self.attack= randrange(4,8)
           self.defence=4
        elif(self.Char_race=="DWARF"):
           self.attack= randrange(3,5)
           self.defence=8

               
               
               
               
               
               
               