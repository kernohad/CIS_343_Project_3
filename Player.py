import Weapon
from random import randint


class Player(object):

	health = 0
	attack = 0
	inventory = []

	def __init__(self):
		self.health = randint(100, 125)
		self.attack = randint(10, 20)

		for x in range(10):
			tmp = randint(1, 4)
			if tmp == 1:
				self.inventory.append(Weapon.HershyKisses())
			elif tmp == 2:
				self.inventory.append(Weapon.SourStraWS())
			elif tmp == 3:
				self.inventory.append(Weapon.ChocolateBars())
			elif tmp == 4:
				self.inventory.append(Weapon.NerdBombs())


	def getInventory(self):
		return self.inventory

	def setInventory(self, newInventory):
		self.inventory = newInventory

	def getHealth(self):
		return self.health

	def setHealth(self, newHealth):
		self.health = newHealth

	def getAttack(self):
		return self.attack

	def setAttack(self, newAttack):
		self.attack = newAttack

	def isPlayerDead(self):
		if self.health <= 0:
			print('You died')
			return True
		else:
			return False

