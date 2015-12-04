from game_data import World, Item, Location
from player import Player
import winsound


freq = 2500
duration = 1000
winsound.Beep(freq, duration)

if __name__ == "__main__":
    WORLD = World("map.txt", "locations.txt", "items.txt")
    PLAYER = Player(2,4) # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = ["look", "inventory", "score", "quit", "back"]
    choice = ""

    while not PLAYER.victory:
        location = WORLD.get_location(PLAYER.x, PLAYER.y, True, PLAYER)

        #put in locations, everytime the reach closer to the destination they will earn two points
        #when they reach farther from the location they will lose 1 point
        #PLAYER.points+= 2
        #PLAYER.points-= 1

        print("You've got an important exam coming up this evening, and you've been studying for weeks.")
        print("Last night was a particularly late night on campus. You had difficulty focusing, so rather than staying in one place, you studied in various places throughout the building as the night progressed.")
        print("Unfortunately, when you woke up this morning, you were missing some important exam-related items. You cannot find your T-card, and you're pretty sure that you're not going to get into tonight's exam without it.")
        print("Also, you seem to have misplaced your lucky exam pen -- even if they let you in, you can't possibly write with another pen!")
        print("Finally, your instructor for the course is nicer than your CSC108 instructors in that they are allowing you one handwritten page of information in the exam.")
        print("Last night, you painstakingly crammed as much material onto a single page as humanly possible, but that's missing, too!")
        print("All of this stuff must be around the building somewhere! Can you find all of it before your exam starts tonight?")

        print("Here is a map of Univeristy of Toronto Mississauga, you are ")
        print("                       ________________")
        print("                       |    library   |")
        print("                       |   3th floor  |")
        print("                    == |              |")
        print("---------------   ==   ------|   |-----")
        print("|   library   | ==           |   |")
        print("|   2nd floor |         _____|   |____")
        print("|             |        | study room   |")
        print("|_    ________|        |____      ____|")
        print("  |  |                      |    |                    ________________            _____________")
        print("--|  |-------               |    |                   |               |           |            |")
        print("|           |               |    |                   |               |           |            |")
        print("| bathroom  |               |  l |                   |  Deerfield    |           |    CCIT    |")
        print("|           |               |  o |                   |               |           |            |")
        print("--|  |-------               |  n |___________________|               |___________|            |")
        print("  |  |                      |  g                                wilderness trail              |")
        print("  |  |                      |     ____________________________________________________________|")
        print("  |  |                      |  p |")
        print("  | p|                      |  a |")
        print("  | a|                      |  t |")
        print("  | t|                      |  h |")
        print("  | h|                      |    |")
        print("  |  |                   ___|    |___")
        print("  |  |                  |            |")
        print("  |  |                  |            |                                        __________")
        print("  |  |__________________|            |/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/          |")
        print("  |         catwalk       starbucks  ----------------------------------------           |")
        print("  |_____________________                       hallway                            IB    |")
        print("                        |            ----------------------------------------           |")
        print("                        |____________/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ __________|")



        print("What to do? \n")
        print("Here are your options: ")
        print(menu)
        choice = input("\nEnter action: ")

        if (choice == "[menu]"):
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")

            if choice =="look":
                Location.get_brief_description()
            elif choice == "inventory":
                inventory = player.get_inventory()
            elif choice == "score":
                print(score)
            elif choice == "quit":
                exit()
            elif choice == "back":
                print ("What do do?")
                choice = ("Choose action: ")


        elif choice == 'north':
            PLAYER.move_north()
            location = WORLD.get_location(PLAYER.x, PLAYER.y)

        elif choice == 'south':
            PLAYER.move_south()
            location = WORLD.get_location(PLAYER.x, PLAYER.y)

        elif choice == 'east':
            PLAYER.move_east()
            location = WORLD.get_location(PLAYER.x, PLAYER.y)

        elif choice == 'west':
            PLAYER.move_west()
            location = WORLD.get_location(PLAYER.x, PLAYER.y)


   # def score(score):
#    print("Score:" +str(score))

        # CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON USER'S CHOICE
        #    REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if the
        #               choice the user made was just a movement, so only updating player's position is enough to change
        #               the location to the next appropriate location
        # Possibilities: a helper function do_action(WORLD, PLAYER, location, choice)
        # OR A method in World class WORLD.do_action(PLAYER, location, choice)
        # OR Check what type of action it is, then modify only player or location accordingly
        # OR Method in Player class for move or updating inventory
        # OR Method in Location class for updating location item info, or other location data
        # etc....