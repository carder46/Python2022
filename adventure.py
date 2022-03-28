#import all the functions from adventurelib
from adventurelib import *

################
#DEFINE ROOM
################

outside = Room("You are standing facing the house, it is warm and human, you hear the bystanders mourning the loss. Talk to the police chief.")
entryway = Room("You are in the entryway. It is clean and nothing has been touched.")
kitchen = Room("You enter the kitchen, looks normal. However a knife is missing from the magnetic stand.")
diningroom = Room("You are in the dining room, the curtains are moving as if there is a gust of wind behind them.")
livingroom = Room("You are in the living room, this house is oddly clean from a crime scene. What's that smell? A light odour seems to be coming from the east.")
masterbedroom = Room("You enter the master bedroom, the smell is alot stronger now. The curtains are still closed but it's midday, a glass of water is resting on the bedside table and a netflix movie is playing on the TV. The bed is unmade and still messy, what's happening?")
ensuite = Room("You enter the ensuite. There is a handprint on the shower curtain, what is that smell? It's even stronger now, it is unbearable.")
courtyard = Room("You are in the courtyard, a nice break from inside with fresh air and nice smelling flowers.")
guestbedroom = Room("You are in the guest bedroom, there is a rug, however the room looks normal.")
guestensuite = Room("You enter the guest enuite, nothing interesting here.")


################
#ROOM CONNECTIONS
################
outside.north = entryway
entryway.north = livingroom
entryway.east = kitchen
entryway.south = outside
entryway.west = diningroom
masterbedroom.north = ensuite
masterbedroom.west = livingroom
livingroom.east = masterbedroom
livingroom.south = entryway
livingroom.north = courtyard
livingroom.west = guestbedroom
diningroom.east = entryway
diningroom.north = guestbedroom
guestbedroom.north = guestensuite
guestbedroom.south = diningroom
courtyard.south = livingroom
courtyard.west = guestensuite


################
#VARIABLE
################
current_room = outside

################
#OUTSIDE
################ 
#@when("go north")
#def jump():
#	print("You jump")

@when("talk to")
@when("talk to chief")
@when("talk to police chief")
def police_chief():
	global current_room
	if current_room == outside:
		print("Hello, Detective. This is the first murder case that has occurred in the town in 30 years. We do not have an established Investigation Bureau so I thank you kindly for choosing to come and lead this investigation. Due to safety standards, we are yet to enter the house so cannot provide the location of the body. Please find the body and report it back to us as soon as possible, thank you.\n TIP : Use 'inspect' to find clues about the room that you are in.\n TIP : Use 'exits' to find available exits!")

@when("enter house")
@when("enter home")
@when("enter door")
def enter_entryway():
	global current_room
	if current_room == outside:
		print("You enter the house, good luck Detective")
		current_room = entryway
	else: 
		print("There is no house here")
	print(current_room)

################
#INSPECT
################ 
@when("inspect")
@when("look")
@when("search")
def inspect():
	global current_room
	if current_room == entryway:
		print("Nothing interesting here, maybe we should move on.")
	if current_room == kitchen:
		print("Hmm, the dishwasher is beeping...")
	if current_room == dining:
		print("The curtains are moving as if there is wind blowing behind them...")



@when("dishwasher")
@when("search dishwasher")
@when("look in dishwasher")
def dishwasher():
	global current_room
	if current_room == kitchen:
		print("You find:\n - The missing knife blade from the stand. \n - A bunch of clean dishes. \n")


@when("go to curtains")
@when("inspect curtains")
@when("open curtains")
def dining():
	global current_room
	if current_room == dining:
		print("You find :\n - A smashed window.\n")

################
#BINDS
################ 
@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		#checks if the current room list of exits has
		#the direction the player wants to go
		current_room = current_room.exit(direction)
		print(f"You go {direction}")
		print(current_room)
	else:
		print("You cannot go that way.")

@when ("exits")
def exits():
	print(current_room)
	print("There are exits, to the ",current_room.exits())

	

################
#MAIN FUNCTION
################

def main():
	print(current_room)
	start()
	#start the main loop

main()