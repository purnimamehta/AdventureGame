class Location:

    def __init__(self):
        '''Creates a new location.          
        ADD NEW ATTRIBUTES TO THIS CLASS HERE TO STORE DATA FOR EACH LOCATION.
        
        Data that could be associated with each Location object:
        a position in the world map,
        a brief description,
        a long description,
        a list of available commands/directions to move,
        items that are available in the location,
        and whether or not the location has been visited before.
        Store these as you see fit.

        This is just a suggested starter class for Location.
        You may change/add parameters and the data available for each Location class as you see fit.
  
        The only thing you must NOT change is the name of this class: Location.
        All locations in your game MUST be represented as an instance of this class.
        '''

        self.position = position
        self.briefdesc = briefdesc
        self.longdesc = longdesc
        self.commands = commands
        self.items = items

        pass



    def get_brief_description (self):
        '''Return str brief description of location.'''


        pass

    def get_full_description (self):
        '''Return str long description of location.'''
        file = open(filename, 'r')
        for line in file:
            line[1] = line.readline()


        pass

    def available_actions(self):
        '''
        -- Suggested Method (You may remove/modify/rename this as you like) --
        Return list of the available actions in this location.
        The list of actions should depend on the items available in the location
        and the x,y position of this location on the world map.'''
        pass

class Item:

    def __init__ (self, name, start, target, target_points):
        '''Create item referred to by string name, with integer "start"
        being the integer identifying the item's starting location,
        the integer "target" being the item's target location, and
        integer target_points being the number of points player gets
        if item is deposited in target location.

        This is just a suggested starter class for Item.
        You may change these parameters and the data available for each Item class as you see fit.
        Consider every method in this Item class as a "suggested method":
                -- Suggested Method (You may remove/modify/rename these as you like) --

        The only thing you must NOT change is the name of this class: Item.
        All item objects in your game MUST be represented as an instance of this class.
        '''

        self.name = name
        self.start = start
        self.target = target
        self.target_points = target_points

    def get_starting_location (self):
        '''Return int location where item is first found.'''


        pass

    def get_name(self):
        '''Return the str name of the item.'''

        pass

    def get_target_location (self):
        '''Return item's int target location where it should be deposited.'''

        pass

    def get_target_points (self):
        '''Return int points awarded for depositing the item in its target location.'''

        pass

class World:

    def __init__(self, mapdata, locdata, itemdata):
        '''
        Creates a new World object, with a map, and data about every location and item in this game world.

        You may ADD parameters/attributes/methods to this class as you see fit.
        BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES.

        :param mapdata: name of text file containing map data in grid format (integers represent each location, separated by space)
                        map text file MUST be in this format.
                        E.g.
                        1 -1 3
                        4 5 6
                        Where each number represents a different location, and -1 represents an invalid, inaccessible space.
        :param locdata: name of text file containing location data (format left up to you)
        :param itemdata: name of text file containing item data (format left up to you)
        :return:
        '''
        self.map = self.load_map(mapdata) # The map MUST be stored in a nested list as described in the docstring for load_map() below
        # self.locations ... You may choose how to store location and item data.
        self.load_locations(locdata) # This data must be stored somewhere. Up to you how you choose to do it...
        self.load_items(itemdata) # This data must be stored somewhere. Up to you how you choose to do it...

    def load_map(self, filename):
        '''
        THIS FUNCTION MUST NOT BE RENAMED OR REMOVED.
        Store map from filename (map.txt) in the variable "self.map" as a nested list of strings OR integers like so:
            1 2 5
            3 -1 4
        becomes [['1','2','5'], ['3','-1','4']] OR [[1,2,5], [3,-1,4]]
        RETURN THIS NEW NESTED LIST.
        :param filename: string that gives name of text file in which map data is located
        :return: return nested list of strings/integers representing map of game world as specified above
        '''

        #http://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-4-the-game-loop/

        file = open(filename, "r")
        l = []
        for line in file:
            line = line.strip()
            line = line.split(' ')
            line = map(int,line)
            l.append(line)
        file.close()
        return l
        pass

    def load_locations(self, filename):
        '''
        Store all locations from filename (locations.txt) into the variable "self.locations"
        however you think is best.
        Remember to keep track of the integer number representing each location.
        Make sure the Location class is used to represent each location.
        Change this docstring as needed.
        :param filename:
        :return:
        '''

        file = open(filename, "r")
        filenametxt = f.read()
        d = filename.loads(filenametxt)







        pass

    def load_items(self, filename):
        '''
        Store all items from filename (items.txt) into ... whatever you think is best.
        Make sure the Item class is used to represent each item.
        Change this docstring accordingly.
        :param filename:
        :return:
        '''
        if item not in buildings[location]:
            print(" no item")
            return




        pass

    def get_location(self, x, y):
        '''Check if location exists at location (x,y) in world map.
        Return Location object associated with this location if it does. Else, return None.
        Remember, locations represented by the number -1 on the map should return None.
        :param x: integer x representing x-coordinate of world map
        :param y: integer y representing y-coordinate of world map
        :return: Return Location object associated with this location if it does. Else, return None.
        '''
        self.x = x
        self.y = y

        if buildings =
            {'library': { postion :' north of the cct building, 4th floor,', firstfloor:' Go south', turnleft: ' No way ', turnright: ' No way '},
            {'firstfloor': {desciption : ' you are on the 1st floor on the library', gooutsideoflib : 'there is a starbucks', turnleft : ' no way ', turnright: ' no way', Goto4thfloor: ' back at the forth floor'},
            {'gooutsideoflib': { description: ' you are now infront of the warm smelling starbucks', goinsidestarbucks: ' buy or not buy something', gobackintolib: ' now back in the library', gooutside: 'IB is right infront of you', turnleft: ' no way'}}

        sec = {}
        for i in range(buildings):
            index = i[0]
            postion = index



        #http://inventwithpython.com/blog/2014/12/11/making-a-text-adventure-game-with-the-cmd-and-textwrap-python-modules/
        #https://github.com/soapy1/TextAdventure/blob/master/textAdventure.py
        #https://www.youtube.com/watch?v=8CDePunJlck






        pass
