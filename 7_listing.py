'''#1
fibonacci = ["0","1","1","2","3","5","8","13","21","34"]
print(fibonacci)
#2
fruit = ["pineapple","mango","pear","dragonfruit","apple"]
print(fruit)
#3
yter = ["walterbonk","Mankeyman56235","Carter♦D Gaming","ultraformula1"]
print(yter)
#4
song = []
song.append("Fortnite Battle Pass")
song.append("505")
song.append("Baby")
song.append("MaoZeDong")
#5
books = []
books.append(input("Name a book.\n"))
books.append(input("Name a book.\n"))
books.append(input("Name a book.\n"))
books.append(input("Name a book.\n"))
books.append(input("Name a book.\n"))
print(books)
#6
print("Hi, welcome to Pizza Maker")
order_complete = False
pizza_toppings = []

while order_complete == False:
	topping = input("What topping? - push enter to finish")
	if topping == "": #if the user pushes enter, the order is done
		print("Order Done")
		order_complete = True
	elif topping in pizza_toppings: #check if topping exists already
		print("You already have that topping")
	else: #add to list if not
		print("Great, adding it to the list")
		pizza_toppings.append(topping)
print("Here are your toppings")
#this next line might be new
#it joins the list together and seperates
#with commas, but you can change the seperator
print(",".join(pizza_toppings))'''
#8
names = ["Asheen","Ashwin","Asharn","Ashan","Ashane"]
print(names)
names.sort()
print(names)
names.reverse()
print(names)