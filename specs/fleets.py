from specs.exceptions import InvalidFleetException, InvalidModuleException
# from exceptions import InvalidFleetException, InvalidModuleException
from specs.ships import Fighter, Destroyer, Cruiser, Battleship
# from ships import Fighter , Destroyer, Cruiser, Battleship
import random
import os

class Fleet: 
  command_points = 0
  def __init__(self, userid):
    '''
    Creates a Fleet by reading in a matching text file in the fleets/ folder
    DO NOT CHANGE THIS FUNCTION.
    '''
    self.name = userid
    self.ships = []
    self.read_fleet_file()
    #self.command_points = 0

  def read_fleet_file(self):
    '''
    This function attempts to load a fleet file and ensures a fleet file is valid.
    '''
    # print('self.name:', self.name)
    self.command_points = 0

    #accessing the path to the parent directory then to the fleets file for it to read
    cwd = os.getcwd()
    parentdir = os.path.dirname(cwd)
    filepath = os.path.join(cwd,'fleets', self.name+'.txt')
    #print(filepath)
    # filepath below is used for personal testing
    #filepath = os.path.join(parentdir,'specs', self.name+'.txt')
    
    with open(filepath) as f:
      lines = f.readlines()
      for values in lines:
        #if the command points is within the range, then we would append the values of the ships and add command points
        if self.command_points <= 100 and self.command_points >= 0:
          if values[0] == 'F':
            self.ships.append(Fighter(values[2:-1]))
            self.command_points += 1
          elif values[0] == "D":
            self.ships.append(Destroyer(values[2:-1]))
            self.command_points += 2
          elif values[0] == "C":
            self.ships.append(Cruiser(values[2:-1]))
            self.command_points += 4
          elif values[0] == "B":
            self.ships.append(Battleship(values[2:-1]))
            self.command_points += 8

          #if it is an invalid ship type, raise an InvalidFleetException
          else:
            raise InvalidFleetException("Invalid ship type")
        #if we have more than 100 command points, then we raise an InvalidFleetException
        else:
          raise InvalidFleetException("Cannot have more than 100 command points")
      
      return self.ships
      
  def get_weapons(self, ship_type):
    '''
    Returns a list of all weapons in the fleet of ships that have not yet been destroyed and belong to the given ship type.
    '''
    # TODO Phase 2
    all_weapons = []
    self.counter = 0
    #if the weapons belong to the given ship type and are not destroyed, add to the all_weapons list
    for ship in self.ships:
      if isinstance(ship, ship_type) and self.ships[self.counter].hull != 0:
        for weapons in self.ships[self.counter].weapons:
          all_weapons.append(weapons)
      self.counter += 1
    return all_weapons
  
  def __str__(self):
    """
    Returns a string with the summary of a fleet.
    """
    stats = self.get_stats()
    string = "Fleet random\n=========================================================\nShips: " + str(stats["ships"]) + "/" + str(int(stats["total_ships"])) +  ", Command Points: " + str(int(stats["cost"])) + "/" + str(int(stats["total_cost"])) + "\nHull: " + str(int(stats["total_hull"])) + "/"+ str(int(stats["hull"]))+", Armor: " + str(int(stats["armor"])) + "/" + str(int(stats["total_armor"])) + ", Shields: " + str(int(stats["shields"])) + "/" + str(int(stats["total_shields"]))

    return string
    
  def get_stats(self):
    """
    Returns a dictionary with the fleets most important values.
    """
    # TODO: Phase 2
    stats = {
      "cost": 0,
      "ships": 0,
      "hull": 0,
      "armor": 0,
      "shields": 0,
      "total_cost": 0,
      "total_ships": 0,
      "total_hull": 1, # 1 just to avoid an initial div/0 error
      "total_armor": 1,
      "total_shields": 1,
      "damage_taken": 0
    }
    
    total_ships = len(self.ships)
    stats["total_ships"] = total_ships
    ships = 0
    total_hull = 0
    total_armor = 0
    total_shields = 0
    cost = 0
    hull = 0
    armor = 0
    shields = 0
    damage_taken = 0
    #going through the ships and its attributes for the total
    for i in range(len(self.ships)):
      total_hull += self.ships[i].max_hull
      total_armor += self.ships[i].max_armor
      total_shields += self.ships[i].max_shields
      if self.ships[i].hull != 0:
        ships += 1
        cost += self.ships[i].cost
        hull += self.ships[i].hull
        armor += self.ships[i].armor
        shields += self.ships[i].shields
    #changing the values fo the dictionary
    stats["total_cost"] = self.command_points
    stats["total_hull"] = total_hull
    stats["total_armor"] = total_armor  
    stats["total_shields"] = total_shields
    stats["ships"] = ships
    stats["cost"] = cost
    stats["hull"] = hull
    stats["armor"] = armor      
    stats["shields"] = shields
    
    damage_taken = ((total_armor + total_shields + total_hull) - (armor + shields + hull))

    stats["damage_taken"] = damage_taken
    
    return stats
    
  def list_ships(self):
    # DO NOT CHANGE THIS METHOD
    print("T |  H   |  A   |  S   |  PD  |  E   | DPS |")
    print("==|======|======|======|======|======|=====|")
    for ship in self.ships:
      print(ship)

def create_random_fleet():
  """
  This function will update `random.txt` with a new, randomly composed fleet.
  DO NOT CHANGE THIS FUNCTION
  """
  file = open("fleets/random.txt", "w")
  s = ""

  cp = 0
  while(cp != 100):
    # create random ship type
    type = random.choice("FFFFDDDCCB")

    # if ship type would exceed command points try again, 
    # otherwise increase command points and fill ship with modules
    if type == 'B' and cp + 8 > 100:
      continue
    elif type == 'B':
      cp += 8
      s += "B " + random_weapon_modules(4) + random_defense_modules(3) + "\n"
    elif type == 'C' and cp + 4 > 100:
      continue
    elif type == 'C':
      cp += 4
      s += "C " + random_weapon_modules(3) + random_defense_modules(2) + "\n"
    elif type == 'D' and cp + 2 > 100:
      continue
    elif type == 'D':
      cp += 2
      s += "D " + random_weapon_modules(2) + random_defense_modules(1) + "\n"
    elif type == 'F':
      cp += 1
      s += "F " + random_weapon_modules(1) + "\n"

  file.write(s)
  file.close()


def random_weapon_modules(count):
  # DO NOT CHANGE THIS FUNCTION
  s = ""
  while len(s) < count:
    s += random.choice("RLT")
  return s

def random_defense_modules(count):
  # DO NOT CHANGE THIS FUNCTION
  s = ""
  while len(s) < count:
    module = random.choice("SAEP")
    if module == "E" and "E" in s:
      continue
    s += module
  return s
