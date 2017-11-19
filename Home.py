#!/usr/bin/env python3

import Monster
from random import randint

class Home(object):

	
	"""'''''''''''''''''''''''''''''''''''''''''''''
	Initialize the Home object
	Creates a list of 10 random monsters for the Home
	'''''''''''''''''''''''''''''''''''''''''''''"""
	def __init__(self):
		self.monsterList = []
		for x in range(10):
			tmp = randint(1, 5)
			if tmp == 1:
				self.monsterList.append(Monster.Zombie())
			elif tmp == 2:
				self.monsterList.append(Monster.Vampire())
			elif tmp == 3:
				self.monsterList.append(Monster.Ghoul())
			elif tmp == 4:
				self.monsterList.append(Monster.Werewolf())
			elif tmp == 5:
				self.monsterList.append(Monster.Person())


	"""'''''''''''''''''''''''''''''''''''''''''''''
	A method to print the Home's monster list for testing
	'''''''''''''''''''''''''''''''''''''''''''''"""
	def printList(self):
		print()
		print('---------- Monsters ----------')
		for x in self.monsterList:
			print(x.getType())
		print('--------------------------')
		print()


	"""'''''''''''''''''''''''''''''''''''''''''''''
	A method to get the Home's monster list
	'''''''''''''''''''''''''''''''''''''''''''''"""
	def getList(self):
		return self.monsterList


	"""'''''''''''''''''''''''''''''''''''''''''''''
	A method to set the Home's monster list
	'''''''''''''''''''''''''''''''''''''''''''''"""
	def setList(self, newList):
		self.monsterList = newList


