
from easyinput import read
from bintree import *
from class_individu import *

class conjunt_individus:
    
    def __init__(self) -> None:
        
        self.__numero_individus = read(int)
        self.__numero_cromosomes = read(int)
        self.__individus = []
        self.arbre = self.__llegeix_bintree_int(self, 0)
        
        self.__crea_arbre()
        self.__assigna_cromosomes()
        
        
    def crea_arbre(self, __numero_individus):
        # Crea el arbol
        pass
        
    
    def llegeix_bintree_int(self, marca):
        x = read(int)
        if x != marca:
            l = self.llegeix_bintree_int(marca)
            r = self.llegeix_bintree_int(marca)
            return BinTree(x,l,r)
        else:
            return BinTree()
        
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
        
    
    def __assigna_cromosomes(self):
        
        pass
    
    
    
    
    
    
        
    