from ships import Fighter, Destroyer, Cruiser, Battleship, Ship
from weapons import Railgun, Laser, Torpedo
from fleets import *
# J = Fighter("A") #should say no defense allowed
# K = Destroyer("SSS")
# print(K.max_shields) # 450
# Y = Cruiser("EESSAAAA") 
# print(Y.max_shields) #900
# print(Y.evasion) #0.4
# print(Y.max_armor) #600 
# U = Destroyer("AASSE")
# print(U.max_armor) # should be 450
# print(U.max_shields) #should be 300
# print(U.evasion) #should be 0.4

#Y = Battleship("LLRT")
# print(Y.weapons) #should be list with objects in them
# print(Y.weapons[1].accuracy) #0.8
# print(Y.weapons[3].accuracy) #None 
# H = Fighter("R")
# print(H.weapons[0].accuracy) #1
## accuracy seems to work well

#print(Y.weapons[0].damage) #should be 90
# fleets = Fleet("random.txt")
# print(len(fleets.ships)) #good, list of objects
# print(fleets.name) # good
# print(fleets.ships) # good

#Y = Fighter("R")
#print(Y.cost)
## need to fix cost and add command points exception

## ask him about two test cases relating to 2000 vs 2500
## path file confusion
## is command points an accumulation of all ship points? relates to 
## 100 command points exception?
## Exceptions suppose to fleet. or ship. ?

# fleets = Fleet("mess") # testing exceptions
# fleets = Fleet("random")
# print(fleets.get_weapons(Fighter))

# fleet = Fleet("mess")
# weapons = fleet.get_weapons(Fighter)
# print(fleet.ships)
# print(len(weapons))
# print(weapons)