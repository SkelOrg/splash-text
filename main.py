import sys
import json
import random

file = open("data.json","r") # gets and reads the JSON file
possibletext = json.load(file) # gets the text from JSON file and stores into array
file.close()

randnum = random.randint(0, len(possibletext) - 1) # generates a random number between 0 and the amount of items in the list
print(possibletext[randnum]) # gets a random item with the random number (items[numberofitem])
