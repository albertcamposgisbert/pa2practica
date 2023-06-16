"""
L'estat (privat!) de les instàncies d'aquesta classe consistirà en una
instància de Parell de Cromosomes i un conjunt d'identificadors de tret, aquells que
l'individu posseeix. Aquí, l'expressió conjunt es refereix a l'estructura de dades set, que
Python ens proporciona. Quines operacions us fan falta (els mètodes públics) és
quelcom que heu de decidir vosaltres.

"""

from class_parell_cromosomes import *

class individu():
    
    def __init__(self, individu_id, parell):
        self.__individu_id = individu_id
        self.__parell_cromosomes = parell_cromosomes(parell)
        self.__trets = set()
    
    def __str__(self) -> str:
        self.__ordena_trets_alfabeticament()
        elements_trets = "\n".join(str(elem) for elem in self.__trets)
        return f"{self.__parell_cromosomes}\n{elements_trets}" if elements_trets else f"{self.__parell_cromosomes}" # Printar parell de cromosomes a partir de __str__, y trets
    
    def __ordena_trets_alfabeticament(self):
        llista_ordenada = sorted(self.__trets)
        set_ordenat = set(llista_ordenada)
        return set_ordenat
    
    def get_id_by_individu(self):
        return self.__individu_id
    
    def get_parell_cromosomes(self):
        return self.__parell_cromosomes
    
    def afegir_tret(self, tret):
        self.__trets.add(tret)
        
    def treure_tret(self, tret):
        self.__trets.add(tret)
        
    def te_tret(self, tret):
        return tret in self.__trets

        
        