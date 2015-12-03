from game_data import World, Item, Location
from player import Player
import winsound

# when player wins the game
import winsound

freq = 2500
duration = 1000
winsound.Beep(freq, duration)

if __name__ == "__main__":
    WORLD = World("map.txt", "locations.txt", "items.txt")
    PLAYER = Player(0,0) # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = "look", "inventory", "score", "quit", "back"

    while not PLAYER.victory:
        location = WORLD.get_location(PLAYER.x, PLAYER.y)

        #put in locations, everytime the reach closer to the destination they will earn two points
        #when they reach farther from the location they will lose 1 point
        PLAYER.points+= 2
        PLAYER.points-= 1

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


    def score(score):
            print("Score:" +str(score)

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