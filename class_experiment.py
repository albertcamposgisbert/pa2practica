
from easyinput import read

class experiment:

    def __init__(self, n, m):
        self.nombre_individus = read(int)  #Nombre d'individus
        self.nombre_gens = read(int)  #Nombre de gens de cada cromosoma
        #arbre
