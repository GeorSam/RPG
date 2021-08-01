class equipment():
   def __init__(self,player):
       self.player=player
       
   def invent(self,item):
        if len(self.player.equip)<5:
         self.player.equip.append(item) 
         if item=="HELMET":
           self.player.defence=self.player.defence*1.2   
        elif self.player.equip.len==5:
         print("Your bag is full")  
         
   def Eq_used(self,item_used):
        if item_used in self.player.equip:
           if item_used == "SWORD" and self.player.Char_race=="HUMAN":
               self.player.attack=self.player.attack*1.5
           elif item_used == "SWORD" and self.player.Char_race=="ELF":
               self.player.attack=self.player.attack*1.3
           elif item_used == "SWORD" and self.player.Char_race=="DWARF":
               self.player.attack=self.player.attack*1.2
           elif item_used == "BOW" and self.player.Char_race=="HUMAN":
               self.player.attack=self.player.attack*1.2
           elif item_used == "BOW" and self.player.Char_race=="ELF":
               self.player.attack=self.player.attack*1.5
           elif item_used == "BOW" and self.player.Char_race=="DWARF":
               self.player.attack=self.player.attack*1.05
           elif item_used == "HAMMER" and self.player.Char_race=="HUMAN":
               self.player.attack=self.player.attack*1.2
           elif item_used == "HAMMER" and self.player.Char_race=="ELF":
               self.player.attack=self.player.attack*1.05
           elif item_used == "HAMMER" and self.player.Char_race=="DWARF":
               self.player.attack=self.player.attack*1.5   
           elif item_used == "SHIELD" and self.player.Char_race=="HUMAN":
               self.player.defence=self.player.defence*1.1
           elif item_used == "SHIELD" and self.player.Char_race=="ELF":
               self.player.defence=self.player.defence*1.1
           elif item_used == "SHILED" and self.player.Char_race=="DWARF":
               self.player.defence=self.player.defence*1.2 
        if item_used in self.player.equip and item_used=="HELMET":
               self.player.defence=self.player.defence*1.2            