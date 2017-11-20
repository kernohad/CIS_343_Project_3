import Game

if __name__ == "__main__":

	game = Game.Game()

  for x in range(len(game.getNeighborhood().getGrid())):
      for y in range(len(game.getNeighborhood().getGrid()[x])):
        super().__init__()
        game.getNeighborhood().getGrid()[x][y].add_observer(game)
 

	while game.isGameOver() == False:

		command = input('\n>').split()

		# Check if anything is entered
		if len(command) > 0:



				# Help command
				if command[0] == 'help' or command[0] == 'Help':
					print("This is help")

				# Move command
				elif command[0] == 'move' or command[0] == 'Move':

					# Check to many arguments
					if len(command) < 3:

						#Check to few arguments
						if len(command) > 1:

							# Reads second argument for direction
							if command[1] == 'north' or command[1] == 'North' or command[1] == 'south' or command[1] == 'South' or command[1] == 'east' or command[1] == 'East' or command[1] == 'west' or command[1] == 'West':
								game.movePlayer(command[1])

							# Catch everything not valid above
							else:
								print('ERROR: That is not a valid direction.')

						else:
							print('ERROR: You need to enter a direction with the "move" command.')

					else:
						print('ERROR: To many arguments. "Move" has only 2 arguments.')

					# Gets current home row and col
					row = str(game.getCurrentRow())
					col = str(game.getCurrentCol())
					# Display what current home is
					print('You are at Home:(' + row + ',' + col + ')')

				elif command[0] == 'inventory' or command[0] == 'Inventory':
					inventory = game.getPlayer().getInventory()

					print()
					print('------------------------- Inventory -------------------------')
					print(' Key \t Name \t\t Attack Modifier \t Times Used')
					print()
					for x in inventory:
						print(' ', inventory.index(x), '\t', x.getName(), '\t', x.getAttackModifier(), '\t\t\t', x.getTimesUsed(), '/', x.getMaxUse())
					print('--------------------------------------------------------------')
					print()

				# View command. Prints the current home's monster list.
				elif command[0] == 'view' or command[0] == 'View':
					row = str(game.getCurrentRow())
					col = str(game.getCurrentCol())

					print()
					print('---------- Monsters in Home:(' + row +  ','+ col + ') ----------')
					print(' Monster \t\t Health')
					print()
					for x in game.getCurrentHome().monsterList:
						print(' ', x.getType(), '\t\t', x.getHealth())
					print('--------------------------------------------')
					print()

				# Attack command. The player attacks every monster in the current home
				elif command[0] == 'attack' or command[0] == 'Attack':

					# Check to many arguments
					if len(command) < 3:
						# Check to few arguments
						if len(command) > 1:

							monsters = game.getCurrentHome().getList()
							player = game.getPlayer()

							# Convert second argument to an int
							num = int(command[1])
							# Check if second argument is a valid key
							if num < len(player.getInventory()):

								attackModifier = player.getInventory()[num].getAttackModifier()

								# Loop through every monster in home
								for x in range(len(monsters)):
									if not player.isPlayerDead() and monsters[x].getType() != 'Person':
										# Player attacks monster
										monsters[x].setHealth(monsters[x].getHealth() - (player.getAttack() * attackModifier))
                    
                    # if monster died and turned to human, call Home update
                    if monsters[x].getHealth() <= 0:
                      game.getCurrentHome().update()

                      
									if not monsters[x].isMonsterDead():
										# Monster Attacks player
										player.setHealth(player.getHealth() - monsters[x].getAttack())

								# Increment 'times used' for weapon		
								player.getInventory()[num].setTimesUsed(1)
								#Check if weapon used has maxed out, if so, remove it from list
								if not player.getInventory()[num].hasUsesLeft():
									del player.getInventory()[num]
									print('You broke the weapon you just used.')


							else:
								print('ERROR: You do not have a weapon in your inventory with that key.')

						else:
							print('ERROR: You need to enter the key of the weapon you want to attack with. Use "inventory" to see what weapons you have and their key')
					else:
						print('ERROR: To many arguments. "Atack" has only 2 arguments.')




				# Quit command
				elif command[0] == 'quit' or command[0] == 'Quit':
					exit()

				# Catch everything not listed above. Not valid command
				else:
					print('ERROR: That is not a command. Enter "help" for a list of commands.')
			

		else:
			print('ERROR: Please enter a command. Enter "help" for a list of commands.')
