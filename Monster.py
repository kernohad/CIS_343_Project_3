#!/usr/bin/env python3

# https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
from abc import ABCMeta, abstractmethod
from random import randint

"""'''''''''''''''''''''''''''''''''''''''''''''
	An abstract class to maintain Monster data
'''''''''''''''''''''''''''''''''''''''''''''"""
class Monster(object):

	__metaclass__ = ABCMeta

	health = 0
	attack = 0
	monsterType = ''

	def getType(self):
		return self.monsterType

	def getAttack(self):
		return self.attack

	def setAttack(self, newAttack):
		self.attack = newAttack

	def getHealth(self):
		return self.health

	def setHealth(self, newHealth):
		self.health = newHealth
		

"""'''''''''''''''''''''''''''''''''''''''''''''
	A class to maintain Person data
'''''''''''''''''''''''''''''''''''''''''''''"""
class Person(Monster):
	def __init__(self):
		self.health = 100
		self.attack = -1
		self.monsterType = 'Person'
	
"""'''''''''''''''''''''''''''''''''''''''''''''
	A class to maintain Zombie data
'''''''''''''''''''''''''''''''''''''''''''''"""
class Zombie(Monster):
	def __init__(self):
		self.health = randint(50, 100)
		self.attack = randint(0, 10)
		self.monsterType = 'Zombie'
	

"""'''''''''''''''''''''''''''''''''''''''''''''
	A class to maintain Vampire data
'''''''''''''''''''''''''''''''''''''''''''''"""
class Vampire(Monster):
	def __init__(self):
		self.health = randint(100, 200)
		self.attack = randint(10, 20)
		self.monsterType = 'Vampire'

"""'''''''''''''''''''''''''''''''''''''''''''''
	A class to maintain Ghoul data
'''''''''''''''''''''''''''''''''''''''''''''"""
class Ghoul(Monster):
	def __init__(self):
		self.health = randint(40, 80)
		self.attack = randint(15, 30)
		self.monsterType = 'Ghoul'

"""'''''''''''''''''''''''''''''''''''''''''''''
	A class to maintain Werewolf data
'''''''''''''''''''''''''''''''''''''''''''''"""
class Werewolf(Monster):
	def __init__(self):
		self.health = 200
		self.attack = randint(0, 40)
		self.monsterType = 'Werewolf'




