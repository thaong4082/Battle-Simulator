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
from specs.weapons import Railgun, Laser, Torpedo

class TestWeapons(unittest.TestCase):
  def test_211(self):
    """ Testing get_weapons(ship_type) for fighters
    """
    weapons = Fleet("random").get_weapons(Fighter)

    self.assertEqual(len(weapons), 20, "Our test fleet contains 20 fighters, thus the returning list should contain 20 weapons when calling fleet.get_weapons(Fighter)")

    r = 0
    t = 0
    l = 0
    o = 0

    for weapon in weapons:
      if isinstance(weapon, Railgun):
        r += 1
      elif isinstance(weapon, Laser):
        l += 1
      elif isinstance(weapon, Torpedo):
        t += 1
      else:
        o += 1

    self.assertEqual(r, 5, "Wrong number of Railguns when calling fleet.get_weapons()")
    self.assertEqual(l, 9, "Wrong number of Lasers when calling fleet.get_weapons()")
    self.assertEqual(t, 6, "Wrong number of Torpedos when calling fleet.get_weapons()")
    self.assertEqual(o, 0, "When calling fleet.get_weapons() you return objects that are not weapons.")

  def test_212(self):
    """ Testing get_weapons(ship_type) for all ships
    """
    fleet = Fleet("random")

    weapons = \
      fleet.get_weapons(Fighter) + \
      fleet.get_weapons(Destroyer) + \
      fleet.get_weapons(Cruiser) + \
      fleet.get_weapons(Battleship)


    self.assertEqual(len(weapons), 25 + 34 + 24, "Wrong number of weapons returned when calling fleet.get_weapons()")

    r = 0
    t = 0
    l = 0
    o = 0

    for weapon in weapons:
      if isinstance(weapon, Railgun):
        r += 1
      elif isinstance(weapon, Laser):
        l += 1
      elif isinstance(weapon, Torpedo):
        t += 1
      else:
        o += 1

    self.assertEqual(r, 25, "Wrong number of Railguns when calling fleet.get_weapons()")
    self.assertEqual(l, 34, "Wrong number of Lasers when calling fleet.get_weapons()")
    self.assertEqual(t, 24, "Wrong number of Torpedos when calling fleet.get_weapons()")
    self.assertEqual(o, 0, "When calling fleet.get_weapons() you return objects that are not weapons.")

  def test_221(self):
    """ Testing fire() don't do anything if no target
    """
    attacker = Fighter("R")

    try:
      attacker.weapons[0].fire(0)
    except:
        self.fail("fire(weapon, combat_round) raised exception when it should just do nothing if self.target is None.")

  def test_222(self):
    """ Testing fire() don't do anything if combat round is incorrect
    """
    attacker = Fighter("T")
    defender = Fighter("R")
    attacker.weapons[0].target = defender
    attacker.weapons[0].fire(1)

    self.assertEqual(defender.armor, 100, "fire() should not damage ship if combat round is incorrect (weapon charging).")

  def test_223(self):
    """ Testing fire() - torpedos
    """
    attacker = Fighter("T")
    defender = Destroyer("RRE")
    attacker.weapons[0].target = defender
    attacker.weapons[0].fire(0)

    self.assertEqual(defender.shields, 300, "A torpedo shot should directly damage armor.")
    self.assertEqual(defender.armor, 180, "fire() should make damage if combat round is correct and weapon did hit.")
    self.assertEqual(defender.hull, 300, "weapons should not make damage on armor and hull at the same time")

    defender.armor = 50
    attacker.weapons[0].fire(0)
    self.assertEqual(defender.armor, 0, "fire() should make damage if combat round is correct and weapon did hit.")
    self.assertEqual(defender.hull, 300, "excess damage should not apply from armor to hull")

    defender.armor = 0
    attacker.weapons[0].fire(15)

    self.assertEqual(defender.hull, 300 - 120 * 1.2, "torpedos should make more damage on hull.")

    defender = Battleship("LLLLPPP")
    attacker.weapons[0].fire(0)
    self.assertEqual(defender.shields, 1000, "torpedos should not be able to damage a Battleship with PPP loadout.")
    self.assertEqual(defender.armor, 1000, "torpedos should not be able to damage a Battleship with PPP loadout.")
    self.assertEqual(defender.hull, 1000, "torpedos should not be able to damage a Battleship with PPP loadout.")

    defender = Battleship("LLLLAAA")
    attacker.weapons[0].target = defender
    health = defender.armor + defender.hull
    for i in range(10):
      attacker.weapons[0].fire(0)
      new_health = defender.armor + defender.hull

      self.assertLess(new_health, health, "Your torpedos should always hit if there is no point defense.")

      health = new_health

  def test_224(self):
    """ Testing fire() - accuracy
    """
    attacker = Battleship("RRRRPPP")

    hits = 0
    for i in range(10000):
      defender = Battleship("RRRRPPP")
      defender.evasion = 0
      attacker.weapons[0].target = defender
      attacker.weapons[0].fire(0)

      if defender.shields < 1000:
        hits += 1

    #we expect between 72% and 88% accuracy for battleships with no evasion
    expected_hits_min = 10000 * 0.72
    expected_hits_max = 10000 * 0.88

    self.assertGreater(hits, expected_hits_min, "Your accuracy seems to be incorrectly accounted for")
    self.assertLess(hits, expected_hits_max, "Your accuracy seems to be incorrectly accounted for")

  def test_225(self):
    """ Testing fire() - evasion
    """
    attacker = Fighter("L")

    evaded = 0
    for i in range(10000):
      defender = Destroyer("RRE")
      attacker.weapons[0].target = defender
      attacker.weapons[0].fire(0)

      if defender.shields == 300:
        evaded += 1

    #we expect an evasion ratio between 72% and 88% evaded
    self.assertGreater(evaded, 10000 * 0.72, "Your evasion seems to be incorrectly accounted for")
    self.assertLess(evaded, 10000 * 0.88, "Your evasion seems to be incorrectly accounted for")

  def test_226(self):
    """ Testing fire() - damage modifiers
    """
    # Testing Fighters
    attacker = Fighter("L")
    defender = Destroyer("RRE")
    defender.evasion = 0
    attacker.weapons[0].target = defender
    attacker.weapons[0].accuracy = 1
    attacker.weapons[0].fire(0)

    damage = round(defender.max_shields - defender.shields)
    self.assertEqual(damage, round(0.4 * 60), "Fighter Test: Your damage multiplier (ship size) seems to be incorrectly accounted for.")

    # Testing Destroyers
    attacker = Destroyer("RRE")
    defender = Destroyer("RRE")
    defender.evasion = 0

    for weapon in attacker.weapons:
      weapon.target = defender
      weapon.accuracy = 1
      weapon.fire(0)

    damage = round(defender.max_shields - defender.shields)
    self.assertEqual(damage, round(1.2 * 10 * 2), "Destroyer Test: Your damage multiplier (ship size) seems to be incorrectly accounted for.")

    # Testing Cruisers
    attacker = Cruiser("LRTE")
    defender = Battleship("RRRSS")
    defender.evasion = 0
    defender.shields = 0

    for weapon in attacker.weapons:
      weapon.target = defender
      weapon.accuracy = 1
      weapon.fire(0)

    damage = round(defender.max_armor - defender.armor)
    expected_damage = round(1.2 * (10 * 0.4 + 1.2 * 60 + 120))
    self.assertEqual(damage, expected_damage, "Cruiser Test: Your damage multiplier seems to be incorrectly accounted for.")

    # Testing Battleships
    attacker = Battleship("RLLTAAA")
    defender = Battleship("RRRSS")
    defender.evasion = 0
    defender.shields = 0
    defender.armor = 0

    for weapon in attacker.weapons:
      weapon.target = defender
      weapon.accuracy = 1
      weapon.fire(0)

    damage = round(defender.max_hull - defender.hull)
    expected_damage = round(1.5 * (10 * 0.9 + 60 * 2 + 1.2 * 120))
    self.assertEqual(damage, expected_damage, "Battleship Test: Your damage multiplier seems to be incorrectly accounted for.")

  def test_227(self):
    """ Testing fire() - destroyed ships should not be able to fire
    """
    attacker = Fighter("T")
    defender = Battleship("RRRRPPP")
    attacker.armor = 0
    attacker.hull = 0
    defender.evasion = 0
    attacker.weapons[0].target = defender
    attacker.weapons[0].fire(0)

    self.assertEqual(defender.armor, defender.max_armor, "Destroyed ships should not be able to make damage/fire.")

  def test_231(self):
    """ Testing get_stats() total values
    """
    stats = Fleet("random").get_stats()

    self.assertEqual(stats["total_ships"], 45, "Fleet has incorrect total number of ships")
    self.assertEqual(stats["total_cost"], 100, "Fleet has incorrect total cost")
    self.assertEqual(stats["total_hull"], 13600, "Fleet has incorrect total hull")
    self.assertEqual(stats["total_armor"], 16200, "Fleet has incorrect total armor")
    self.assertEqual(stats["total_shields"], 16100, "Fleet has incorrect total shields")

  def test_232(self):
    """ Testing get_stats() damaged values
    """
    fleet = Fleet("random")

    f1 = None
    f2 = None

    # manually destroy / damage some ships (the first two fighters encountered)
    for ship in fleet.ships:
      if not f1 and isinstance(ship, Fighter):
        f1 = ship
        continue
      if not f2 and isinstance(ship, Fighter):
        f2 = ship
      if f1 and f2:
        break

    f1.armor = 0
    f1.shields = 0
    f1.hull = 0

    f2.armor = 0
    f2.hull = 50

    stats = fleet.get_stats()

    self.assertEqual(stats["ships"], 44, "Fleet has incorrect total number of ships")
    self.assertEqual(stats["cost"], 99, "Fleet has incorrect total cost")
    self.assertEqual(stats["hull"], 13450, "Fleet has incorrect total hull")
    self.assertEqual(stats["armor"], 16000, "Fleet has incorrect total armor")
    self.assertEqual(stats["shields"], 16000, "Fleet has incorrect total shields")
    self.assertEqual(stats["damage_taken"], 450, "Fleet has incorrect damage_taken")

  def test_241(self):
    """ Testing __str__() total values
    """
    s = Fleet("random").__str__()

    self.assertEqual(s.strip(), "Fleet random\n=========================================================\nShips: 45/45, Command Points: 100/100\nHull: 13600/13600, Armor: 16200/16200, Shields: 16100/16100", "String method incomplete or incorrectly formatted.")


if __name__ == '__main__':
    unittest.main()