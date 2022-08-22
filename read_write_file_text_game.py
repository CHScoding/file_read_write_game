# Import for path manipulation with file reading/writing
import os
# Inventory list
inventory = ["", "", ""]
# List for first time experiences and ending lock
progress_gates = [1, 1, 1, 1]
# Tuple of room numbers
rooms_tuple = (1, 2, 3, 4, 5, 6)
# Bool variable lock needed for final condition to beat the game
p_lock_locked = 1
# Variables that determine if the player has experienced a specific event for the first time
first_time_flame = 1
first_time_water = 1
first_time_dark = 1

# Name of save file
fname = "game_save.txt"
# Gets the current working directory path
cw = os.getcwd()
# Stores a concatenated file path with the working directory and text file
abspath = os.path.join(cw, fname)

# Print narration messages
print("You wake up and find yourself trapped in an enclosed circular room surrounded by six doors.")
print("You think to yourself, 'How did this happen?' You last remember being greeted at your home by an unusual group of colorfully dressed individuals claiming you won a prize.")
print("Unfortunately, just as quickly as you rejected what appeared to be an obvious scam, you also found yourself quickly asleep.")
print("At least that's what you think happened. 'Regardless of what happened, one thing is for certain you need to figure out where you are, and how to get out.'")
print("Since the room you are currently in is barren there is really only no other option but to choose a room.")
print("")
#with open("RAdventures.txt", "w") as file:
    #file.write("data")
#file.close()
#file = open(abspath, "w+") #"w+"
#file.writelines("word")
#file.writelines("wordssds")
#file.close()


def flame_room():
    """
    Function that can add to the inventory list based on user's input and first or second experience
    """
    # Makes variable available to local scope
    global first_time_flame
    print("")
    print("You're in the flame room.")
    print("Despite the flashy design of the door's exterior, the interior of the room is rather drab. ")
    print("One thing that does match the door's design is the heat. The abundance of lit wall-mounted torches has resulted in the room being very warm.")
    print("You also happen to notice a long table that stretches from one side of the room to the other.")
    print("On top of the table are a bunch of small silver objects.")
    print("What will you do?")
    print("")
    # Loop through conditions until user's input matches one
    while True:
        # Loop through user input until they enter an appropriate integer
        while True:
            # Check user input for usable input
            try:
                # Variable to store user input
                player_choice = int(input("1. Inspect table | 2. Exit room | 3. Check inventory: "))
                # Break off from loop
                break
            # Catch exceptions from improper user input
            except Exception:
                # Message to warn user about improper input
                print("There was an issue with your response. Please type a number without punctuation.")

        # Checks user input to the first choice
        if player_choice == 1:
            # Checks if this is the first time the player has chosen this choice
            if int(first_time_flame) == 1:
                # Print narration messages
                print("")
                print("You get close to the table and pick up one of the objects.")
                print("Turns out the objects are all pocket lighters.")
                print("You try to turn the one you are holding one, but it doesn't light.")
                print("You have a feeling if you want a working lighter you may have to sift through them for one that does work.")
                print("You go through with it and find a lighter with a weak flame after testing about 50 different lighters.")
                print("")
                # Add lighter to inventory
                inventory[0] = "Lighter"
                # Set first time flame variable false to prevent the first time messages from displaying again
                first_time_flame = 0

            # Print message after user tries to access input 1 after doing the first attempt
            elif first_time_flame == 0:
                print("")
                print("'I don't need a new lighter, and I would rather not have to need another one from there again.'")
                print("")

            else:
                print("Error, try again.")
                break

        # Check option 2 input to exit
        elif player_choice == 2:
            game_start()

        # Check option 3 input for inventory to display
        elif player_choice == 3:
            print(inventory)

        else:
            # Improper input warning message
            print("There was an issue with your response. Please type a number without punctuation.")


def water_room():
    """
    Function that can add to the inventory list based on user's input and first or second experience
    """
    # Makes variable available to local scope
    global first_time_water
    print("")
    print("You're in the water room.")
    print("This room matches with its door design as it is actually raining, or rather there are sprinklers on the ceiling spraying water.")
    print("Besides the sprinklers, there are vents around the ends of the room collecting the water. There is also a water bottle that has found itself on top of the drains.")
    print("What will you do?")
    print("")
    # Loop through conditions until user's input matches one
    while True:
        # Loop through user input until they enter an appropriate integer
        while True:
            # Check user input for usable input
            try:
                # Variable to store user input
                player_choice = int(input("1. Inspect water bottle | 2. Exit room | 3. Check inventory: "))
                # Break off from loop
                break
            # Catch exceptions from improper user input
            except Exception:
                # Message to warn user about improper input
                print("There was an issue with your response. Please type a number without punctuation.")

        if player_choice == 1:
            # Checks if this is the first time the player has chosen this choice
            if int(first_time_water) == 1:
                # Print narration messages
                print("")
                print("You pick up the water bottle which is already contains a little water.")
                print("With nothing else noticeable in the room you catch some of the water from the sprinklers into the bottle as you make your way to the door.")
                print("")
                # Add water bottle to inventory
                inventory[1] = "Water Bottle"
                # Set first time flame variable false to prevent the first time messages from displaying again
                first_time_water = 0

            # Print message after user tries to access input 1 after doing the first attempt
            elif first_time_water == 0:
                print("")
                print("'There is no reason to go back in there right now.'")

            else:
                print("Try again.")
                break

        # Check option 2 input to exit
        elif player_choice == 2:
            game_start()

        elif player_choice == 3:
            print(inventory)

        else:
            # Improper input warning message
            print("There was an issue with your response. Please type a number without punctuation.")


def metal_room(members):
    """
    Function that can remove and add list items based on an equal condition, and gives the user input for more choices.
    :param members: The inventory list of items
    :return: The inventory list of items
    """
    print("")
    print("You're in the metal room.")
    print("The room is largely empty and with a gradient of grey splashed across every surface.")
    print("The only objects of note are the four boxes piled on each other in the corner and a medium-sized makeshift wooden table against the wall furthest from the door.")
    print("What will you do?")
    print("")
    # Loop through conditions
    while True:
        # Loop through user input until it is usable
        while True:
            try:
                player_choice = int(input("1. Inspect boxes | 2. Inspect table | 3. Exit room | 4. Check inventory: "))
                break
            except Exception:
                print("There was an issue with your response. Please type a number without punctuation.")

        # Check user input to see if it is equal to the first option
        if player_choice == 1:
            print("")
            print("You get close to the boxes. Weary something might come out you hesitate and then quickly open them one by one.")
            print("Turns out there was nothing in any of them, except the last one. Unlike the other boxes, this one was stuck to the floor.")
            print("Based on the contents of the box it became possible to at least imagine why the box might be so thoroughly planted to the ground.")
            print("Inside the box was a circular hole in the ground. It was completely dark inside the hole.")
            print("Perhaps there is something that can help you see into the hole.")
            print("")

            while True:
                try:
                    # Check inventory index for lighter item
                    if "Lighter" in str(inventory):
                        # Ask the user if they want to use the item
                        use_item = input("You think that the lighter could be used to view in the hole. Use it? yes/no ").lower()
                        print("")
                        # Verify user input as yes to exchange the lighter for a stone
                        if use_item == "yes":
                            # Check each item in the inventory list that was given to the members parameter of the function
                            for memb in members:
                                # Verify if the item is the lighter
                                if memb == "Lighter":
                                    # Remove lighter and add weighty stone to inventory
                                    inventory[0] = "Weighty Stone"
                                    # Print narration messages
                                    print("")
                                    print("You turn the lighter on and hold it just above the top of the hole.")
                                    print("You're shocked by how deep the hole is, which is to say it was not more than a couple of feet deep.")
                                    print("You notice a palish object glint at the bottom.")
                                    print("You use the light to get a closer look and notice that it is a perfectly oval stone.")
                                    print("Thinking it might be important, you try to grab it, but when you pick it up its far heavy than its small size would suggest")
                                    print("Additionally, by the time you hoist it up near the top, the top of the hole begins to close around your arms causing you to drop the lighter.")
                                    print("When the lighter lands at the bottom, the hole opens back up.")
                                    print("With the lighter off not only can you not see where it landed, but with the sudden squeeze your arms exhibited, you decide to leave it and take the stone.")
                                    print("")
                                    # Return the altered list items to the inventory
                                    return inventory

                                else:
                                    continue
                        # Go back to choices
                        elif use_item == "no":
                            print("You decide to look elsewhere.")
                            break

                        else:
                            # Improper input warning message
                            print("There was an issue with your input. Please try typing yes or no again.")
                    # If the user has no voice recorder move back to the choices
                    else:
                        break
                # Catch exceptions and go back to this room's choices
                except Exception:
                    print("")
                    # Break from loop and return to choices
                    break

        # Check option 2 input
        elif player_choice == 2:
            # Print narration messages
            print("")
            print("Its literally a bare rickety wooden table.")
            print("Just lightly touching the table causes it to creak and shamble in place.")
            print("With nothing else around the table you decide to leave it.")
            print("")

        # Check exit input
        elif player_choice == 3:
            game_start()

        # Display inventory as a message
        elif player_choice == 4:
            print(inventory)

        else:
            # Improper input warning message
            print("There was an issue with your response. Please type a number without punctuation.")


def white_room(members):
    """
    Removes and adds list items based on an equal condition, and gives the user input for more choices.
    :param members: The inventory list of items
    :return: The inventory list of items
    """
    print("")
    print("You're in the white sci-fi room.")
    print("The room looks sparsely filled with usable objects, but the protruding panels and bright lights make it feel more claustrophobic than it otherwise should.")
    print("The only objects of note are what appear to be an intercom system and a 3D printer that looks to be dysfunctional.")
    print("What will you do?")
    print("")
    # Loop through conditions until user's input matches one
    while True:
        while True:
            # Loop through user input until they enter an appropriate integer
            if "Shiny Key" in str(inventory) and not p_lock_locked:
                print("After looking for any possible reaction to your use of the stone, you notice the panels in the white room shifted around oddly.")
                print("The panels on the wall furthest from the door were now moved to the sides of a door.")
                print("You run up to the door and try to open it. It's locked.")
                print("You try the shiny key you have on the door's lock.")
                print("It unlocks and behind the door... is the outside world!")
                print("Now to find whoever put you in there.")
                print("To be continued...")
                main()
            else:
                break

        while True:
            # Check user input for usable input
            try:
                # Variable to store user input
                player_choice = int(input("1. Inspect intercom system | 2. Inspect 3D printer | 3. Exit room | 4. Check inventory: "))
                # Break off from loop
                break
            # Catch exceptions from improper user input
            except Exception:
                # Message to warn user about improper input
                print("There was an issue with your response. Please type a number without punctuation.")

        if player_choice == 1:
            print("")
            print("You approach the intercom. You say a few words hoping to reach someone but it seems useless.")
            print("However, upon getting a closer look, your ear picks up what sounds like rustling noises and light breathing on the other end.")
            print("Though there is still no response to continued attempts at communication, perhaps there is something that can be used to illicit a response.")
            print("")
            # Loop through list checking conditions and user inputs to use the items
            while True:
                try:
                    # Check inventory index for Voice Recorder item
                    if "Voice Recorder" in str(inventory):
                        # Ask the user if they want to use the item
                        use_item = input("You think that the voice recorder could be used to get a response. Use it? yes/no ").lower()
                        print("")
                        # Verify user input as yes to exchange the voice recorder for a key
                        if use_item == "yes":
                            # Check each item in the inventory list that was given to the members parameter of the function
                            for memb in members:
                                # Verify if the item is the voice recorder
                                if memb == "Voice Recorder":
                                    # Removes voice recorder and adds curved key to inventory
                                    inventory[2] = "Curved Key"
                                    # Print narration messages
                                    print("")
                                    print("After a moment of playing the recorded voice, all noise behind the intercom goes silent.")
                                    print("A half-minute or so goes by before you hear a scratchy voice say, 'I haven't heard that voice in ages...'")
                                    print("You hear a loud mechanical noise expelling air. When you turn around you see a square panel in the wall about a foot or so long on each side has opened.")
                                    print("The voice grabs your ear again and says, 'please put that recorder in the that opening. I'll give you something in return.'")
                                    print("You've gone this far you might as well go all the way, you think to yourself.")
                                    print("The opening in the wall on closer inspection, while dark, is only a few inches deep.")
                                    print("You place the recorder in and as you step back it closes up immediately. More mechanical noises arise and a clinking noise happens behind you.")
                                    print("'Hope it helps,' says the voice as the intercom goes silent for a final time.")
                                    print("You look around and notice something on the 3D printer. You pick up the object which appears to be an oddly curved key.")
                                    print("Not only was the key odd, but the once thought to be broken 3D printer not only appeared to have made a key but in only a few seconds.")
                                    print("Despite that, the printer does not seem to be operable from within the room and is still useless to you. You leave the room.")
                                    print("")
                                    # Return the altered list items to the inventory
                                    return inventory

                                else:
                                    continue
                        # Go back to choices
                        elif use_item == "no":
                            print("You decide to look elsewhere.")
                            break

                        else:
                            # Improper input warning message
                            print("There was an issue with your input. Please try typing yes or no again.")
                    # If the user has no voice recorder move back to the choices
                    else:
                        break
                # Catch exceptions and go back to this room's choices
                except Exception:
                    print("")
                    # Break from loop and return to choices
                    break

        # Check option 2 input
        elif player_choice == 2:
            # Print narration messages
            print("")
            print("You inspect the 3D printer. Unfortunately, it really does look unusable.")
            print("If only you could print a master key, a cellphone, or some other tool to escape.")
            print("After spending a few minutes looking around the printer in hopes of some solution it looks as though it won't be of any use.")
            print("")

        # Check exit input
        elif player_choice == 3:
            game_start()

        elif player_choice == 4:
            print(inventory)

        else:
            # Improper input warning message
            print("There was an issue with your response. Please type a number without punctuation.")


def black_room():
    """
    Function that removes list items based on user input and first or second time experience
    """
    # Make global variables accessible to local scope
    global p_lock_locked
    global first_time_dark

    print("You're in the pitch black room.")
    print("Despite being very dark, there is a small light at the end of the room on top of some kind of table")
    print("What will you do?")
    # Loop through conditions until user's input matches one
    while True:
        # Loop through user input until they enter an appropriate integer
        while True:
            # Check user input for usable input
            try:
                # Variable to store user input
                player_choice = int(input("1. Inspect Glowing Table | 2. Exit room | 3. Check inventory: "))
                # Break off from loop
                break
            # Catch exceptions from improper user input
            except Exception:
                # Message to warn user about improper input
                print("There was an issue with your response. Please type a number without punctuation.")

        if player_choice == 1:
            # Checks if this is the first time the player has chosen this choice
            if int(first_time_dark) == 1:
                # Print narration messages
                print("You find a desk with a light illuminating from an unknown source. On top of the desk is what looks like a voice recorder.")
                print("Before touching anything you look around the desk and notice a single drawer with a lock on the front.")
                print("Eventually you pick up the voice recorder, but before being able to inspect it, a voice booms throughout the room.")
                print("'Your time is running out, you should hurry,' said the voice followed by a laugh.")
                print("Already frenzied by the sudden voice, there was now a feeling a nausea. However, this was not from the voice, but from the odd smoke filling the room.")
                print("You dash out of the room and close the door behind you. It's probably time to check out somewhere else...")
                # Add voice recorder to inventory
                inventory[2] = "Voice Recorder"
                print("")
                # Set first time dark variable false to prevent the first time messages from displaying again
                first_time_dark = 0

            # Print message after user tries to access input 1 after doing the first attempt
            elif first_time_dark == 0:
                print("")
                print("'I don't want to go back in there...'")

            else:
                print("Try again.")
                break

            # Loop through list checking conditions and user inputs to use the items
            while True:
                try:
                    # Check inventory index for curved key item
                    if "Curved Key" in str(inventory):
                        print("However, after being driven out of the room previously, you decide it might be worth checking out the dark room again.")
                        print("You enter and make your way straight to the desk.")
                        # Ask the user if they want to use the item
                        use_key = input("You think that the curved key could be used to open the drawer. Use it? yes/no ").lower()
                        print("")
                        # Verify user input as yes to use the curved key
                        if use_key == "yes":
                            # Remove cursed key from inventory
                            inventory[2] = ""
                            print("You attempt to slide the key into the desk drawer lock.")
                            print("Surprisingly, it goes in without trouble. However, upon unlocking the drawer, the key breaks!")
                            print("You attempt to pull out the desk drawer, and instead pull the entire thing out.")
                            print("The drawer falls on the floor with a thud and inside the desk is a protruding piece of circular wood")
                            print("You reach for it and when you place your hand on it it easily pushes into the wood below it.")
                            print("Realizing its a pressure sensor you think you could get somewhere if you placed the stone on it.")
                            # Ask user to use stone
                            use_stone = input("Use the stone? yes/no: ")
                            # Verify user input to use stone
                            if use_stone == "yes":
                                # Remove stone from inventory list
                                inventory[0] = ""
                                print("For once, nothing seemed to happen due to your interference.")
                                print("You leave the room hoping to find out if something happened somewhere else.")
                                # Unlock the final lock by setting the locked variable to False instead of True
                                p_lock_locked = 0

                            # Go back to choices
                            elif use_stone == "no":
                                print("You decide to look elsewhere.")

                            else:
                                print("There was an issue with your input. Please try typing yes or no again.")

                        # Go back to choices
                        elif use_key == "no":
                            print("You decide to look elsewhere.")
                            break

                        else:
                            # Improper input warning message
                            print("There was an issue with your input. Please try typing yes or no again.")
                    # If the user has no curved key move back to the choices
                    else:
                        break
                # Catch exceptions and go back to this room's choices
                except Exception:
                    print("")
                    # Break from loop and return to choices
                    break

        # Check option 2 input to exit
        elif player_choice == 2:
            game_start()

        elif player_choice == 3:
            print(inventory)

        else:
            # Improper input warning message
            print("There was an issue with your response. Please type a number without punctuation.")


def wood_room(members):
    print("You're in the wood room.")
    print("The room contains a small potted tree in the center. On one of the wooden walls is a sign saying, 'Please keep the tree watered.")
    print("")
    print("What will you do?")
    # Loop through conditions until user's input matches one
    while True:
        # Loop through user input until they enter an appropriate integer
        while True:
            # Check user input for usable input
            try:
                # Variable to store user input
                player_choice = int(input("1. Inspect tree | 2. Exit room | 3. Check inventory: "))
                # Break off from loop
                break
            # Catch exceptions from improper user input
            except Exception:
                # Message to warn user about improper input
                print("There was an issue with your response. Please type a number without punctuation.")

        # Check user input to option one's number
        if player_choice == 1:
            print("You look at the tree and its only about as half as tall as you.")
            print("The tree looks as though it had not been watered in a long time.")
            print("You try to move the tree but find that its stuck to the ground. Rather than take the chance to destroy it you back off.")
            print("")
            # Loop through list checking conditions and user inputs to use the items
            while True:
                try:
                    # Check inventory index for water bottle item
                    if "Water Bottle" in str(inventory):
                        # Ask the user if they want to use the item
                        use_item = input("You think that the water bottle could be used to water the tree. Use it? yes/no ").lower()
                        print("")
                        # Verify user input as yes to exchange the water bottle for a key
                        if use_item == "yes":

                            # Check each item in the inventory list that was given to the members parameter of the function
                            for memb in members:
                                # Verify if the item is the water bottle
                                if memb == "Water Bottle":
                                    # Remove water bottle and add shiny key to inventory list
                                    inventory[1] = "Shiny Key"
                                    # Print narration messages
                                    print("You water the tree with the water you stored in the bottle.")
                                    print("Nothing appears to happen, however, as the water seeps into the pot's soil you see a small compartment open up on the side of the pot.")
                                    print("You stare at it for a moment as a bit of dirt falls out.")
                                    print("You reach a couple of fingers into the compartment and feel something small and metallic.")
                                    print("You pull it out and find that it is a very shiny key.")
                                    # Return the altered list items to the inventory
                                    return inventory

                                else:
                                    continue

                        # Go back to choices
                        elif use_item == "no":
                            print("You decide to look elsewhere.")
                            break

                        else:
                            # Improper input warning message
                            print("There was an issue with your input. Please try typing yes or no again.")
                    # If the user has no voice recorder move back to the choices
                    else:
                        break
                # Catch exceptions and go back to this room's choices
                except Exception:
                    print("")
                    # Break from loop and return to choices
                    break

        # Check exit input
        elif player_choice == 2:
            game_start()

        elif player_choice == 3:
            print(inventory)

        else:
            # Improper input warning message
            print("There was an issue with your response. Please type a number without punctuation.")


def game_start():
    # Make inventory variable available to local scope
    global inventory

    # Loop through user input conditions
    while True:
        print("Your options are: \n 1. Flame Painted Door \n 2. Water Painted Door \n 3. Grey Metal Door \n 4. White Sci-Fi Door \n 5. Pitch Black Door \n 6. Normal Wood Door \n 7. View Inventory \n 8. Exit Game \n 9. Save Game \n (Input the corresponding number) ")
        # Loop until user gives a usable input
        while True:
            try:
                player_choice = int(input("Which door will you go in?: "))
                break
            except Exception:
                print("There was an issue with your response. Please type a number without punctuation.")
        # Check user input to see if it matches room number
        if player_choice == rooms_tuple[0]:
            # Execute flame room function
            flame_room()

        # Check user input to see if it matches room number
        elif player_choice == rooms_tuple[1]:
            # Execute water room function
            water_room()

        # Check user input to see if it matches room number
        elif player_choice == rooms_tuple[2]:
            # Execute metal room function and give it the inventory list argument for its parameter
            inventory = metal_room(inventory)
            metal_room(inventory)

        # Check user input to see if it matches room number
        elif player_choice == rooms_tuple[3]:
            # Execute white room function and give it the inventory list argument for its parameter
            inventory = white_room(inventory)
            white_room(inventory)

        # Check user input to see if it matches room number
        elif player_choice == rooms_tuple[4]:
            # Execute black room function
            black_room()

        # Check user input to see if it matches room number
        elif player_choice == rooms_tuple[5]:
            # Execute wood room function and give it the inventory list argument for its parameter
            inventory = wood_room(inventory)
            wood_room(inventory)

        # Check user input to see if it matches option number
        elif player_choice == 7:
            # Print contents of the inventory list
            print(inventory)

        # Check user input to see if it matches option number
        elif player_choice == 8:
            # Exit the game
            exit()

        # Checks player input for matching value
        elif player_choice == 9:
            # Opens the file at the directory path for writing and then closes when finished
            with open(abspath, 'w+') as f:
                # Loops to write each item in the inventory to the save file
                for i in inventory:
                    # Writes the item from the inventory list to the file
                    f.write(i + "\n")
                # Writes the single value of each variable to a line in the file
                f.write(str(p_lock_locked) + "\n")
                f.write(str(first_time_flame) + "\n")
                f.write(str(first_time_water) + "\n")
                f.write(str(first_time_dark) + "\n")
            
            print("")
            print("Your progress has been saved.")
            print("")


        else:
            print("There was an issue with your input, please try again.")


def main():
    # Give access to global variables on local scope
    global inventory
    global progress_gates
    global p_lock_locked
    global first_time_flame
    global first_time_water
    global first_time_dark

    print("Welcome to the Roundabout Adventure.")
    while True:

        play_game = input("Would you like to play? Yes/No | If you'd like to load a previous save type load: ").lower()
        # Sets variable values and starts game if user input is yes
        if play_game == "yes":
            # Sets list to empty values
            inventory = ["", "", ""]
            # Sets locks to 1
            p_lock_locked = 1
            first_time_flame = 1
            first_time_water = 1
            first_time_dark = 1

            game_start()
        
        # Quits game
        elif play_game == "no":
            exit()

        # Loads data from save file
        elif play_game == "load":
            inventory
            # Reads the data from the file at the absolute path
            with open(abspath, 'r+') as f:
                # Reads the lines in order from the first in the save file and sets the read value to the list index
                inventory[0] = f.readline().strip()
                inventory[1] = f.readline().strip()
                inventory[2] = f.readline().strip()
                # Reads lines and sets more values to specific list indexes
                progress_gates[0] = f.readline().strip()
                progress_gates[1] = f.readline().strip()
                progress_gates[2] = f.readline().strip()
                progress_gates[3] = f.readline().strip()

                # Ensures a conversion from the read value in the progress gate variables to be an integer, and then stores them in their respective variable
                p_lock_locked = int(progress_gates[0])
                first_time_flame = int(progress_gates[1])
                first_time_water = int(progress_gates[2])
                first_time_dark = int(progress_gates[3])
       
            game_start()

        else:
            # Warning message to user based on improper input
            print("There was an issue with your answer. Try typing yes or no again.")


main()
