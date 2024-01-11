import sys
import os
# getting the current directory
current = os.getcwd()
# Getting the parent directory name
parent = os.path.dirname(os.path.dirname(current))
# adding the parent directory to the sys.path.
sys.path.append(parent)

import unittest
from specs.ships import Fighter, Destroyer, Cruiser, Battleship
from specs.weapons import Railgun, Laser, Torpedo, Weapon
class TestWeapons(unittest.TestCase):

  def setUp(self):
    self.f = Fighter("R")
    self.d = Destroyer("RLS")
    self.c = Cruiser("RLTPE")
    self.b = Battleship("RLLTPPE")

    self.fr = self.f.weapons[0]

    for weapon in self.d.weapons:
      if isinstance(weapon, Railgun):
        self.dr = weapon
      if isinstance(weapon, Laser):
        self.dl = weapon

    for weapon in self.c.weapons:
      if isinstance(weapon, Railgun):
        self.cr = weapon
      if isinstance(weapon, Laser):
        self.cl = weapon
      if isinstance(weapon, Torpedo):
        self.ct = weapon

    for weapon in self.b.weapons:
      if isinstance(weapon, Railgun):
        self.br = weapon
      if isinstance(weapon, Laser):
        self.bl = weapon
      if isinstance(weapon, Torpedo):
        self.bt = weapon

  def test_configuration(self):
    """ Testing weapon placement
    """
    self.assertTrue(isinstance(self.f.weapons, list), "Weapons must be stored as a Python list.")
    self.assertTrue(isinstance(self.d.weapons, list), "Weapons must be stored as a Python list.")
    self.assertTrue(isinstance(self.c.weapons, list), "Weapons must be stored as a Python list.")
    self.assertTrue(isinstance(self.b.weapons, list), "Weapons must be stored as a Python list.")

    self.assertEqual(len(self.f.weapons), 1, "Fighters must have exactly one weapon.")
    self.assertEqual(len(self.d.weapons), 2, "Destroyers must have exactly 2 weapons.")
    self.assertEqual(len(self.c.weapons), 3, "Cruisers must have exactly 3 weapons.")
    self.assertEqual(len(self.b.weapons), 4, "Battleships must have exactly 4 weapons.")

    r = 0
    l = 0
    t = 0
    for weapon in self.b.weapons:
      if isinstance(weapon, Railgun):
        r += 1
      if isinstance(weapon, Laser):
        l += 1
      if isinstance(weapon, Torpedo):
        t += 1

    self.assertEqual(r, 1, "Battleship(RLLTPPE) should have 1 Railgun.")
    self.assertEqual(l, 2, "Battleship(RLLTPPE) should have 2 Lasers.")
    self.assertEqual(t, 1, "Battleship(RLLTPPE) should have 1 Torpedo.")

  def test_inheritance(self):
    """ Testing weapon inheritance
    """
    self.assertTrue(isinstance(self.f.weapons[0], Railgun), \
      "Not using Railgun class when required in ships.")

    self.assertTrue(isinstance(self.d.weapons[1], Laser), \
      "Not using Laser class when required in ships.")

    self.assertTrue(isinstance(self.c.weapons[2], Torpedo), \
      "Not using Torpedo class when required in ships.")

    self.assertTrue(isinstance(self.f.weapons[0], Weapon), \
      "Railguns must inherit from the Weapon class.")
    self.assertTrue(isinstance(self.f.weapons[0], Weapon), \
      "Lasers must inherit from the Weapon class.")
    self.assertTrue(isinstance(self.f.weapons[0], Weapon), \
      "Torpedos must inherit from the Weapon class.")

  def test_stats(self):
    """ Testing weapon stats
    """
    railgun = self.fr
    # print(type(self.fr.ship))
    self.assertEqual(railgun.ship, self.f, "Weapon's ship attribute must reference the ship in which the weapon was built into.")
    self.assertEqual(railgun.target, None, "Weapons should be initialized with no target (None).")
    self.assertEqual(railgun.cooldown, 1, "A railgun's cooldown should be 1.")
    self.assertEqual(railgun.damage, 10.0, "A Fighter's railguns damage should be 10.0.")
    self.assertEqual(railgun.accuracy, 1.0, "A Fighter's railguns accuracy should be 1.0.")

    railgun = self.dr
    self.assertEqual(railgun.damage, 10.0, "A Destroyers's railguns damage should be 10.0.")
    self.assertEqual(railgun.accuracy, 1.0, "A Destroyers's railguns accuracy should be 1.0.")

    laser = self.dl
    self.assertEqual(laser.cooldown, 5, "A laser's cooldown should be 5.")
    self.assertEqual(laser.damage, 60.0, "A Destroyers's laser's damage should be 60.0.")
    self.assertEqual(laser.accuracy, 1.0, "A Destroyers's laser's accuracy should be 1.0.")

    railgun = self.cr
    self.assertEqual(railgun.damage, 10 * 1.2, "A Cruiser's railguns damage should be 12.0.")
    self.assertEqual(railgun.accuracy, 0.9, "A Cruiser's railguns accuracy should be 0.9.")

    laser = self.cl
    self.assertEqual(laser.damage, 60 * 1.2, "A Cruiser's laser's damage should be 72.0.")
    self.assertEqual(laser.accuracy, 0.9, "A Cruiser's laser's accuracy should be 0.9.")

    torpedo = self.ct
    self.assertEqual(torpedo.cooldown, 15, "A torpedo's cooldown should be 15.")
    self.assertEqual(torpedo.damage, 120 * 1.2, "A Cruiser's torpedo damage should be 144.")

    railgun = self.br
    self.assertEqual(railgun.damage, 10 * 1.5, "A Battleship's railguns damage should be 15.0.")
    self.assertEqual(railgun.accuracy, 0.8, "A Battleship's railguns accuracy should be 0.8.")

    laser = self.bl
    self.assertEqual(laser.damage, 60 * 1.5, "A Battleship's laser's damage should be 90.0.")
    self.assertEqual(laser.accuracy, 0.8, "A Battleship's laser's accuracy should be 0.8.")

    torpedo = self.bt
    self.assertEqual(torpedo.cooldown, 15, "A torpedo's cooldown should be 15.")
    self.assertEqual(torpedo.damage, 120 * 1.5, "A Battleship's torpedo damage should be 180.0.")


if __name__ == '__main__':
    unittest.main()