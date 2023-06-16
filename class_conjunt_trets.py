
"""
Conjunt de Trets: L'estat (privat!) de les instàncies d'aquesta classe (en realitat
només en caldrà una per experiment) consistirà en un diccionari de parelles
(nom_tret, info_tret), on nom_tret és una string i info_tret pot ser una tupla
de dos elements, una instància de Parell de Cromosomes i un conjunt d'instàncies
d'Individu (aquells que tenen el tret). Aquí, l'expressió conjunt es refereix a
l'estructura de dades set, que Python ens proporciona
. Quines operacions us fan falta (els mètodes públics) és quelcom que heu de decidir vosaltres.
"""
from class_conjunt_individus import *
from class_parell_cromosomes import *
from collections import namedtuple

Element = namedtuple("Element", ["interseccio", "individus"])


class conjunt_trets:
    
    def __init__(self,conj):
        self.__conjunt_individus=conj
        self.__trets={}
    def distribucio_trets(self, tret):
        arb_aux=BinTree(self.get_root(), self.get_left(), self.get_right())
            
        if arb_aux.get_left().te_tret(tret)==0 and arb_aux.get_left().leaf():
            arb_aux.poda_subarbre(arb_aux.get_left)
        if arb_aux.get_right().te_tret(tret)==0 and arb_aux.get_right().leaf:
            arb_aux.poda_subarbre(arb_aux.right)
        arb_aux.get_left.distribucio_trets(tret)
        arb_aux.get_rightdistribucio_trets(tret)
        result = arb_aux.distribucio_inorder(tret)
        return result 
    def afegir_tret(self,nom_tret,numero_individu):
        """
        Assigna informació a una clau. Si la clau ja hi és dins
        el diccionari, la informació és modificada.
        cas pitjor: Theta(n). cas mitjà: Theta(1+n/M).
        """
        if nom_tret in self.__trets: #Això vol dir que el tret ja el teniem
            elem=self.__trets[nom_tret]
            a=elem.individus
            for i in a:
                if i.get_id_by_individu==numero_individu:
                    return 'error'
            self.__conjunt_individus.afegir_tret(nom_tret,numero_individu)
            interseccio_original=elem.interseccio


            cromosomes_nou_element=self.__conjunt_individus.get_individu_by_id(numero_individu).get_parell_cromosomes()

            nova_interseccio=interseccio_original.interseccio(cromosomes_nou_element)

            elem.individus.append(self.__conjunt_individus.get_individu_by_id(numero_individu))

            elem._replace(interseccio=nova_interseccio)
            self.__trets[nom_tret]=elem
        else:

            self.__conjunt_individus.afegir_tret(nom_tret,numero_individu)
            cromosomas=self.__conjunt_individus.get_individu_by_id(numero_individu).get_parell_cromosomes()
            self.__trets[nom_tret]=Element(cromosomas,[self.__conjunt_individus.get_individu_by_id(numero_individu)])
          
    def treure_tret(self, tret, numero_individu):
        """
        Elimina la parella (clau, valor) del diccionari. Si la clau no pertany al
        diccionari, res canvia.
        cas pitjor: Theta(n). cas mitjà: Theta(1+n/M).
        """
        tetret=False
        i=0
        element=self.__trets[tret]
        individuos= element.individus
        if tret in self.__trets:
            while i < len(individuos):
                if individuos[i].get_id_by_individu() == numero_individu:
                    tetret=True
                    individuos.pop(i)
                    break
                i+=1

            if len(individuos)==0 : 
                self.__conjunt_individus.treure_tret(tret,numero_individu)
                del self.__trets[tret]
                tetret=False
            
            elif tetret:
                ind=individuos[0].get_parell_cromosomes()
                element._replace(interseccio=ind.get_cromosomas())
                self.__conjunt_individus.treure_tret(tret,numero_individu)

                for i in individuos:
                    cromosomas=i.get_parell_cromosomes()
                    intersection= parell_cromosomes.interseccio(element.interseccio,cromosomas)
                    element._replace(interseccio=intersection) 
                self.__trets[tret]=element   
        else:
            return 'error'

                
    def consulta_tret(self, tret):
        """
        retorna el valor associat a una clau, None si la clau no hi és
        cas pitjor: Theta(n). cas mitjà: Theta(1+n/M).
        """
        if tret in self.__trets:
            element=self.__trets[tret]
            interseccio=element.interseccio
            individus=element.individus
            return (interseccio.get_cromosomas(),individus)
        else:
            return None
