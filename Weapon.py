#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
from random import randint

"""'''''''''''''''''''''''''''''''''''''''''''''
	An abstract class to maintain Weapon data
'''''''''''''''''''''''''''''''''''''''''''''"""
class Weapon(object):

	__metaclass__ = ABCMeta

	name = ""
	attackModifier = 0
	timesUsed = 0
	MAX_USE = 0

	# Checks if an instance has uses left. Returns true if it still has use left. Returns false if it has no more uses. TODO - Somewhere if false notify something. 
	def hasUsesLeft(self):
		if self.timesUsed < self.MAX_USE:
			return True
		else:
			return False

	def getName(self):
		return self.name

	def getAttackModifier(self):
		return self.attackModifier

	def getTimesUsed(self):
		return self.timesUsed

	def setTimesUsed(self, times):
		self.timesUsed += times

	def getMaxUse(self):
		return self.MAX_USE


"""'''''''''''''''''''''''''''''''''''''''''''''
	A class to maintain HershyKiss data
'''''''''''''''''''''''''''''''''''''''''''''"""
class HershyKisses(Weapon):
	def __init__(self):
		self.name = "Hershy Kiss"
		self.attackModifier = 1
		self.MAX_USE = float("inf")

	
"""'''''''''''''''''''''''''''''''''''''''''''''
	A class to maintain SourStraw data
'''''''''''''''''''''''''''''''''''''''''''''"""
class SourStraWS(Weapon):
	def __init__(self):
		self.name = "Sour Straw"
		self.attackModifier = randint(100,175)/100
		self.MAX_USE = 2

	
"""'''''''''''''''''''''''''''''''''''''''''''''
	A class to maintain ChocolateBar data
'''''''''''''''''''''''''''''''''''''''''''''"""
class ChocolateBars(Weapon):
	def __init__(self):
		self.name = "Chocolate Bar"
		self.attackModifier = randint(200, 240)/100
		self.MAX_USE = 4



"""'''''''''''''''''''''''''''''''''''''''''''''
	A class to maintain NerdBomb data
'''''''''''''''''''''''''''''''''''''''''''''"""
class NerdBombs(Weapon):
	def __init__(self):
		self.name = "Nerd Bomb"
		self.attackModifier = randint(350, 500)/100
		self.MAX_USE = 1

	
		