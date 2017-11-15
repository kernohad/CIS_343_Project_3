import Home

class Neighborhood(object):

	GRID_SIZE = 4
	# grid = [[Home.Home()]*GRID_SIZE]*GRID_SIZE
	grid = [[Home.Home(), Home.Home(), Home.Home(), Home.Home()],
			[Home.Home(), Home.Home(), Home.Home(), Home.Home()]]

	# def __init__(self):
	# 	for row in self.grid:
	# 		for col in row:
	# 			tmp = Home.Home()
	# 			print(tmp.monsterList[0].getType())
	# 			col = tmp


