#import all the functions from adventurelib
from adventurelib import *

#rooms
space = Room("You are drifting in space. You see a spaceship")
airlock = Room("You are in an airlock")
cargo = Room("You are in the cargo bay")
docking = Room("You are in the docking bay")
hallway = Room("You are in the spaceship hallway")
quarters = Room("You are in the crew quarters, there is a locker.")
bridge = Room("You are on the bridge, there is a sussy dead body")
escape_pods = Room("You are in the escape pods")
mess_hall = Room("You are in the mess hall #YummyInMyTummy")

#room connections
docking.west = cargo
hallway.north = cargo
hallway.east = bridge
hallway.south = mess_hall
hallway.west = airlock
bridge.south = escape_pods
mess_hall.west = quarters
quarters.north = airlock


#variables
current_room = space

#binds 
@when("jump")
def jump():
	print("You jump")

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_airlock():
	global current_room
	if current_room == space:
		print("You haul yourself into the airlock")
		current_room = airlock
	else: 
		print("There is no airlock here")
	print(current_room)

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

@when ("look")
def look():
	print(current_room)
	print("There are exits, to the {",".join(current_room.exits())}")

	

#EVERYTHING GOES ABOVE HERE - DO NOT CHANGE
#ANYTHING BELOW THIS LINE
#the main function
def main():
	print(current_room)
	start()
	#start the main loop

main()