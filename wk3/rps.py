import random

class Player:
	def __init__(self, name, play):
		self.name = name
		self.play = play
		
	def rochambeau(self):
		throw = ["rock", "paper", "scissors"]
		self.play = throw[random.randint(0,2)]

sara = Player("Sara", "scissors")
bruce = Player("Bruce", "rock")

sara.rochambeau()
bruce.rochambeau()

if 