class Location:
    def __init__(self, position, brief_description, long_description, commands, items, times_visited):
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
        :param: position: coordinate of where the player is
        :param: brief_description: a small description on the location
        :param: long_description: a longer description on the location
        :param: commands: directions to move
        :param: items: items that in the location
        :param: times_visted: how many times player visited the location before
        Example
        position: ( 0 , 0)
        brief_description: " You are in Starbucks."
        long_description: " You are in the cozy warmest place of them all at UTM. It's where everyone comes to get their warm spice lattes. You are are starbuck."
        commands: North, South, East, West
        items: " There is gum on the fourth floor of the library"
        times_visited: library visited: 1
        '''

        self.position = position
        self.brief_description = brief_description
        self.long_description = long_description
        self.commands = commands
        self.items = items
        self.times_visited = 0

    def get_brief_description(self):
        '''Return str brief description of location.
        :param:
        :return: brief description
        example:
        brief_description: " You are in Starbucks."
        '''

        return self.brief_description

    def get_full_description(self):
        '''Return str long description of location.
        :param:
        :return: full  description
        example:
        long_description: " You are in the cozy warmest place of them all at UTM. It's where everyone comes to get their warm spice lattes. You are are starbuck."
        '''

        return self.long_description

    def available_actions(self):
        '''
        -- Suggested Method (You may remove/modify/rename this as you like) --
        Return list of the available actions in this location.
        The list of actions should depend on the items available in the location
        and the x,y position of this location on the world map.
        :param:
        :return: commands available
        example:
        commands: North, South, East, West
        '''

        return self.commands


class Item:
    def __init__(self, name, start, target, target_points):
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
        :param: name: name of the item
        :param: start: where the item is first located
        :param: target: where the item should go ( target location)
        :param: target_points: how many points does the item count for

        Example
        name: "gum"
        start: "library fourth floor"
        target: "in players mouth"
        target_points: " 2 points"
        '''

        self.name = name
        self.start = start
        self.target = target
        self.target_points = target_points

    def get_starting_location(self):
        '''Return int location where item is first found.
        :param:
        :return: the integer location where the item is first located at
        example: Item is found in library at (0,1)
                 return Item in library at (0,1)
        '''
        return self.start

    def get_name(self):
        '''Return the str name of the item.
        :param
        :return: the name of the item
        example: item name: GUM
        '''

        return self.name

    def get_target_location(self):
        '''Return item's int target location where it should be deposited.
        :param:
        :return: items destination coordinates
        example: gum is suppose to go into the trashcan
                trashcan coordinates are (2,3)
                gum must reach coordinates (2,3)
        '''
        return self.target

    def get_target_points(self):
        '''Return int points awarded for depositing the item in its target location.
        :param:
        :return: the points for putting the item into its proper location
        example:
        Gum is suppose to go into trashcan
        Gum is in trashcan
        points earned: 3
        '''
        return self.target_points


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

        self.map = self.load_map(mapdata)
        self.locations = self.load_locations(locdata)
        self.items = self.load_items(itemdata)

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
        example:
        1   0   -1
        2   3   4
        -1  5   6
        '''

        file = open(filename, "r")
        new_map = []

        for line in file:
            new_map.append(
                [int(i) for i in line.strip().split()]
            )

        file.close()
        return new_map

    def load_locations(self, filename):
        '''
        Store all locations from filename (locations.txt) into the variable "self.locations"
        however you think is best.
        Remember to keep track of the integer number representing each location.
        Make sure the Location class is used to represent each location.
        Change this docstring as needed.
        :param filename:
        :return: the list return_location

        Example:
        LOCATION 1
        Points = 1

        You are on the first floor of the UTM Library. There is an empty study room to the South, an exit from the library to the North.
        You are on the first floor of the UTM Library. It's usually crowded at this time of the day, but today it's eerily quiet.
        Only a few students are studying inside one of the study rooms. You better not disturb them. A librarian stands near the
        service desk, looking bored and sleepy. There is an empty study room to the South, an exit from the library to the North.

        Go North
        Go south
        Go East
        Go West
        '''

        items = None
        times_visted = 0
        brief_description = ""
        long_description = ""
        commands = []
        index_of_location = ""

        file = open(filename, "r")
        for line in file:

            if "LOCATION" in line:
                index_of_location = int(line.split(" ")[1].strip("\n"))

            if "brief description:" in line:
                brief_description = line.strip("brief description:")

            if "long description:" in line:
                long_description = line.strip("long description:").strip("\n")

        location = Location(index_of_location, brief_description, long_description, commands, items, times_visted)

        file.close()
        return location

    def load_items(self, filename):
        '''
        Store all items from filename (items.txt) into ... whatever you think is best.
        Make sure the Item class is used to represent each item.
        Change this docstring accordingly.
        :param filename:
        :return: the list return_items

        Example:
        Item: Gum
        Location: Library
        Points: 2

        Brief_description: You have gum.

        long_description: You have the 5 flavor, ever lasting blueberry gum. It is a 6 pack. Black packaging.

        list of commands: Eat the gum
                          leave the gum
                          hit the gum
        '''

        file = open(filename, 'r')
        return_items = []
        for line in file:
            lolol = line.split(" ")
            return_items.append(lolol)
        file.close()

        return return_items

    def get_location(self, x, y):
        '''Check if location exists at location (x,y) in world map.
        Return Location object associated with this location if it does. Else, return None.
        Remember, locations represented by the number -1 on the map should return None.
        :param x: integer x representing x-coordinate of world map
        :param y: integer y representing y-coordinate of world map
        :return: Return Location object associated with this location if it does. Else, return None.

        Example: x = 3 , y = 4

        player location will move ( 3, 4)
        '''

        for i in self.locations:
            if y > 0 and x > 0:
                return Location
            else:
                return None

        for column in range(len(self.map)):
            for row in range(len(self.map[column])):
                for location in self.locations:
                    if int(location.get_position()) == self.map[column][row]:
                        if (row == x and column == y):
                            return location
        return None

x = World("map.txt","locations.txt","items.txt")
print(x.load_locations("locations.txt"))
