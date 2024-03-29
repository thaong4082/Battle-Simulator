#NAMES: Maddie Kear and Thao Nguyen

from phase2tests.tests import tests_phase2
# run via shell: python main.py (to avoid visual bugs)

# from tests import test_ships
# test_ships() # TODO 

from specs.fleets import Fleet, create_random_fleet
from simulation import Simulation

# CONFIGURATION
gui = True # Set to False to run combat without GUI

# Prepare Fleets

# feel free to modify student.txt to a fleet of your liking...
leftFleet = Fleet("student") 
# will be randomly generated each time. has a very weak targeting mechanism
create_random_fleet()
rightFleet = Fleet("random") 

# Run Simulation
Simulation(leftFleet, rightFleet, gui) 
