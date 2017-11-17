
import Home


"""'''''''''''''''''''''''''''''''''''''''''''''
	A class to maintain Neighborhood data
'''''''''''''''''''''''''''''''''''''''''''''"""
class Neighborhood(object):

	GRID_SIZE = 4
	

	def __init__(self):
		self.grid = []
		for row in range(self.GRID_SIZE):
			self.grid.append(list())
			for col in range(self.GRID_SIZE):
				tmp = Home.Home()
				self.grid[row].append(tmp)
 

