import random

class Die:
	def __init__(self, numSides):
		self.numSides = numSides
		self.value = random.randint(1,numSides)
	def rollDie(self):
		self.value = random.randint(1,self.numSides)

def rollCup(cup):
	for die in cup:
		die.rollDie()

def printCup(cup):
	roll = ""
	for die in cup:
		roll += str(die.value) + " "
	print(roll)

die1 = Die(6) 
die2 = Die(6)
die3 = Die(6)
die4 = Die(6)
die5 = Die(6)

cup = [die1, die2, die3, die4, die5]

for i in range(1,4):
	printCup(cup)
	rollCup(cup)