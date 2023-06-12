
"""
Conjunt de Trets: L'estat (privat!) de les instàncies d'aquesta classe (en realitat
només en caldrà una per experiment) consistirà en un diccionari de parelles
(nom_tret, info_tret), on nom_tret és una string i info_tret pot ser una tupla
de dos elements, una instància de Parell de Cromosomes i un conjunt d'instàncies
d'Individu (aquells que tenen el tret). Aquí, l'expressió conjunt es refereix a
l'estructura de dades set, que Python ens proporciona
. Quines operacions us fan falta (els mètodes públics) és quelcom que heu de decidir vosaltres.
"""


class conjunt_trets:
    
    def __init__(self) -> None:
        
        __conjunt_trets = {} # Clave : tret | Valor : info de tret
        pass
    
    def __str__(self) -> None:
        
        # Debe dar la info del tret consultado en el main (consulta tret).
        pass
    
    def afegir_tret(self, numero_individu):
        pass
    
    def treure_tret(self, tret):
        pass
    
    def get_individus_amb_tret(self, tret):
        pass
    
    def actualitzar_tret(self, tret):
        pass
    
    
    
    
