from Position import Position
from Boat import Boat

import numpy as np
import random

class Game(object):

    def __init__(self, grid_size):
        self.boat_grid  = np.zeros((grid_size, grid_size), dtype=int) 
        #On initialise une matrice plus grande pour gérer les effets de bords (rempli de 1 pour la grille des positions possible
        self._position_grid  = np.full((grid_size+2, grid_size+2), 1, dtype=int)
        #Les lignes et colunms des extrémités à 0 [TODO]

    #Placement d'un bateau
    def _get_next_random_position(self, current_boat):
        #explorer la matrice pour donner la nouvelle position possible qui dépend de l'orientation du bateau 
        random_column = -1
        random_row = -1
        potential_boat = []
        trycount=0

        #on somme les elements du vecteur (à 1) et on compare à la taille du bateau
        while np.sum(potential_boat)<current_boat.size:
            #On sort si on ne trouve pas au bout de N essais
            if trycount > 100:
                print('Erreur : Ne peut pas résoudre le problème')
                return Position(-1,-1)
            trycount=trycount+1

            if current_boat.is_vertical == True :
                random_column = random.randint(1,self.boat_grid.shape[1]-1)
                random_row = random.randint(1,self.boat_grid.shape[0]-current_boat.size)
                potential_boat = self._position_grid[random_row:random_row+current_boat.size, random_column:random_column+1]
            
            else :
                random_row = random.randint(1,self.boat_grid.shape[0]-1)
                random_column = random.randint(1,self.boat_grid.shape[1]-current_boat.size)
                potential_boat = self._position_grid[random_row:random_row+1, random_column:random_column+current_boat.size]
        
        if current_boat.is_vertical == True :
            self._position_grid[random_row-1:random_row+current_boat.size+1, random_column-1:random_column+2] = 0
            self.boat_grid[random_row:random_row+current_boat.size, random_column:random_column+1] = 1
        else:
            self._position_grid[random_row-1:random_row+2, random_column-1:random_column+current_boat.size+1] = 0
            self.boat_grid[random_row:random_row+1, random_column:random_column+current_boat.size] = 1
        return Position(random_row,random_column)

    #Création de certaine variable + placement de tous les bateaux par rapport à leurs taille
    def set_up(self, boattype_list):
        random.seed()
        self.score = 0
        self.boat_list= []
        for boatsize in sorted(boattype_list,reverse=True):
            current_boat = Boat(size=boatsize)
            current_boat.set_position(self._get_next_random_position(current_boat))
            self.boat_list.append(current_boat)
    
    #Méthode pour evaluer si le bateau est touché
    def play(self, position):
        for boat in self.boat_list:
            if boat.touch_evaluate(position) :
                self.score += 1
                return boat   
        
        self.score += 10  
        return None

    #Méthode pour evaluer quand es ce que la parti est fini
    def is_finished(self):
        finished = True
        for boat in self.boat_list:
            finished = finished and boat.has_sink()
        return finished
