import random

throws = ["rock", "paper", "scissors"]
score = [0,0]

player1 = throws[random.randint(0,2)]
player2 = throws[random.randint(0,2)]

if player1 == "rock":
	if player2 == "paper":
		score[1] += 1
	if player2 == "scissors":
		score[0]+= 1

if player1 == "paper":
	if player2 == "scissors":
		score[1] += 1
	if player2 == "rock":
		score[0]+= 1

if player1 == "scissors":
	if player2 == "rock":
		score[1] += 1
	if player2 == "paper":
		score[0]+= 1

player1 = throws[random.randint(0,2)]
player2 = throws[random.randint(0,2)]

if player1 == "rock":
	if player2 == "paper":
		score[1] += 1
	if player2 == "scissors":
		score[0]+= 1

if player1 == "paper":
	if player2 == "scissors":
		score[1] += 1
	if player2 == "rock":
		score[0]+= 1

if player1 == "scissors":
	if player2 == "rock":
		score[1] += 1
	if player2 == "paper":
		score[0]+= 1

player1 = throws[random.randint(0,2)]
player2 = throws[random.randint(0,2)]

if player1 == "rock":
	if player2 == "paper":
		score[1] += 1
	if player2 == "scissors":
		score[0]+= 1

if player1 == "paper":
	if player2 == "scissors":
		score[1] += 1
	if player2 == "rock":
		score[0]+= 1

if player1 == "scissors":
	if player2 == "rock":
		score[1] += 1
	if player2 == "paper":
		score[0]+= 1

print score