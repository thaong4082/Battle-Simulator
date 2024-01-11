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
from specs.fleets import Fleet, InvalidModuleException, InvalidFleetException

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
      Fleet("invalid_evasion") #we should be throwing an exception here but we are not, we are but the test case is not seeing it

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