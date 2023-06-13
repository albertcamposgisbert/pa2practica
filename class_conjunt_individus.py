
from easyinput import read
from bintree import *
from class_individu import *

"""
Conjunt d'Individus: L'estat (privat!) de les instàncies d'aquesta classe (en
realitat només en caldrà una per experiment) consistirà en l'arbre binari que defineix la
relació entre individus i una col·lecció amb les instàncies d'Individu que hagin
aparegut. Quines operacions us fan falta (els mètodes públics) és quelcom que heu de
decidir vosaltres.

"""

class conjunt_individus:
    
    def __init__(self) -> None:
        
        self.__numero_individus = read(int) # Nombre d'individus
        self.__numero_cromosomes = read(int) # Nombre de gens de cada cromosoma
        self.__individus = ()
        self.__arbre = self.__llegeix_bintree_int(self, 0)
        self.__crea_arbre()
        self.__assigna_cromosomes()
        
    def llegeix_bintree_int(self,marca):
        x = read(int)
        if x != marca:
            l = self.llegeix_bintree_int(marca)
            r = self.llegeix_bintree_int(marca)
            return BinTree(x,l,r)
        else:
            return BinTree()
        
    
    def __inicialitza_individus(self, __numero_individus):
        def __assigna_cromosomes(self):
            pass
        for i in range(__numero_individus+1):
            
            pass
        
    def __crea_arbre(self):
        #Crea arbol para distribución trets
        pass
    
    def afegir_individu(self, cromosomes):
        # añadir individuo a la lista de conjunto de individuos, creando una instancia de la clase Individu
        pass
    
    def afegir_tret(self, individu, tret):
        # Asociar "tret" a un individuo concreto de la lista indexando en ella
        pass
        
    def get_individu(self, numero_individu):
        # Devuelve el individuo indexando en la lista por el id passado como argumento
        
        return self.__individus[numero_individu]
    
    def get_numero_cromosomes(self):
        # Devuelve el total de cromosomas
        
        return self.__numero_cromosomes

    
    
    
    
    
    
        
    