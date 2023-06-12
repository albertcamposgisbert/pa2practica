
from class_conjunt_individus import *
from class_conjunt_trets import *


class experiment:

    def __init__(self, nombre_individus, nombre_gens):
        self.__nombre_individus = nombre_individus  #Nombre d'individus
        self.__nombre_gens = nombre_gens  #Nombre de gens de cada cromosoma
        
        conjunt_individus = conjunt_individus()
        conjunt_trets = conjunt_trets()

