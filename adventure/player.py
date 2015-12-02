class Player:

    def __init__(self, x, y):
        '''
        Creates a new Player.
        :param x: x-coordinate of position on map
        :param y: y-coordinate of position on map
        :return:
        This is a suggested starter class for Player.
        You may add new parameters / attributes / methods to this class as you see fit.
        Consider every method in this Player class as a "suggested method":
                -- Suggested Method (You may remove/modify/rename these as you like) --
        '''
        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False

    def move(self, dx, dy):
        '''
        Given integers dx and dy, move player to new location (self.x + dx, self.y + dy)
        :param dx:
        :param dy:
        :return:
        '''
        self.x += dx
        self.y += dy

        pass

    def move_north(self):
        '''These integer directions are based on how the map must be stored
        in our nested list World.map'''
        """Go to the 4th floor of the library, if possible."""

        self.move(0,0)


    def move_south(self):
        self.move(0,1)

    def move_east(self):
        self.move(1,0)

    def move_west(self):
        self.move(-1,0)

    def add_item(self, item):
        '''
        Add item to inventory.
        :param item:
        :return:
        '''

        if item not in self.inventory:
            self.inventory.append(item)
        return True

    def remove_item(self, item):
        '''
        Remove item from inventory.
        :param item:
        :return:
        '''
        if item in self.inventory:
            self.inventory.remove(item)

        return True




    def get_inventory(self):
        '''
        Return inventory.
        :return:
        '''

        return self.inventory

#http://codereview.stackexchange.com/questions/37677/a-small-python-text-adventure-frame