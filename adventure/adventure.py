from game_data import World, Item, Location
from player import Player

if __name__ == "__main__":
    WORLD = World("map.txt", "locations.txt", "items.txt")
    PLAYER = Player(0,0) # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = ["look", "inventory", "score", "quit", "back"]
    #same as command in calender

    while not PLAYER.victory:
        location = WORLD.get_location(PLAYER.x, PLAYER.y)


        # ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # depending on whether or not it's been visited before,
        #   print either full description (first time visit) or brief description (every subsequent visit)


        # The introduction
        print("Oh no! Its almost time for your exam. It is about you!  Also about zombies.  If this is your first time playing you should type in 'how to play' so that you can learn to play the game.  If you played the game before, took a look at the code before playing or are exceptional at guessing, type in 'start' to begin.")
        opt = input()
        if opt == 'start':
            main()
        elif opt == 'how to play':
            print("\n\n\n\nHOW TO PLAY:  \n\nMAIN CONTROLS:  There are several functions you can do in this game.  To move around you simply enter which way you want to go.  For example, if you want to go left, type in \"left\".  It is important to note that your movements are traked using a grid system.  You can find your position in the x or y plane at any time by inputting \"pos x\" or \"pos y\".\nTo print a map so you can know where in the world you are, input \"map\".  It will show you a map and tell you where you are.\nAs you might assume, you are carrying stuff.  To see what you are holding you can input \"check items\".  You can also drop stuff by inputting \"drop\" or check if you can pick anything up from your environment by inputting \"search\".\nIf you want to know how many health points you have, type in \"health\"   \n \nFIGHTING:  You can also fight zombies in this game.  At any one time you can fight one or two zombies but keep in mind, your friend in fat and lazy and does not help you while you fight.  First you will be told how many zombies you are fighting.  Then you can choose to fight by typeing in \"yes\" or you can choose to get away from the fight by typeing in \"run\" and \"no\" to do niether.  To choose which zombie you wish to attack, press \"1\" for zombie one, or \"2\" for zombie two.\nIf your hp is low after fighting some zombies you can eat or drink by typing in \"eat\" or \"drink\".  Remeber that you need to have food or water for you do this... unless you are a wizard then you just need to remeber aquaerupto.  \nThat is it.  Also, sometimes you can kill a zombie into negative hp.  Don't worry about that, you are just that awesome.")
            if input() == 'start':
                main()
            elif input() == 'quit':
               exit

        print("What to do? \n")
        print("[menu]")
        for action in location.available_actions():
            print(action)
        choice = input("\nEnter action: ")

        if (choice == "[menu]"):
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")

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