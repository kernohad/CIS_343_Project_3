import Player
import Neighborhood
from Observer import Observer

class Game(Observer):

	def __init__(self):
		self.player = Player.Player()
		self.neighborhood = Neighborhood.Neighborhood(self)
		self.currentCol = 0
		self.currentRow = 0
		self.currentHome = self.neighborhood.getGrid()[self.currentRow][self.currentCol]
		self.totalMonsters = 0

		# Loop through every Monster in every Home and count all non Person Monsters
		for x in range(len(self.neighborhood.getGrid())):
			for y in range(len(self.neighborhood.getGrid()[x])):
				for z in range(len(self.neighborhood.getGrid()[x][y].getList())):
					if self.neighborhood.getGrid()[x][y].getList()[z].getType() != 'Person':
						self.totalMonsters += 1

		
	def isGameOver(self):
		if self.player.getHealth() <= 0:
			# Player Loses
			return True
		elif self.totalMonsters <= 0:
			# Player Wins
			return True
		else:
			return False

	def movePlayer(self, direction):
		if direction == 'north' or direction == 'North':
			if self.currentRow > 0:
				self.currentRow -= 1
			else:
				print('Player cannot move North.')

		elif direction == 'south' or direction == 'South':
			if self.currentRow < len(self.neighborhood.getGrid()):
				self.currentRow += 1
			else:
				print('Player cannot move South.')

		elif direction == 'west' or direction == 'West':
			if self.currentCol > 0:
				self.currentCol -= 1
			else:
				print('Player cannot move West.')

		elif direction == 'east' or direction == 'East':
			if self.currentCol < len(self.neighborhood.getGrid()[self.currentRow]):
				self.currentCol += 1
			else:
				print('Player cannot move East.')

		self.currentHome = self.neighborhood.getGrid()[self.currentRow][self.currentCol]

	def getPlayer(self):
		return self.player

	def getNeighborhood(self):
		return self.neighborhood

	def getCurrentHome(self):
		return self.currentHome

	def getCurrentCol(self):
		return self.currentCol

	def getCurrentRow(self):
		return self.currentRow

	def getTotalMonsters(self):
		return self.totalMonsters

	def setTotalMonsters(self, newTotal):
		self.totalMonsters = newTotal

	def update(self):
		self.totalMonsters -= 1


