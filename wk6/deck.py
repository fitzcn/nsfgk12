# coding: utf-8
import random

deck = ["A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠",
"A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
"A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦",
"A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣"]

def printEach(lst):
	for item in lst:
		print item

def printEachInReverse(lst):
	lst.reverse()
	printEach(lst)
	lst.reverse()

def selectRandom(lst):
	index = random.randint(0,51)
	print lst[index]


printEach(deck)
printEachInReverse(deck)
printEach(deck)
selectRandom(deck)