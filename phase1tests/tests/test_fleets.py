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
from specs.fleets import Fleet
from specs.ships import Fighter, Destroyer, Cruiser, Battleship

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


if __name__ == '__main__':
    unittest.main()