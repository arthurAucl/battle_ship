from Position import Position
import random

#class pour definir ce qu'est un bateau
class Boat(object):
    count = 0
    #dictionnaire pour les bateaux
    boat_types = {
        1: {'name':'Sous-marin', 'color':'red'}, 
        2: {'name':'Torpilleur','color':'green'},
        3: {'name':'Escorteur', 'color':'orange'},
        4: {'name':'Croiseur', 'color':'blue'},
        5: {'name':'Porte-Avion','color':'pink'},
    }
    #création de certaine variable +  definir si le bateau est vertical ou non
    def __init__(self, size):
        random.seed()
        self._positions = []
        self._touch_positions = []

        self.size = size
        self.is_vertical = random.choice([True,False])
        self.name = Boat.boat_types[size]['name']
        self.color = Boat.boat_types[size]['color']
    
    # Définir que le bateau à une position pas rapport à sa taille 
    def set_position(self, start_position):
        for index in range(self.size):
            if self.is_vertical:
                current_position = Position(start_position.x + index, start_position.y)
            else:
                current_position = Position(start_position.x, start_position.y + index)

            self._positions.append(current_position)

    #Méthode pour evaluer si le bateau est touché
    def touch_evaluate(self, position):
        if position in self._positions:
            if not position in self._touch_positions:
                self._touch_positions.append(position)
            return True
        else:
            return False

    #Méthode pour evaluer si le bateau est coulé
    def has_sink(self):
        if len(self._touch_positions) == len(self._positions):
            return True
        return False

# Boat
# Boat
