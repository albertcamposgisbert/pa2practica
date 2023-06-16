
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
		
        if not self.te_tret(tret):
            self.set_root(self.get_root*-1)
        distribucio_inorder(self.right, tret)
        distribucio_inorder(self.left, tret)
		
        return self.inorder
        
    def __inicialitza_individus(self, id_individu, cromosomes):
        # Instancia un individuo de la clase individuo, y lo añade a "conjunt_individus"
        self.__individus.append(individu(id_individu, cromosomes))
    
    def afegir_tret(self, tret, individu_id):
        # Asociar "tret" a un individuo concreto de la lista indexando en ella
        self.get_individu(individu_id).afegir_tret(tret) # Utiliza "afegir_tret" de la clase individu
        
    def treure_tret(self, tret, individu_id):
        # Quitar "tret" a un individuo concreto de la lista indexando en ella
        self.get_individu(individu_id).treure_tret(tret)
        
    def consulta_individu(self, individu_id):
        # Devuelve el individuo indexando en la lista por el id passado como argumento
        individu_in = False
        for individu in self.__individus:
            if individu.get_id_by_individu() == individu_id:
                individu_in = True
                cromosomas=individu.get_parell_cromosomes().get_cromosomas()
                return cromosomas
                
        if individu_in == False:
            print("error")
    
    def get_numero_cromosomes(self):
        # Devuelve el total de cromosomas
        return self.__numero_cromosomes

            
            

    
    
    
    
    
    
        
    
