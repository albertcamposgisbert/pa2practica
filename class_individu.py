"""
L'estat (privat!) de les instàncies d'aquesta classe consistirà en una
instància de Parell de Cromosomes i un conjunt d'identificadors de tret, aquells que
l'individu posseeix. Aquí, l'expressió conjunt es refereix a l'estructura de dades set, que
Python ens proporciona. Quines operacions us fan falta (els mètodes públics) és
quelcom que heu de decidir vosaltres.

"""

from class_parell_cromosomes import *

class individu():
    
    def __init__(self, individu_id, parell_cromosomes) -> None:
        self.__individu_id = individu_id
        self.__parell_cromosomes = parell_cromosomes(parell_cromosomes)
        self.__trets = set()
    
    def __str__(self) -> str:
        
        pass

        
        