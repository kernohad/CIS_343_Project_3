#!/usr/bin/env python3

import Monster
from random import randint

class Home(object):

	monsterList = []

	def __init__(self):
		for x in range(10):
			tmp = randint(1, 4)
			if tmp == 1:
				self.monsterList.append(Monster.Zombie())
			elif tmp == 2:
				self.monsterList.append(Monster.Vampire())
			elif tmp == 3:
				self.monsterList.append(Monster.Ghoul())
			elif tmp == 4:
				self.monsterList.append(Monster.Werewolf())

	def getList(self):
		print()
		print('-------- HOME -------------')
		for x in self.monsterList:
			print(x.getType())
		print('---------------------------')
		print()


a = Home()
a.getList()
b = Home()
b.getList()
c = Home()
c.getList()