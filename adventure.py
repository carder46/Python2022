#import all the functions from adventurelib
from adventurelib import *

################
#DEFINE ROOM
################
#this describes the room as the player enters it, eg the courtyard description will show as they 'walk' into the courtyard
Room.items = Bag()
outside = Room("You are standing facing the house, it is warm and humid, you hear the bystanders mourning the loss. Talk to the police chief.")
entryway = Room("You are in the entryway. It is clean and nothing has been touched.")
kitchen = Room("You enter the kitchen, looks normal. However a knife is missing from the magnetic stand.")
diningroom = Room("You are in the dining room, the curtains are moving as if there is a gust of wind behind them.")
livingroom = Room("You are in the living room, this house is oddly clean from a crime scene. What's that smell? A light odour seems to be coming from the east.")
masterbedroom = Room("You enter the master bedroom, the smell is alot stronger now. The curtains are still closed but it's midday, a glass of water is resting on the bedside table and the TV is playing. The bed is unmade and still messy, what's happening?")
ensuite = Room("You enter the ensuite, is this vanity a LEVIVI LEEDS FLOOR-STANDING 400MM VANITY $392.00 from plumbingworld.co.nz??")
courtyard = Room("You are in the courtyard, a nice break from inside with fresh air and nice smelling flowers.")
guestbedroom = Room("You are in the guest bedroom, there is a rug, however the room looks normal.")
guestensuite = Room("You enter the guest enuite, nothing interesting here.")


################
#ROOM CONNECTIONS
################
#these are variables that store which direction a player must go from each team.
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
#this section includes variables for when the game begins, the player starts outside and the photo is not taken, hence the 'False'
current_room = outside
photo_taken = False
inventory = Bag()


################
#ITEMS
################
#this creates the item called camera
camera = Item("camera","cam","c")
camera.description = ("The crime scene camera use to take photos of the body")

#this adds the camera item to the outside room
outside.items.add(camera)

#this allows the player to pick the camera up and take it
@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def get_item(item):
	if item == "photo" and "camera" in inventory:
		use("camera")
		return
	if item in current_room.items:
		t = current_room.items.take(item)
		print(t)
		inventory.add(t) #this adds the camera to the inventory
		print(f"You take the {item} from the police chief.")
	else:
		print("There is no camera here, you have to get it outside from the police chief.")


#this allows the player to check their inventory to make sure they either have items, or have no items.
@when("inventory")
def check_inventory():
	print("You have")
	for item in inventory:
		print(item)

#this code is for the end when the player finds the body and needs to take a photo.
@when("use ITEM")
def use(item):
	global photo_taken
	if inventory.find(item)==camera and current_room == ensuite:
		print("You take a photo of the body lets get going.")
		photo_taken = True
		print("Look at your available exits, navigate your way out of the house.")
	else:
		print("Save the camera memory, use it when you find the body.")


@when("talk to")
@when("talk to chief")
@when("talk to police chief")
def talkto():
	if photo_taken == True and current_room == outside:
		print("I am glad you are back, did you find the body? I assume that you have, can I have the camera?")
	if photo_taken == False:
		if current_room == outside:
			print("Hello, Detective. This is the first murder case that has occurred in the town in 30 years. We do not have an established Investigation Bureau so I thank you kindly for choosing to come and lead this investigation. Due to safety standards, we are yet to enter the house so cannot provide the location of the body. Please find the body and report it back to us as soon as possible, thank you.\n TIP : Use 'inspect' to find clues about the room that you are in.\n TIP : Use 'exits' to find available exits!")
			print("Take this camera, take a photo when you find it and bring it back.")
		else:
			print("I am glad you are back, did you find the body? I assume that you have, can I have the camera?")

@when("talk to cheif")
@when("talk to police cheif")
def talktoWRONG():
	if current_room == outside:
		print("Learn to spell, it's CHIEF")
		
@when("give ITEM")
@when("hand ITEM")
def give(item):
	if photo_taken == False and current_room == outside:
		print("There is no photo here? Whatever, I will just get someone else to do it for me. Don't come back here, do your job next time.")
		quit()	
	if photo_taken == True and current_room == outside:
		print("Thank you, let me look at the photo now...\n This is perfect, thank you. One more thing...\n *BANG*\n *your vision goes black*\n To be continued...")
		quit()
	

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

@when("go through window")
@when("jump out of window")
@when("jump out window")
def windowjump():
	if current_room == diningroom:
		print("You ")
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
	if current_room == diningroom:
		print("The curtains are moving as if there is wind blowing behind them...")
	if current_room == livingroom:
		print("You see :\n - A grey rug that has been tampered with.")
	if current_room == masterbedroom:
		print("Gosh, what is that smell, we should really hurry up because this is unbearable.")
	if current_room == ensuite:
		print("This has to be it, there is blood everywhere. There is a handprint on the shower curtain, but the shower curtain is closed.")
	if current_room == outside:
		print("How about we just get inside first, the door is infront of you.")
	if current_room == courtyard:
		print("Wow, peaceful, I could definitely get used to this.\n You see:\n Birds, bees, flowers, a pool, a poolhouse, but nothing related to the crime. MOVE IT.")
	if current_room == guestbedroom:
		print("That bed looks really comfy... maybe I should sleep there for a bit.")
	if current_room == guestensuite:
		print("Ordinary boring bathroom, very nicely designed, however.")


@when("go to shower curtain")
@when("open shower curtain")
@when("rip down shower curtain")
def showercurtain():
	global current_room
	if current_room == ensuite:
		print("There he is, you have found the body, let's take a photo for the police chief and get out of here.")

@when("go to grey rug")
@when("search grey rug")
@when("look at grey rug")
@when("go to rug")
@when("search rug")
@when("look at rug")
def rug():
	global current_room
	if current_room == livingroom:
		print("You see :\n - A muddy footprint that seems to have come from a tramping boot of some sort, the footprint is facing in the direction of east.")

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
	if current_room == diningroom:
		print("You find :\n - A smashed window.\n")

@when("lift rug")
def lift_rug():
	global current_room
	if current_room == livingroom:
		print("Nothing under here, search the rug.")

@when("drink water")
def water():
	global current_room
	if current_room == masterbedroom:
		print("Ew, that's disgusting, drinking a dead mans water. Turns out it was drugged and you die. \n TIP : Don't drink water from a dead guys house.")
		quit()

@when("look at tv")
@when("watch tv")
def tv():
	global current_room
	if current_room == masterbedroom:
		print("You look at the TV, he's been watching Ashane De Silva's tiktoks. He can't even dance, please turn the TV off...")

TVon = True

@when("turn on tv")
@when("turn on")
def tvturnon():
	if current_room == masterbedroom and TVon == True:
		print("You can't turn on a TV that is already on, it's kind of common sense?")
	elif current_room == masterbedroom and TVon == False:
		print("Don't even try, turns out the TV remote shorted and you die. Lesson Learnt?")
		quit()

@when("turn off tv")
@when("turn off")
def tvturnoff():
	global TVon
	if current_room == masterbedroom:
		TVon = False
		print("You turn off the TV, thank you.")

@when("make bed")
def bed():
	global current_room
	if current_room == masterbedroom:
		print("Aren't you a detective? You make the bed, looks nice, maybe you should be a housewife/husband.")
		masterbedroom.description = "The room still smells horrible, but atleast now you have made the bed, so it looks somewhat presentable."

@when("sleep in bed")
@when("sleep")
def sleep():
	global current_room
	if current_room == guestbedroom:
		print("You sleep in the bed, the murderer comes back and you die. Stay attentive next time.")
		quit()

@when("eggs")
def egg():
	eggs = input("Do you like scrambled eggs?\n")
	if eggs.lower() == "yes":
		print("ARGHHHHHHHHHHHHHH scrambled eggs are like eating rubber")
		quit()
	else:
		print("Good, yay, you win!!")
		quit()
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

@when("give up")
def giveup():
	print("You give up, farewell, Detective.")
	quit()
################
#MAIN FUNCTION
################

def main():
	print(current_room)
	start()
	#start the main loop

main()




