import Player
import Neighborhood

class Game(object):

	def __init__(self):
		self.player = Player.Player()
		self.neighborhood = Neighborhood.Neighborhood()
		self.currentCol = 0
		self.currentRow = 0
		self.currentHome = self.neighborhood.getGrid()[self.currentRow][self.currentCol]

	def isGameOver(self):
		if self.player.getHealth() <= 0:
			# Player wins
			return True
		# elif all monsters are turned to people
			# Player loses
			#return True
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

		
