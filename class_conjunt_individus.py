
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
    
    def __init__(self, numero_individus, numero_cromosomas, marca = 0):
        
        self.__numero_individus = numero_individus
        self.__numero_cromosomes = numero_cromosomas
        self.__individus = []
        self.__arbre = self.llegeix_bintree_int(marca)
        
        for i in range(1, self.__numero_individus+1):
            self.__inicialitza_individus(i, read(str))
        
    def llegeix_bintree_int(self,marca):
        x = read(int)
        if x != marca:
            l = self.llegeix_bintree_int(marca)
            r = self.llegeix_bintree_int(marca)
            
            return BinTree(x,l,r)
        else:
            return BinTree()

    def get_arbre(self):
        return self.__arbre

    def distribucio_inorder(self, arbre, tret):
        if not arbre.get_root()!=None:
            pass
        else:
            if not arbre.get_root().te_tret(tret):
                arbre.set_root(arbre.get_root*-1)
            che=BinTree(arbre.get_root, arbre.get_left.distribucio_inorder(tret), arbre.get_right.distribucio_inorder(tret))
            
        return che.inorder()
        
    def __inicialitza_individus(self, id_individu, cromosomes):
        # Instancia un individuo de la clase individuo, y lo añade a "conjunt_individus"
        self.__individus.append(individu(id_individu, cromosomes))

    
    def afegir_tret(self, tret, individu_id):
        # Asociar "tret" a un individuo concreto de la lista indexando en ella
        self.get_individu_by_id(individu_id).afegir_tret(tret) # Utiliza "afegir_tret" de la clase individu
        
    def treure_tret(self, tret, individu_id):
        # Quitar "tret" a un individuo concreto de la lista indexando en ella
        self.get_individu_by_id(individu_id).treure_tret(tret)
        
    def get_individu_by_id(self, individu_id):
        # Devuelve el individuo indexando en la lista por el id passado como argumento
        for individu in self.__individus:
            if individu.get_id_by_individu() == individu_id:
               # cromosomas=individu.get_parell_cromosomes().get_cromosomas()
                return individu
    def get_numero_cromosomes(self):
        # Devuelve el total de cromosomas
        return self.__numero_cromosomes

 
    def get_num_individuos(self):
            return self.__numero_individus    
    def consulta_individu(self, individu_id):
        individu = self.get_individu_by_id(individu_id)
        if individu:
            print(individu)
        else:
            print('error')
        

            
            

    
    
    
    
    
    
        
    
