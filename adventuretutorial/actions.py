import player
from player import Player

class Action(object):
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name   = name
        self.kwargs = kwargs
    
    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)
    
class MoveNorth(Action):
    def __init__(self):
        super(MoveNorth, self).__init__(method=Player.move_north, name='Move North', hotkey = 'n')
   
class MoveSouth(Action):
    def __init__(self):
        super(MoveSouth, self).__init__(method=Player.move_south, name='Move South', hotkey = 's')

class MoveEast(Action):
    def __init__(self):
        super(MoveEast, self).__init__(method=Player.move_east, name='Move East', hotkey = 'e')
    
class MoveWest(Action):
    def __init__(self):
        super(MoveWest, self).__init__(method=Player.move_west, name='Move West', hotkey = 'w')

class ViewInventory(Action):
    """Prints the player's inventory"""
    def __init__(self):
        super(ViewInventory, self).__init__(self, methods=Player.print_inventory, name='View Inventory', hotkey = 'i')         

class Attack(Action):
    def __init__(self, enemy):
        super(Attack, self).__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy)

class Flee(Action):
    def __init__(self, tile):
        super(Flee, self).__init__(method=Player.flee, name="Flee", hotkey='f', tile=tile)

