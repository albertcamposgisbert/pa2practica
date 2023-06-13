"""
Parell de Cromosomes: L'estat (privat!) de les instàncies d'aquesta classe pot
consistir en un (o més) contenidors amb els bits dels cromosomes. Quines operacions us
fan falta (els mètodes públics) és quelcom que heu de decidir vosaltres.

"""

class parell_cromosomes:
    
    def __init__(self, cromosomes = "") -> None:
        self.__cromosomes = cromosomes
        
    def __str__(self):
        # str method must return "parell de cromosomes" in the data type in which they are contained.
        pass
    
    def interseccio(self, parell_cromosomes):
        pass