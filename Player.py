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


	def printInventory(self):
		print()
		print('------------------------- Inventory -------------------------')
		print(' Key \t Name \t\t Attack Modifier \t Times Used')
		print()
		for x in self.inventory:
			print(' ', self.inventory.index(x), '\t', x.getName(), '\t', x.getAttackModifier(), '\t\t\t', x.getTimesUsed(), '/', x.getMaxUse())
		print('--------------------------------------------------------------')
		print()

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

