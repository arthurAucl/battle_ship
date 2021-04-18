from Position import Position
from tkinter import *
from tkinter.messagebox import *
import pygame
import time 
from math import *
from Game import Game
from Boat import Boat
import random

#class pour placer un bouto
class Cell(Button):
    def config(self, row, column):
        self.row = row
        self.column = column

#class pour créer l'interface 
class GameView(object):
 
    def __init__(self, game):
        self._game = game
        self._top = Tk()
        self._top.grid()
        self._grid = []
        self._configure_menu()
        self._configure_frames()
        #self.configure_easy_level()
        self.configure_medium_level()
        #self.configure_hard_level()
        #self.configure_impossible_level()
        #self.bouton_level()
        #self.resultForCell()


    def _configure_menu(self):
        # Configuration main window
        self._top.title("Bataille Navale")
        self._top.maxsize(1080,720)
        self._top.minsize(1080,720)

        #creation de la barre de menu
        self._menubar = Menu(self._top)

        self._game_menu = Menu(self._menubar, tearoff=0)
        self._parametre = Menu(self._menubar, tearoff=0)
        self._aide = Menu(self._menubar, tearoff=0)

        self._game_menu.add_command(label="Nouvelle Partie", command=self._restart)
        self._game_menu.add_command(label="Quitter", command=self._top.quit)
        self._menubar.add_cascade(label="Jeu", menu=self._game_menu)
        
        self._aide.add_command(label="Les règles du jeu", command=self._regles)
        self._menubar.add_cascade(label="Aide", menu=self._aide)
        
        self._top.config(menu=self._menubar)
        

    def _configure_frames(self):
        #Création de colonnes et ligne qui prenne toute la fenetre 
        for r in range(ceil(self._game.boat_grid.shape[0]+(self._game.boat_grid.shape[0]/2))):
            self._top.rowconfigure(r, weight=1)    
        for c in range(ceil(self._game.boat_grid.shape[1]+(self._game.boat_grid.shape[1]/2))):
            self._top.columnconfigure(c, weight=1)

        #Création des frames diviser la fenetre en trois parties
        Frame_score = Frame(self._top, bg="red")
        Frame_score.grid(row = 0, column = 0, rowspan = ceil(self._game.boat_grid.shape[0]/2), columnspan = self._game.boat_grid.shape[1], sticky = W+E+N+S) 
        Frame_game = Frame(self._top, bg="blue")
        Frame_game.grid(row = ceil(self._game.boat_grid.shape[0]/2), column = 0, rowspan = self._game.boat_grid.shape[0], columnspan = self._game.boat_grid.shape[1], sticky = W+E+N+S)
        Frame_level = Frame(self._top, bg="blue")
        Frame_level.grid(row = 0, column = self._game.boat_grid.shape[1], rowspan = ceil(self._game.boat_grid.shape[0]+(self._game.boat_grid.shape[0]/2)), columnspan = ceil(self._game.boat_grid.shape[1]+(self._game.boat_grid.shape[1]/2)), sticky = W+E+N+S)

        #Création d'un label qui affiche le score
        self._scoreLabel_text = StringVar()
        self._scoreLabel_text.set(f"Votre score est {self._game.score}")
        self._scoreLabel = Label(master=Frame_score, textvariable=self._scoreLabel_text, height=6)
        self._scoreLabel.place(x = 325, y = 50, width=150, height=25)

        #Placement des boutons de la matrice "boat_grid"
        for row_index in range(self._game.boat_grid.shape[0]):
            Frame_game.rowconfigure(row_index, weight=1)  
            for col_index in range(self._game.boat_grid.shape[1]):
                Frame_game.columnconfigure(col_index, weight=1)
                button = Cell(Frame_game, borderwidth=0, relief=FLAT, height = 1, width = 1)
                button.config(row = row_index, column = col_index)
                button.grid(row = row_index, column = col_index, sticky = W+E+N+S)
                button.bind("<Button-1>", self.selectedCell)
                self._grid.append(button)

    #Bouton de niveau (non fonctionable mais nous n'avons pas compris pourquoi)
    #def bouton_level(self):
        #bouton_easy = Button(Frame3, text="Facile", command=configure_easy_level)
        #bouton_easy.pack(side=TOP)
        #bouton_medium = Button(Frame3, text="Normal", command=configure_medium_level)
        #bouton_medium.pack()
        #bouton_hard = Button(Frame3, text="Difficile", command=configure_hard_level)
        #bouton_hard.pack()
        #bouton_impossible = Button(Frame3, text= "Impossible", command=configure_impossible_level)
        #bouton_impossible.pack()

    #Méthode recommencer (non fonctionnel)
    def _restart(self):
        showinfo("Recommencer", "Recommencer")
    
    #Méthode pour definir les règles du jeu 
    def _regles(self):
        showinfo("Les régles sont:", "Les règles de la bataille navale sont simples. L’objectif est de couler tous les bateaux en ayant le minimum de points de score. Les sous-marins qui ne prennent qu’une seule case sont en rouge. Les torpilleurs qui prennent deux cases sont en vert. Les escorteurs qui prennent trois cases sont en orange. Les croiseurs qui prennent quatres cases sont en bleu. Et les porte-avions qui prennent cinq cases sont en rose. Les bateaux ne peuvent pas etre à coté. Maintenant à vous de jouer.!")
    
    #Méthode exprimer la selection du bouton choisi dans la matrice "boat_grid" 
    def selectedCell(self, event):
        cell = event.widget
        cell.bind("<Button-1>", None)
        position = Position(cell.row, cell.column)    
        self.resultForCell(cell = cell, boat = self._game.play(position))
        
    #Méthode pour afficher la fenetre  
    def display_grid(self):
        self._top.mainloop()

    #Méthode pour definir ce qu'est le level facile
    #def configure_easy_level(self):
        #cell_quantity = ceil((20 * 20) / 2)

        #sampling = random.choices(self._grid, k=cell_quantity)
       # for cell in sampling:
        #   position = Position(cell.row, cell.column)    
        #    self.resultForCell(cell = cell, boat = self._game.play(position)) 
        #pass
        
    #Méthode pour definir ce qu'est le level moyen
    def configure_medium_level(self):
        cell_quantity = ceil((20 * 20) / 4)

        sampling = random.choices(self._grid, k=cell_quantity)
        for cell in sampling:
            position = Position(cell.row, cell.column)    
            self.resultForCell(cell = cell, boat = self._game.play(position))
        pass
    
    #Méthode pour definir ce qu'est le level difficile
    #def configure_hard_level(self):
        #cell_quantity = ceil((20 * 20) / 8)

        #sampling = random.choices(self._grid, k=cell_quantity)
        #for cell in sampling:
            #position = Position(cell.row, cell.column)    
            #self.resultForCell(cell = cell, boat = self._game.play(position)) 
        #pass
    
    #Méthode pour definir ce qu'est le level impossible 
    #def configure_impossible_level(self):
        #pass

    #Méthode pour afficher un message lorsque un bateau est coulé et pour la fin du jeu
    def resultForCell(self, cell, boat):
        self._scoreLabel_text.set(f"Votre score est {self._game.score}")
        if boat :
            cell.configure(fg=boat.color, text="X")
            if boat.has_sink():
                if (self._game.is_finished()==FALSE):
                    print ("coule")
                    showinfo("Coulé",f"Un {boat.name} a été coulé")
            if self._game.is_finished():
                print ("Finished")
                showinfo("Game Over",f"Toute la flotte a été coulée")
                retry = askretrycancel("Recommencer", "Une nouvelle chance ?")
                if retry:
                    self._restart()
                else:
                    self._top.quit()
        else :
            cell.configure(fg='blue', text="O", bg="blue")
        
        
