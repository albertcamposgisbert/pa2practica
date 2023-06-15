
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
    
    def __init__(self, marca = 0):
        
        self.__numero_individus = read(int) # Nombre d'individus
        self.__numero_cromosomes = read(int) # Nombre de gens de cada cromosoma
        self.__individus = []
        self.arbre = self.llegeix_bintree_int(marca)
        
        for i in range(1, self.__numero_individus):
            self.__inicialitza_individus(i, read(str))
        
    def llegeix_bintree_int(self,marca):
        x = read(int)
        if x != marca:
            l = self.llegeix_bintree_int(marca)
            r = self.llegeix_bintree_int(marca)
            
            return BinTree(x,l,r)
        else:
            return BinTree()
        
    def distribucio_inorder(self, tret):
        pass
        
    def __inicialitza_individus(self, id_individu, cromosomes):
        # Instancia un individuo de la clase individuo, y lo añade a "conjunt_individus"
        self.__individus.append(individu(id_individu, cromosomes))
    
    def afegir_tret(self, id_individu, tret):
        # Asociar "tret" a un individuo concreto de la lista indexando en ella
        tret = read(str)
        individu_id = read(int)
        self.get_individu(individu_id).afegir_tret(tret) # Utiliza "afegir_tret" de la clase individu
        
    def treure_tret(self):
        # Quitar "tret" a un individuo concreto de la lista indexando en ella
        tret = read(str)
        individu_id = read(int)
        self.get_individu(individu_id).treure_tret(tret)
        
    def consulta_individu(self):
        # Devuelve el individuo indexando en la lista por el id passado como argumento
        individu_in = False
        for individu in self.__individus:
            individu_id = read(int)
            if individu.get_id_by_individu == individu_id:
                individu_in = True
                print(f"consulta individu {individu.individu_id}")
                print(individu)
                
        if individu_in == False:
            print("error")
    
    def get_numero_cromosomes(self):
        # Devuelve el total de cromosomas
        return self.__numero_cromosomes

            
            

    
    
    
    
    
    
        
    