from specs.weapons import Railgun, Laser, Torpedo
from specs.exceptions import InvalidModuleException
#from weapons import Railgun, Laser, Torpedo
#from exceptions import InvalidModuleException


class Ship:
  """
  Creates a ship with its' respective values for hull, armor, shields, max values of these, defense modules, weapons, and cost
  """
  def __init__(self, modules):
    self.modules = modules
    self.defense = 0
    self.evasion_count = 0
    self.evasion = self.calc_evasion()
    self.weapons = []
    
    base = self.calc_base()
    self.base = base
    self.hull = base
    self.armor = base
    self.shields = base
    self.max_hull = base
    self.max_armor = base
    self.max_shields = base
    self.pd = 0
    self.mod(modules)
    self.max_hull = self.hull 
    self.max_armor = self.armor
    self.max_shields = self.shields
    self.cost = self.calc_cost()
    
  def __str__(self):
    """
    String method to print the ship in a user-friendly way
    """
    if isinstance(self, Fighter):
      letter = "F"
    elif isinstance(self, Destroyer):
      letter = "D"
    elif isinstance(self, Cruiser):
      letter = "C"
    elif isinstance(self, Battleship):
      letter = "B"

    #accumulating the total damage and total cooldown in order to calcule DPS
    total_damage = 0
    total_cooldown = 0
    for i in range(len(self.weapons)):
      total_damage += self.weapons[i].damage
      total_cooldown += self.weapons[i].cooldown
      
    #for the number of weapons in that ship,( all damage values )/(all cooldown value)
    DPS = total_damage/total_cooldown

    #Making the string
    s = letter + " | " + str(self.max_hull) + " | " + str(int(self.max_armor)) + " | " + str(int(self.max_shields)) + " | " + str(int(self.pd *100)) + "%" + " | " + str(int(self.evasion*100)) + "%" + " | " + str(int(DPS))

    return s

  
  def calc_cost(self):
    """
    Assigning the cost to the ship depending on which type of ship it is
    """
    if isinstance(self, Fighter):
      return  1
    elif isinstance(self, Destroyer):
      return 2
    elif isinstance(self, Cruiser):
      return 4
    elif isinstance(self, Battleship):
      return 8

  def calc_acc(self):
    """
    Assigning the accuracy to the ship depending on which type of ship it is
    """
    if isinstance(self, Fighter):
      return  1
    elif isinstance(self, Destroyer):
      return 1
    elif isinstance(self, Cruiser):
      return 0.9
    elif isinstance(self, Battleship):
      return 0.8
      
  def calc_base(self):
    """
    Assigning the base value to the ship depending on which type of ship it is
    """
    if isinstance(self, Fighter):
      return 100
    elif isinstance(self, Destroyer):
      return  300
    elif isinstance(self, Cruiser):
      return 600
    elif isinstance(self, Battleship):
      return 1000

  def calc_evasion(self):
    """
    Assigning the evasion value to the ship depending on which type of ship it is
    """
    if isinstance(self, Fighter):
      return 0.8
    elif isinstance(self, Destroyer):
      return  0.4
    elif isinstance(self, Cruiser):
      return 0.2
    elif isinstance(self, Battleship):
      return 0.1
  
  def mod(self, modules):
    """
    Adding the defense modules and weapons to the ships
    """
    valid_mod = ["S", "A", "E", "P", "R", "L", "T"]
    defense_mod = ["S", "A", "E", "P"]
    weapon_mod = ["R", "L", "T"]

    #checking if letter is a valid letter
    #print(modules)
    for i in modules:
      if i not in valid_mod:
        raise InvalidModuleException("Invalid module type")
        
      # if letter is a defense type of module
      elif i in defense_mod:
        #if the ship is a fighter, raise an InvalidModuleException since they are not able to have defense module
        if isinstance(self, Fighter):
          raise InvalidModuleException("Fighter not able to have defense modules")
          #if the ship is a destroyer, apply the defense modules and update respective values
        elif isinstance(self, Destroyer):
          if self.defense >= 0 and self.defense < 1:
            if i == "S":
              self.shields = (self.base * 0.5) + self.shields
              self.defense += 1
            elif i == "A":
              self.armor = (self.base * 0.5) + self.armor
              self.defense += 1
            elif i == "E":
              if self.evasion_count < 1:
                self.evasion = self.evasion*2
                self.evasion_count += 1
                self.defense +=1
              else:
                #raise InvalidModuleException if the ship has more than one Ion Thruster Module
                raise InvalidModuleException("Ship cannot contain more than one Ion Thruster Module")
            elif i == "P":
              self.pd += 1/3  
          else:
            #raise InvalidModuleException when we reached the maximum defense modules 
            raise InvalidModuleException("Reached maximum defense modules")
            #if ship is a Cruiser, apply the defense modules and update respective values
        elif isinstance(self, Cruiser):
          if self.defense >= 0 and self.defense < 2:
            if i == "S":
              self.shields = (self.base * 0.5) + self.shields
              self.defense += 1
            elif i == "A":
              self.armor = (self.base * 0.5) + self.armor
              self.defense += 1
            elif i == "E":
              if self.evasion_count < 1:
                self.evasion = self.evasion*2
                self.evasion_count += 1
                self.defense +=1
              else:
              #raise InvalidModuleException if the ship has more than one Ion Thruster Module
                raise InvalidModuleException("Ship cannot contain more than one Ion Thruster Module")
            elif i == "P":
              self.pd += 1/3
          else:
            #raise InvalidModuleException when we reached the maximum defense modules 
            raise InvalidModuleException("Reached maximum defense modules")
            #if ship is a Battleship, apply the defense modules and update respective values
        elif isinstance(self, Battleship):
          if self.defense >= 0 and self.defense < 3:
            if i == "S":
              self.shields = (self.base * 0.5) + self.shields
              self.defense += 1
            elif i == "A":
              self.armor = (self.base * 0.5) + self.armor
              self.defense += 1
            elif i == "E":
              if self.evasion_count < 1:
                self.evasion = self.evasion*2
                self.evasion_count += 1
                self.defense +=1
              else:
             #raise InvalidModuleException if the ship has more than one Ion Thruster Module
                raise InvalidModuleException("Ship cannot contain more than one Ion Thruster Module")
            elif i == "P":
              self.pd += 1/3
          else:
            #raise InvalidModuleException when we reached the maximum defense modules 
            raise InvalidModuleException("Reached maximum defense modules")
            
      #if the letter is a weapon
      elif i in weapon_mod:
        #if ship is a Fighter, attach assigned weapon to ship
        if isinstance(self, Fighter):
          if len(self.weapons) == 0:
            if i == "R":
              self.weapons.append(Railgun(1, 1, self))
            elif i == "L":
              self.weapons.append(Laser(1, 1, self))
            elif i == "T":
              self.weapons.append(Torpedo(1, 2, self))
          else:
            #Figher is only allowed one weapon
            raise InvalidModuleException("Reached maximum number of allowed weapons")
            
        elif isinstance(self,Destroyer):
          #if ship is a Destroyer, attach assigned weapon to ship
          if len(self.weapons) >= 0 and len(self.weapons) < 2:
            if i == "R":
              self.weapons.append(Railgun(1,1, self))
            elif i == "L":
              self.weapons.append(Laser(1,1, self))
            elif i == "T":
              self.weapons.append(Torpedo(1,2, self))
          else:
            #Destroyer is only allowed 2 weapons
            raise InvalidModuleException("Reached maximum number of allowed weapons")
  
        elif isinstance(self, Cruiser):
          #if ship is a Cruiser, attach assigned weapon to ship
          if len(self.weapons) >= 0 and len(self.weapons) < 3:
            if i == "R":
              self.weapons.append(Railgun(1.2, 0.9, self))
            elif i == "L":
              self.weapons.append(Laser(1.2, 0.9, self))
            elif i == "T":
              self.weapons.append(Torpedo(1.2, 2, self))
          else:
            #Cruiser is only allowed 3 weapons
            raise InvalidModuleException("Reached maximum number of allowed weapons")
            
        elif isinstance(self, Battleship):
          #if ship is a Battleship, attach assigned weapon to ship
          if len(self.weapons) >= 0 and len(self.weapons) < 4:
            if i == "R":
              self.weapons.append(Railgun(1.5, 0.8, self))
            elif i == "L":
              self.weapons.append(Laser(1.5, 0.8, self))
            elif i == "T":
              self.weapons.append(Torpedo(1.5, 2, self))
          else:
            #Battleship is only allowed 4 weapons
            raise InvalidModuleException("Reached maximum number of allowed weapons")
            
class Fighter(Ship):
  def __init___(self, modules):
    self.dmg_modifier = 1
    super().__init__(modules)
    
class Destroyer(Ship):
  def __init___(self, modules):
    self.dmg_modifier = 1
    super().__init__(modules)
  
class Cruiser(Ship):
  def __init___(self, modules):
    self.dmg_modifier = 1.2
    super().__init__(modules)
    
class Battleship(Ship):
  def __init___(self, modules):   
    self.dmg_modifier = 1.5
    super().__init__(modules)
