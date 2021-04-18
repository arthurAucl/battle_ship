from GameView import GameView
from Game import Game

#Constante
boat_type_list=[5,4,4,3,3,3,2,2,2,2,1,1,1,1,1]
grid_size = 20

#Set up
game = Game(grid_size)
game.set_up(boat_type_list)
display = GameView(game)

#Game
display.display_grid()
