#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
import random

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
			print("True")
			return True
		else:
			print("False")
			return False


"""'''''''''''''''''''''''''''''''''''''''''''''
	An abstract class to maintain Weapon data
'''''''''''''''''''''''''''''''''''''''''''''"""
class HershyKisses(Weapon):
	def __init__(self):
		self.name = "Hershy Kiss"
		self.attackModifier = 1
		self.MAX_USE = float("inf")

	
"""'''''''''''''''''''''''''''''''''''''''''''''
	An abstract class to maintain Weapon data
'''''''''''''''''''''''''''''''''''''''''''''"""
class SourStraWS(Weapon):
	def __init__(self):
		self.name = "Sour Straw"
		self.attackModifier = random.uniform(1, 1.75)
		self.MAX_USE = 2

	
"""'''''''''''''''''''''''''''''''''''''''''''''
	An abstract class to maintain Weapon data
'''''''''''''''''''''''''''''''''''''''''''''"""
class ChocolateBars(Weapon):
	def __init__(self):
		self.name = "Chocolate Bar"
		self.attackModifier = random.uniform(2, 2.4)
		self.MAX_USE = 4



"""'''''''''''''''''''''''''''''''''''''''''''''
	An abstract class to maintain Weapon data
'''''''''''''''''''''''''''''''''''''''''''''"""
class NerdBombs(Weapon):
	def __init__(self):
		self.name = "Nerd Bomb"
		self.attackModifier = random.uniform(3.5, 5)
		self.MAX_USE = 1

	
		