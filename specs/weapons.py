from random import random

class Weapon:
  def __init__(self, ship, accuracy, dmg_modifier):
    '''
    Base constructor for weapons
    '''
    self.ship = None
    self.target = None
    self.accuracy = accuracy
    self.damage = self.base_damage * dmg_modifier

    '''common attributes'''
      
  def fire(self, combat_round):
    '''
    First checks if a weapon is eligible for firing, otherwise do nothing (charge).
    
    Resolves a weapon applying damage to a specific target.

    If a hit would deduct more damage than the remaining shields the remaining damage of that specific shot is voided. E.g. A ship has 100 shields left. Your weapon made 150 damage. Instead of disabling the shields and doing 50 damage to the armor of the target it will only disable the shield. The next weapon hit will damage armor. Also make sure hull, armor and shields only go down to 0, not become negative values.
    '''
    # TODO Phase 2
    #checks if the weapon is eligible for firing, else do nothing
    self.combat_round = combat_round
    if self.target == None:
      return
    
    #if the weapon isn't in need of cooldown in order to shoot
    if self.combat_round % self.cooldown == 0:
      # if weapon is Torpedo, check whether it passed point defense
      if isinstance(self, Torpedo):
        #if it passed point defense
        if self.target.pd < random():
          #if the target still has some armor, damage it     
          if self.target.armor > 0:
            self.target.armor = max(0, self.target.armor - (self.damage * self.armor_modifier))
            return
          #if the target still has some hull, damage it
          elif self.target.hull > 0:
            self.target.hull = max(0, self.target.hull - (self.damage * self.hull_modifier))
            return

      #Taking evasion into account. If the target evasion is greater than random, then we ignore
      if random() < self.target.evasion:
        return

      #Taking the accuracy into account. If the accuracy is greater than random, ignore
      # print("what weapon? ", type(self))
      if random() > self.accuracy:
        return

      #if there are some shields left and is not a Torpedo, then we damage their shields
      if self.target.shields > 0:
        if not isinstance(self, Torpedo):
          self.target.shields = max(0, self.target.shields - (self.damage * self.shields_modifier))
          return
      #if there are some armor left and is not a Torpedo, then we damage their armor
      if self.target.armor > 0:
        if not isinstance(self, Torpedo):
          self.target.armor = max(0, self.target.armor - (self.damage * self.armor_modifier))
          return
          
      #if there are some hull left and is not a Torpedo, then we damage their armor    
      if self.target.hull > 0:
        self.target.hull = max(0, self.target.hull - (self.damage * self.hull_modifier))
      return

class Railgun(Weapon):
  def __init__(self, dmg_modifier, accuracy, ship):
    self.base_damage = 10
    self.cooldown = 1
    self.hull_modifier = 0.9
    self.armor_modifier = 0.4
    self.shields_modifier = 1.2
    super().__init__(ship, accuracy, dmg_modifier)

class Laser(Weapon):
  def __init__(self, dmg_modifier, accuracy, ship):
    self.base_damage = 60
    self.cooldown = 5
    self.hull_modifier = 1
    self.armor_modifier = 1.2
    self.shields_modifier = 0.4
    super().__init__(ship, accuracy, dmg_modifier)
    
class Torpedo(Weapon):
  def __init__(self, dmg_modifier, accuracy, ship):
    self.base_damage = 120
    self.cooldown = 15
    self.hull_modifier = 1.2
    self.armor_modifier = 1
    self.shields_modifier = None #dont affect shields
    super().__init__(ship, accuracy, dmg_modifier)
    
