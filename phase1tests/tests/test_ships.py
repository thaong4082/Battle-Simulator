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
from specs.ships import Fighter, Destroyer, Cruiser, Battleship, Ship

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


if __name__ == '__main__':
    unittest.main()