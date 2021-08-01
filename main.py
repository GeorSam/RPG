import Charselection
import Path1
import Path2
import time

name= input("Select Character name: ")

while True:
 race= input("Select Character race (character race can be HUMAN,ELF, DWARF): ")
 if race=="HUMAN" or race=="ELF" or race=="DWARF":
  break 
 else:
  continue


char1= Charselection.ch(name,race)
char1.Attributes()
time.sleep(2)
print("\n \n ...Our hero... "+char1.Char_name+" ...rests in the tavern as he hears whispers of a treasure...")
time.sleep(1)
print("\n \n ...they speak of a chest full of gold inside a cave in the forrest....")
time.sleep(1)
print("\n \n ...you decide to take on an adventure!!!")
time.sleep(2)
print("\n Your race's characteristics are",char1.Char_race,"\n Attack is: ",char1.attack,"\n Defence is: ",char1.defence,"\n Health is: ",char1.health)


time.sleep(3)
path_selction_1=input("...as you begin your journey....2 paths uveil in front of you \n into the Dark Forrest..\n....which path do you choose mighty traveller ?? :(LEFT/RIGHT) ")
time.sleep(2)


if path_selction_1=="LEFT":
 Path2.Game_Round(char1)
elif path_selction_1=="RIGHT":
 Path1.Game_Round(char1)
 
time.sleep(1.5)

print("\n CONGRADULATIONS YOU FOUND THE TRESURE....") 
time.sleep(1.5)
print(char1.Char_name+" You end your journey with: ",char1.health,"..HP") 
time.sleep(1.5)
print("\n",char1.Char_name+" Your inventory contains one beautifull GEM and: ",char1.equip)
time.sleep(1.5)



