
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

Element = namedtuple("Element", ["nom_tret", "info_tret"])
Subelement= namedtuple("Subelement", ["interseccio", "individus"])

class conjunt_trets:
    
    def __init__(self):
        self.__M = 100
        self.__taula = self.__M * [None] 
        for i in range(self.__M):
            self.__taula[i] = []
        self.__n     = 0    # nombre d'elements emmagatzemats
    def __posicio(self, nom_tret, h):
        """
        Retorna la posició de la clau a la llista      
        d'elements de la posició h, o None si no el troba.
        """
        l = self.__taula[h]
        if len(l)>0:
            for i in range(len(l)):
                if l[i].nom_tret == nom_tret:
                    return i
            return None
        else:
                return None
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
    def elements(self):
        resultat = []
        for ll in self.__taula:
            for e in ll:
                resultat.append(e)
        return resultat

    def __rehash(self):
        elements = self.elements()
        self.__M = 2*self.__M # Modifiquem la mida de la taula.
        # Inicialitzem tot un altre cop
        self.__taula = self.__M * [None] 
        for i in range(self.__M):
            self.__taula[i] = []
        self.__n = 0

        for e in elements: #Aquí he fet canvis
            h=hash(e.nom_tret) % len(self.__taula)
            self.__taula[h].append(e)
      
    def afegir_tret(self,nom_tret,numero_individu):
        """
        Assigna informació a una clau. Si la clau ja hi és dins
        el diccionari, la informació és modificada.
        cas pitjor: Theta(n). cas mitjà: Theta(1+n/M).
        """
        h = hash(nom_tret) % len(self.__taula)    # la funció 'hash' ens la dona Python
        p = self.__posicio(nom_tret, h)
        if p != None: #Això vol dir que el tret ja el teniem
        
            elem = self.__taula[h][p]
            
            conjunt_individus.afegir_tret(nom_tret,numero_individu)

            elem2=elem.info_tret
            interseccio_original= elem2.interseccio

            cromosomes_nou_element=conjunt_individus.get_individu_by_id(numero_individu).get_parell_cromosomes()

            nova_interseccio=parell_cromosomes.interseccion(interseccio_original,cromosomes_nou_element)

            elem2.individus.append(conjunt_individus.get_individu_by_id(numero_individu))

            elem2._replace(interseccio=nova_interseccio)
            self.__taula[h][p] = elem._replace(info_tret=elem2) # Genera NOU element
        else:
            conjunt_individus.afegir_tret(nom_tret,numero_individu)

            cromosomas=conjunt_individus.get_individu_by_id(numero_individu).get_parell_cromosomes()
            
            info=Subelement(cromosomas,[conjunt_individus.get_individu_by_id(numero_individu)])

            self.__taula[h].append(Element(nom_tret, info))
            self.__n += 1
        alfa = self.__n / self.__M
        if alfa >= 1:
            self.__rehash()

          
    def treure_tret(self, tret, numero_individu):
        """
        Elimina la parella (clau, valor) del diccionari. Si la clau no pertany al
        diccionari, res canvia.
        cas pitjor: Theta(n). cas mitjà: Theta(1+n/M).
        """
        h = hash(tret) % len(self.__taula)
        p = self.__posicio(tret, h)
        element=self.__taula[h][p].info_tret
        individuos= element.individus
        tetret=False
        i=0
        if p != None:
            while i < len(individuos):
                if individuos[i].get_id_by_individu() == numero_individu:
                    tetret=True
                    individuos.pop(i)
                    break
                i+=1
            if len(individuos)==0 : 
                conjunt_individus.treure_tret(tret,numero_individu)
  
                self.__taula[h][p] = self.__taula[h][-1]
                self.__taula[h].pop()
                self.__n -= 1
            
            elif tetret:
                conjunt_individus.treure_tret(tret,numero_individu)
                element._replace(interseccio=conjunt_individus.get_individu_by_id(individuos[0]).get_parell_cromosomes())
                for i in individuos:
                    cromosomas=conjunt_individus.get_individu_by_id(i).get_parell_cromosomes()
                    intersection= parell_cromosomes.interseccion(element.interseccio,cromosomas)
                    element._replace(interseccio=intersection)    
        else:
                return 'error'

                    
    def consulta_tret(self, tret):
        """
        retorna el valor associat a una clau, None si la clau no hi és
        cas pitjor: Theta(n). cas mitjà: Theta(1+n/M).
        """
        h = int(hash(tret) % len(self.__taula))
        p = int(self.__posicio(tret, h))
        element=self.__taula[h][p].info_tret
        if p is not None:
            interseccio=element.interseccio
            individus=element.individus
            return (interseccio.get_cromosomas(),individus)
        else:
            return None
