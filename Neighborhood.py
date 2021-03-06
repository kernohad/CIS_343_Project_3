
import Home


"""'''''''''''''''''''''''''''''''''''''''''''''
	A class to maintain Neighborhood data
'''''''''''''''''''''''''''''''''''''''''''''"""
class Neighborhood(object):

	GRID_SIZE = 4
	

	def __init__(self, game):
		self.grid = []
		for row in range(self.GRID_SIZE):
			self.grid.append(list())
			for col in range(self.GRID_SIZE):
				tmp = Home.Home(game)
				self.grid[row].append(tmp)

	def getGrid(self):
		return self.grid

	def getGridSize(self):
		return self.GRID_SIZE
 

