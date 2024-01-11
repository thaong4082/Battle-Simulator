import random

def set_targets(myFleet, enemyFleet):
  '''
  This should ensure that each weapon of the attacker's ships 
  points towards a valid target (ship) of the defender.
  This function must only change weapons's target property!
  The target property must be a ship in the enemy Fleet.
  '''
  # TODO Phase 3

  #do not shoot invalid ships
  valid_ships = []
  for ship in enemyFleet.ships:
    if ship.hull > 0:
      valid_ships.append(ship)
  
  #priority queue weapons unbounded
  torpedoQ = PriorityQueue()
  railgunQ = PriorityQueue()
  laserQ = PriorityQueue()
  for ship in myFleet.ships:
    priority = get_priority(ship)
    for weapon in ship.weapons:
      if weapon.cooldown == 15 and ship.hull > 0:
        torpedoQ.enqueue(priority, weapon)
      if weapon.cooldown == 5 and ship.hull > 0:
        railgunQ.enqueue(priority, weapon)
      if weapon.cooldown == 1 and ship.hull > 0:
        laserQ.enqueue(priority, weapon)
          
    #setting target for torpedo
  if torpedoQ.is_empty():
    weapon.target = None
  else:
    for targetship in valid_ships:
      #if the their point defense is less, shoot torpedo (1)
      if targetship.pd < 0.65 and torpedoQ.peek() != None:
        torpedo_deployed = torpedoQ.dequeue()
        torpedo_deployed.target = targetship
      #elif they have shields, shoot torpedo (2)
      elif targetship.shields > 0 and torpedoQ.peek() != None:
        torpedo_deployed = torpedoQ.dequeue()
        torpedo_deployed.target = targetship
        #elif they have a high cost (the ship is a battleship or a cruiser, aim torpedo) (3)
      elif targetship.cost > 3 and torpedoQ.peek() != None:
        torpedo_deployed = torpedoQ.dequeue()
        torpedo_deployed.target = targetship
        #else, ignore
      else:
        pass
            
    # #setting target for railgun
  if railgunQ.is_empty():
    weapon.target = None
  else:
    for targetship in valid_ships:
    
      #if the shields is greater than their base, then railgun shoots (8, we made it ourselves)
      if targetship.shields > targetship.base and railgunQ.peek() != None:
        railgun_deployed = railgunQ.dequeue()
        railgun_deployed.target = targetship
      #if the target ships has shields, railgun shoots (4)
      elif targetship.shields > 0 and railgunQ.peek() != None:
        railgun_deployed = railgunQ.dequeue()
        railgun_deployed.target = targetship
      #elif the target ship has little hull, railgun shoot(5)
      elif targetship.hull <= (targetship.max_hull/3) and railgunQ.peek() != None:
        railgun_deployed = railgunQ.dequeue()
        railgun_deployed.target = targetship
      
      else:
        pass

    # # setting target for laser
  if laserQ.is_empty():
    weapon.target = None
  else:
    for targetship in valid_ships:
      #if the shields are down on the target ship, aim the laser (6)
      if targetship.shields == 0 and laserQ.peek() != None:
        laser_deployed = laserQ.dequeue()
        laser_deployed.target = targetship
      #if the armor of the ship is damged by at least half, aim a laser at it (7)
      elif targetship.armor <= (targetship.max_armor/2) and laserQ.peek() != None:
        laser_deployed = laserQ.dequeue()
        laser_deployed.target = targetship
      else:
        pass
#if after all our cases there are weapons that are still not given a target, randomly assign a target
  for ship in myFleet.ships:
    for weapon in ship.weapons:
      if len(valid_ships) > 0:
        if weapon.target == None:
          weapon.target = random.choice(valid_ships)
      else:
        # to prevent weapons shoot on anihalated fleets
         weapon.target = None


#defines the priority queue for ships         
def get_priority(self):
  if self.cost == 8: #if its a battleship
    return 3
  if self.cost == 4: #if its a cruiser
    return 2
  if self.cost == 2: #if its a destroyer
    return 1
  if self.cost == 1: #if its a fighter
    return 0


## Taken from Maddie Kear's Priority Queue Lab
class Queue:
  """Queue ADT implemented as a linked list (options for bounded and unbounded).
  
  """

  def __init__( self, bound = None ):
    """ Queue starts out empty. If bound == None, the queue
    is unbounded. Otherwise set the capacity of the queue
    to be the integer value of bound. """
    self.bound = bound
    self.front = self.back = None
    self.length = 0
    self.capacity = self.bound

  def __len__( self ):
    """ Return the current size of the queue. """
    return self.length

  def is_empty(self):
    """ Returns true if the queue is empty, false otherwise. """
    if self.length == 0:
      return True
    else:
      return False

  def enqueue(self, item):
    """ If full and bounded, return -1 to indicate failure. """
    tempNode = Node(item)
    if self.capacity == self.length:
      return -1
    elif self.capacity == None or self.capacity != self.length:
      if self.is_empty():
        self.front = self.back = tempNode
      else:
        self.back.next = tempNode
        self.back = tempNode

    self.length = self.length + 1
    #return self.length

  def dequeue(self):
    """ DeQ and return item. If empty, return None. """
    if self.is_empty():
      return None
    else:
      temp = self.front.next
      self.length = self.length - 1
      removedItem = self.front.data
      self.front = temp
      return removedItem

  def peek(self):
    """ Return the item that would be dequeue'd next.
        If empty, return None. """
    if self.is_empty():
      return None
    else:
      return self.front.data

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class PNode(Node):
  def __init__(self, data, priority):
    super().__init__(data)
    self.priority = priority

class PriorityQueue(Queue):
  def __init__(self, bound = None):
    super().__init__(bound = None)
    self.front = None

  def enqueue(self, priority, item):
    tempNode = PNode(item, priority)
    
    #case if queue is empty
    if self.is_empty() == True:
      self.front = self.back = tempNode

    #case if the item has lower priority than first item
    else:
      if self.front.priority > priority:
        tempNode.next = self.front
        self.front = tempNode

      else:
        current = self.front
        while current.next:
          if priority < current.next.priority:
            break
          current = current.next
  
        tempNode.next = current.next
        current.next = tempNode
  
    self.length += 1 

  def __str__(self):
    return 'PriorityQueue'
