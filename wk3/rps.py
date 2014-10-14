import random

class Player:
	def __init__(self):
		self.hand = ""
		
	def play(self):
		throw = ["rock", "paper", "scissors"]
		self.hand = throw[random.randint(0,2)]

def rochambeau(p1,p2,score):
	p1.play()
	p2.play()
	if p1.hand == "rock":
		if p2.hand == "paper":
			score[1] += 1
		if p2.hand == "scissors":
			score[0]+= 1

	if p1.hand == "paper":
		if p2.hand == "scissors":
			score[1] += 1
		if p2.hand == "rock":
			score[0]+= 1

	if p1.hand == "scissors":
		if p2.hand == "rock":
			score[1] += 1
		if p2.hand == "paper":
			score[0]+= 1

p1 = Player()
p2 = Player()
score = [0, 0]

while sum(score) < 3:
	rochambeau(p1,p2,score)

print score