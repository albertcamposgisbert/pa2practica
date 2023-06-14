
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
from collections import namedtuple
Element = namedtuple("Element", ["nom_tret", "info_tret"])
Subelement= namedtuple("Subelement", ["interseccio", "individus"])
class conjunt_trets:
    
    def __init__(self) -> None:
        self.__M = 10000
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
        for i in range(len(l)):
            if l[i].nom_tret == nom_tret:
                return i
        return None

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
            elem2=elem.info_tret
            interseccio_original= elem2.interseccio

            cromosomes_nou_element=conjunt_individus.consulta_individu(numero_individu)

            nova_interseccio=self.interseccion(interseccio_original,cromosomes_nou_element)

            elem2.individus.append(numero_individu)

            elem2._replace(interseccio=nova_interseccio)
            self.__taula[h][p] = elem._replace(info_tret=elem2) # Genera NOU element
        else:
            cromosomas=conjunt_individus.consulta_individu(numero_individu)
            info=Subelement(cromosomas,[numero_individu])
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
        if p != None:
            for i in individuos:
                if i==numero_individu:
                    tetret=True
                    individuos.pop(i)
                    break
            if len(individuos)==0 :    
                self.__taula[h][p] = self.__taula[h][-1]
                self.__taula[h].pop()
                self.__n -= 1
            
            elif tetret:
                element._replace(interseccio=conjunt_individus.consulta_individu(individuos[0]))
                for i in individuos:
                    cromosomas=conjunt_individus.consulta_individu(i)
                    intersection= self.interseccion(element.interseccio,cromosomas)
                    element._replace(interseccio=intersection)


                    
    def consulta_tret(self, tret):
        """
        retorna el valor associat a una clau, None si la clau no hi és
        cas pitjor: Theta(n). cas mitjà: Theta(1+n/M).
        """
        h = hash(tret) % len(self.__taula)
        p = self.__posicio(tret, h)
        element=self.__taula[h][p].info_tret
        if p is not None:
            interseccio=element.interseccio
            individus=element.individus
            return interseccio,individus
        else:
            return None
    def interseccion(self,el1,el2):
        i=0
        a1,b1=list(el1[0]),list(el1[1])
        a2,b2=list(el2[0]),list(el2[1])
        a1_a2=[]
        b1_b2=[]
        m=len(a1)
        #p1=''
        #p2=''
        while i<m:
            if a1[i]==a2[i]:
                a1_a2.append(a1[i])
            else:
                a1_a2.append('-')
            if b1[i]==b2[i]:
                b1_b2.append(b1[i])
            else:
                b1_b2.append('-')
            if a1_a2[i]=='-' or b1_b2[i]=='-':
                a1_a2[i]='-'
                b1_b2[i]='-'
            #p1+=a1_a2[i]
            #p2+=b1_b2[i]
            i+=1
        inter=(a1_a2,b1_b2)
        #inter=(p1,p2)    
        return inter
    
