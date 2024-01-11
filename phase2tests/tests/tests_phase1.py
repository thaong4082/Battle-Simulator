import sys
import os
# getting the current directory
current = os.getcwd()
# Getting the parent directory name
parent = os.path.dirname(os.path.dirname(current))
# adding the parent directory to the sys.path.
sys.path.append(parent)
#########################################

import unittest
from specs.fleets import Fleet#, InvalidFleetException, InvalidModuleException
from specs.ships import Fighter, Destroyer, Cruiser, Battleship, Ship
from specs.weapons import Railgun, Laser, Torpedo, Weapon

class TestShips(unittest.TestCase):

  def setUp(self):
    self.f1 = Fighter("R")
    self.d1 = Destroyer("RLS")
    self.d2 = Destroyer("LRA")
    self.d3 = Destroyer("TTE")
    self.c1 = Cruiser("RLTPE")
    self.c2 = Cruiser("RRRAS")
    self.b1 = Battleship("RRRRPPE")
    self.b2 = Battleship("RRRRPPP")
    self.b3 = Battleship("RRRRAAS")

  def test_inheritance(self):
    """ Testing Ship Inheritance
    """
    self.assertTrue(isinstance(self.f1, Fighter), "Fighters must use the Fighter class.")
    self.assertTrue(isinstance(self.d1, Destroyer), "Destroyers must use the Destroyer class.")
    self.assertTrue(isinstance(self.c1, Cruiser), "Cruisers must use the Cruiser class.")
    self.assertTrue(isinstance(self.b1, Battleship), "Battleships must use the Battleship class.")

    self.assertTrue(isinstance(self.f1, Ship), "Fighters must inherit from the Ship class.")
    self.assertTrue(isinstance(self.d1, Ship), "Destroyers must inherit from the Ship class.")
    self.assertTrue(isinstance(self.c1, Ship), "Cruisers must inherit from the Ship class.")
    self.assertTrue(isinstance(self.b1, Ship), "Battleships must inherit from the Ship class.")

  def test_evasion(self):
    """ Testing base evasion
    """
    self.assertEqual(self.f1.evasion, 0.8, "Fighters should have a base evasion of 0.8.")
    self.assertEqual(self.d1.evasion, 0.4, "Destroyers should have a base evasion of 0.4.")
    self.assertEqual(self.c2.evasion, 0.2, "Cruisers should have a base evasion of 0.2.")
    self.assertEqual(self.b3.evasion, 0.1, "Battleships should have a base evasion of 0.1.")

  def test_cost(self):
    """ Testing command points (cost)
    """
    self.assertEqual(self.f1.cost, 1, "Fighters should have a cost of 1.")
    self.assertEqual(self.d1.cost, 2, "Destroyers should have a cost of 2.")
    self.assertEqual(self.c1.cost, 4, "Cruisers should have a cost of 4.")
    self.assertEqual(self.b1.cost, 8, "Battleships should have a cost of 8.")

  def test_max_attributes(self):
    """ Testing * vs max_*
    """
    for ship in [self.f1, self.d1, self.d2, self.d3]:
      self.assertEqual(ship.max_shields, ship.shields, \
        "On newly created ships, both max_shields and shields should be the same.")
      self.assertEqual(ship.max_shields, ship.shields, \
        "On newly created ships, both max_armor and armor should be the same.")
      self.assertEqual(ship.max_shields, ship.shields, \
        "On newly created ships, both max_hull and hull should be the same.")

  def test_pd(self):
    """ Testing point defense
    """
    self.assertEqual(self.f1.pd, 0, "0 point defense modules should result in 0 pd.")
    self.assertEqual(self.c1.pd, 1/3, "1 point defense modules should result in 1/3 pd.")
    self.assertEqual(self.b1.pd, 2/3, "2 point defense modules should result in 2/3 pd.")
    self.assertEqual(self.b2.pd, 1/1, "3 point defense modules should result in 3/3 pd.")

  def test_fighter(self):
    """ Testing Fighter Ships
    """
    self.assertEqual(self.f1.max_hull, 100, "A fighter's hull should be 100.")
    self.assertEqual(self.f1.max_armor, 100, "A fighter's armor should be 100.")
    self.assertEqual(self.f1.max_shields, 100, "A fighter's shields should be 100.")

  def test_destroyer(self):
    """ Testing Destroyer Ships
    """
    self.assertEqual(self.d1.max_hull, 300, "Destroyer(RLS) hull should be 300.")
    self.assertEqual(self.d1.max_armor, 300, "Destroyer(RLS) armor should be 300.")
    self.assertEqual(self.d1.max_shields, 450, "Destroyer(RLS) shields should be 450.")

    self.assertEqual(self.d2.max_hull, 300, "Destroyer(RLS) hull should be 300.")
    self.assertEqual(self.d2.max_armor, 450, "Destroyer(RLS) armor should be 450.")
    self.assertEqual(self.d2.max_shields, 300, "Destroyer(RLS) shields should be 300.")

    self.assertEqual(self.d3.max_hull, 300, "Destroyer(TTE) hull should be 300.")
    self.assertEqual(self.d3.max_armor, 300, "Destroyer(TTE) armor should be 300.")
    self.assertEqual(self.d3.max_shields, 300, "Destroyer(TTE) shields should be 300.")
    self.assertEqual(self.d3.evasion, 0.8, "Destroyer(TTE) evasion should be 0.8.")

  def test_cruiser(self):
    """ Testing Cruiser Ships
    """
    self.assertEqual(self.c1.max_hull, 600, "Cruiser(RLTPE) hull should be 600.")
    self.assertEqual(self.c1.max_armor, 600, "Cruiser(RLTPE) armor should be 600.")
    self.assertEqual(self.c1.max_shields, 600, "Cruiser(RLTPE) shields should be 600.")
    self.assertEqual(self.c1.evasion, 0.4, "Cruiser(RLTPE) evasion should be 0.4.")

    self.assertEqual(self.c2.max_hull, 600, "Cruiser(RRRAS) hull should be 600.")
    self.assertEqual(self.c2.max_armor, 900, "Cruiser(RRRAS) armor should be 900.")
    self.assertEqual(self.c2.max_shields, 900, "Cruiser(RRRAS) shields should be 900.")
    self.assertEqual(self.c2.pd, 0.0, "Cruiser(RRRAS) pd should be 0.0.")

  def test_battleships(self):
    """ Testing Battle Ships
    """
    self.assertEqual(self.b1.max_hull, 1000, "Battleship(RRRRPPE) hull should be 1000.")
    self.assertEqual(self.b1.max_armor, 1000, "Battleship(RRRRPPE) armor should be 1000.")
    self.assertEqual(self.b1.max_shields, 1000, "Battleship(RRRRPPE) shields should be 1000.")
    self.assertEqual(self.b1.evasion, 0.2, "Battleship(RRRRPPE) evasion should be 0.2.")
    self.assertEqual(self.b1.pd, 2/3, "Battleship(RRRRPPE) pd should be 2/3.")

    self.assertEqual(self.b2.max_hull, 1000, "Battleship(RRRRPPP) hull should be 1000.")
    self.assertEqual(self.b2.max_armor, 1000, "Battleship(RRRRPPP) armor should be 1000.")
    self.assertEqual(self.b2.max_shields, 1000, "Battleship(RRRRPPP) shields should be 1000.")
    self.assertEqual(self.b2.evasion, 0.1, "Battleship(RRRRPPP) evasion should be 0.1.")
    self.assertEqual(self.b2.pd, 3/3, "Battleship(RRRRPPP) pd should be 3/3.")

    self.assertEqual(self.b3.max_hull, 1000, "Battleship(RRRRAAS) hull should be 1000.")
    self.assertEqual(self.b3.max_armor, 2000, "Battleship(RRRRAAS) armor should be 2000.")
    self.assertEqual(self.b3.max_shields, 1500, "Battleship(RRRRAAS) shields should be 1500.")
    self.assertEqual(self.b3.evasion, 0.1, "Battleship(RRRRAAS) evasion should be 0.1.")
    self.assertEqual(self.b3.pd, 0/3, "Battleship(RRRRAAS) pd should be 0/3.")

  def test_str_completeness(self):
    """ Testing Ship.__str__(self) completeness
    """
    s = self.b3.__str__()
    self.assertIn("1500", s, "A value is incorrectly formatted or not found.")
    self.assertIn("2000", s, "A value is incorrectly formatted or not found.")
    self.assertIn("1500", s, "A value is incorrectly formatted or not found.")
    self.assertIn("0%", s, "A value is incorrectly formatted or not found.")
    self.assertIn("10%", s, "A value is incorrectly formatted or not found.")
    self.assertIn("B", s, "A value is incorrectly formatted or not found.")
    self.assertIn("15", s, "A value is incorrectly formatted or not found.")

  def test_str_formatting(self):
    """ Testing Ship.__str__(self) formatting
    """
    self.assertEqual(self.f1.__str__(), self.f1.__str__(), "Formatting doesn't match.")
    self.assertEqual(self.d2.__str__(), self.d2.__str__(), "Formatting doesn't match.")
    self.assertEqual(self.c1.__str__(), self.c1.__str__(), "Formatting doesn't match.")
    self.assertEqual(self.b3.__str__(), self.b3.__str__(), "Formatting doesn't match.")


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

class TestFleets(unittest.TestCase):
  def setUp(self):
    self.fleet = Fleet("random")

  def test_configuration(self):
    """ Testing read_fleet_file() basics
    """
    fleet = self.fleet
    self.assertEqual(fleet.name, "random", "Fleet name attribute incorrect or missing.")
    self.assertTrue(isinstance(fleet.ships, list), "Ships must be stored as a Python list.")
    self.assertEqual(len(fleet.ships), 45, "Incorrect number of ships was created.")

  def test_composition(self):
    """ Testing read_fleet_file() composition
    """
    f = 0
    d = 0
    c = 0
    b = 0

    for ship in self.fleet.ships:
      if isinstance(ship, Fighter):
        f += 1
      elif isinstance(ship, Destroyer):
        d += 1
      elif isinstance(ship, Cruiser):
        c += 1
      elif isinstance(ship, Battleship):
        b += 1

    self.assertEqual(f, 20, f"Our test fleet had 20 Fighters, we encounterd {f} in yours.")
    self.assertEqual(d, 14, f"Our test fleet had 14 Destroyers, we encounterd {d} in yours.")
    self.assertEqual(c, 9, f"Our test fleet had 9 Cruisers, we encounterd {c} in yours.")
    self.assertEqual(b, 2, f"Our test fleet had 2 Battleships, we encounterd {b} in yours.")

class TestExceptions(unittest.TestCase):

  def test_unknown_module(self):
    """ Testing Exception (invalid module count)
    """
    with self.assertRaises(InvalidModuleException):
      Fleet("invalid_module_count")
    with self.assertRaises(InvalidModuleException):
      Fleet("invalid_module_count2")
    with self.assertRaises(InvalidModuleException):
      Fleet("invalid_module_count3")

  def test_unknown_ship(self):
    """ Testing Exception (unknown modules)
    """
    with self.assertRaises(InvalidModuleException):
      Fleet("invalid_module_type")

  def test_evasion(self):
    """ Testing Exception (>1 evasion modules)
    """
    with self.assertRaises(InvalidModuleException):
      Fleet("invalid_evasion")

  def test_invalid_fleet1(self):
    """ Testing Exception (invalid ship type)
    """
    with self.assertRaises(InvalidFleetException):
      Fleet("invalid2")

  def test_invalid_fleet2(self):
    """ Testing Exception (100 command point limit)
    """
    with self.assertRaises(InvalidFleetException):
      Fleet("invalid")

if __name__ == '__main__':
    unittest.main()