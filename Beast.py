class enemy:
    def __init__(self, beast_number):
        self.beast_number=beast_number
        self.attack=0
        self.defence=0
        self.health=10
        self.name="NONE"
    def Beast_atr(self):
        if(self.beast_number==1):
           self.name= "ORC"
           self.attack= 3
           self.defence=6
        elif(self.beast_number==2):
           self.name="WOLF"
           self.attack= 2
           self.defence=4
        elif(self.beast_number==3):
           self.name= "TROLL"
           self.attack= 5
           self.defence=5