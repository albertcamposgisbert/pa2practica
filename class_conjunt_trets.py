
"""
Conjunto de características: el estado (¡privado!) de las instancias de esta clase (en realidad
sólo será necesaria una por experimento) consistirá en un diccionario de pares clave valor donde la clave será el
el nombre de la características indicadas e info_tret será una tupla
de dos elementos: una instancia de Par de Cromosomas y una lista de instancias
de Individuo (aquellos que tienen la característica)
"""
from class_conjunt_individus import *
from class_parell_cromosomes import *
from collections import namedtuple
from bintree import BinTree

Element = namedtuple("Element", ["interseccio", "individus"]) 

class conjunt_trets:
    
    def __init__(self,conj):
        """
        Esta clase se instancia en el main usando de argumento la instancia de la anteriormente
        inicializada clase conjunt_individus y se crea el diccionario que usaremos.
        """
        self.__conjunt_individus=conj
        self.__trets={}

    
    def distribucio_trets(self, tret):
        def distribucio_trets_aux(arbol):
            if arbol.empty():
                return None
            arbol_resultado= None
            if self.__conjunt_individus.get_individu_by_id(arbol.get_root()).te_tret(tret):
                arbol_resultado=BinTree(arbol.get_root())
            if distribucio_trets_aux(arbol.get_left()) is not None:
                if arbol_resultado is None:
                    arbol_resultado=BinTree(-arbol.get_root())
                arbol_resultado.set_left(distribucio_trets_aux(arbol.get_left()))
            if distribucio_trets_aux(arbol.get_right()) is not None:
                if arbol_resultado is None:
                    arbol_resultado=BinTree(-arbol.get_root())
                arbol_resultado.set_right(distribucio_trets_aux(arbol.get_right()))
            return arbol_resultado
        
        arbol_resultado=distribucio_trets_aux(self.__conjunt_individus.get_arbre())
        if arbol_resultado is None:
            print(f"\nerror")    
        else:
            cadena=arbol_resultado.inorder()
            cadena_print=' '.join(str(elemento) for elemento in cadena)
            print(f"\n{cadena_print}")



           


    def afegir_tret(self,nom_tret,numero_individu):
        """
        Asigna información a una clave. Si la clave ya esta en el diccionario hacemos los cambios correspondientes
        (añadimos el nuevo individuo(añadimos su instancia de clase individuo) y la nueva intersección). Si el 
        individuo dado ya se había introducido se imprime un error y no se añade. Lo mismo sucede si el individuo
        no es uno de los indicados inicialmente
        """
        m=self.__conjunt_individus.get_num_individuos() #Obtenemos el número de individuos, que también es el máximo
                                                        #individuo que podemos tener y todo individuo de número más grande
                                                        #no es uno de los indicados al inicio(tampoco si es menor que 1)
        if numero_individu>m or numero_individu<1:
            print('error')
        else:
            if nom_tret in self.__trets: #Si tenemos ya la característica en el diccionario vemos primero
                elem=self.__trets[nom_tret] #si ya hemos introducido ese individuo, en ese caso imprimimos un error
                for i in elem.individus:
                    if i.get_id_by_individu() == numero_individu:
                        print('error')
                        return 0                                                
                self.__conjunt_individus.afegir_tret(nom_tret,numero_individu)#Si llamamos a el método hómologo a este de la clase conjunt_individus
                                                                              #y añadimos al individuo correspondiente la característica indicada                                            
                interseccio_original=elem.interseccio                         #a continuación introducimos la instancia correspondiente de la clase individuos
                                                                              #en nuestra lista y encontramos la nueva intersección, que también guardamos en el diccionario
                cromosomes_nou_element=self.__conjunt_individus.get_individu_by_id(numero_individu).get_parell_cromosomes()
                nova_interseccio=interseccio_original.interseccio(cromosomes_nou_element)
                elem.individus.append(self.__conjunt_individus.get_individu_by_id(numero_individu))
                self.__trets[nom_tret]=Element(nova_interseccio,elem.individus)
            else: #Si no estaba en el diccionario ya, cogemos su par de cromosomas y lo guardamos como intersección
                  #ademas de guardar en una lista, que también creamos ahora, el individuo que tendrá esta característica
                  #la tupla resultante será el valor del diccionario y la clave el nombre de la característica.
                self.__conjunt_individus.afegir_tret(nom_tret,numero_individu) #como antés, añadimos la característica a la lista de características del individuo en la clase conjunt_individuos
                cromosomas=self.__conjunt_individus.get_individu_by_id(numero_individu).get_parell_cromosomes()
                self.__trets[nom_tret]=Element(cromosomas,[self.__conjunt_individus.get_individu_by_id(numero_individu)])
    def treure_tret(self, tret, numero_individu):
        """
        Elimina de la lista de individuos de la característica correspondiente el individuo indicado y se
        recalcula la intersección si es necesario o se elimina la característica.
        """
        
        if tret in (self.__trets): #miramos si la característica en cuestión está en el diccionario
            tetret=False
            i=0
            element=self.__trets[tret]
            individuos= element.individus

            for a in individuos: #si el individuo no está para ser eliminado imprimimos error
                if a.get_id_by_individu() != numero_individu:
                    print('error')
                    break

            while i < len(individuos): #Encontramos el individuo indicado y lo eliminamos
                if individuos[i].get_id_by_individu() == numero_individu:
                    tetret=True
                    individuos.pop(i)
                    break
                i+=1

            if len(individuos)<1 : #si el tamaño de la lista de individuos resultante es menor que uno eliminamos
                                    #la característica
                self.__conjunt_individus.treure_tret(tret,numero_individu)#llamamos al homologo de mismo nombre de la clase conjunt_individus para eliminar la característica
                                                                          #de la lista de características del individuo
                del self.__trets[tret]
                tetret=False
            
            elif tetret: #en caso contrario recalculamos la intersección y guardamos la nueva intersección y 
                         #la nueva lista de individuos 
                        
                intersection=individuos[0].get_parell_cromosomes()
                self.__conjunt_individus.treure_tret(tret,numero_individu)#llamamos al homologo de mismo nombre de la clase conjunt_individus para eliminar la característica
                                                                          #de la lista de características del individuo

                for i in individuos:
                    cromosomas=i.get_parell_cromosomes()
                    intersection= intersection.interseccio(cromosomas)
                self.__trets[tret]=Element(intersection,individuos)
        else: #si no existe el tret del que queremos eliminar un individuo mostramos error
            print('error')
        
                
    def consulta_tret(self, tret):
        """
        Retorna una tupla de strings del par de cromosomas de la intersección de la característica indicada
        y la lista de individuos que poseen la característica.
        """
        if tret in self.__trets: #solo si existe el tret retornamos los valores, en caso contrario retornamos un None
                                 #que hará que el main retorne error.
            element=self.__trets[tret]
            interseccio = element.interseccio.get_cromosomas()
            individus=element.individus
            return (interseccio,individus)
        else:
            return None
