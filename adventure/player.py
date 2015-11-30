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

        global location
        newposition = map[location][dx,dy]
        if newposition == -1:
            print('This way is blocked')
        elif newposition >= 0:
            move(dx,dy)
        else:
            location = newposition

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

        itemadd = item.lower()
        if itemadd == ' ':
            print (' take what?')
            return





    def remove_item(self, item):
        '''
        Remove item from inventory.
        :param item:
        :return:
        '''



    def get_inventory(self):
        '''
        Return inventory.
        :return:
        '''

        if len(get_inventory) == 0:
            print('Inventory:\n ( nothing)')
            return
        itemcount = {}
        for item in inventory:
            if item in itemcount.keys():
                itemcount[item] += 1

            else:
                itemcount[item] = 1
        print('Inventory: ')
        for item in set(inventory):
            if item[item] > 1:
                print('  %s (%s)'  % (item, itemcount[item]))
            else:
                print ('  '  + item)


