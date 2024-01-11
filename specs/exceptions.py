
#look at test_exceptions line 34

class InvalidFleetException(Exception):
  """
  If you try to build a ship other than F, D, C, B raise an InvalidFleetException
  If your fleet contains ships worth more than 100 command points raise an InvalidFleetException
  """
  def __init__(self, message):
    self.message = message

class InvalidModuleException(Exception):
  """
  If a ship contains more than the maximum allowed number of weapon / defense slots raise an InvalidModuleException.
  If a ship has an unknown module (letter other than R, L, T, S, A, P, E) raise a InvalidModuleException
  If a ship contains more than one Ion Thruster Module raise an InvalidModuleException
  """
  def __init__(self, message):
    self.message = message