""" Task 1
	In this task, you'll learn to:
		- import a module,
		- define a list, use an if/else statement
		- use the randrange method of the random module
		- use Python's built-in len() and print() functions
"""

# import random module from Python standard library
import random

# define a list of image urls (i.e. list of strings)
images = ["img1", "img2", "img3"]

# set the served img variable to be a random element from imgs
served_img = images[random.randrange(0,len(images)-1)]

# output the img
print(served_img)


# --- Task 2 starts here ->

# ask if user wants to fluck it
question = input("would you want to fluck it?")

# if they said yes, output a message...
if question == "yes":
	print("It has been flucked!")
else:
	print("It has not been flucked :(")	# else, output a different message...

