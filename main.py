import sys
from easyinput import read

#Clases
from bintree import *
from class_conjunt_individus import *
from class_parell_cromosomes import *
from class_individu import *
from class_conjunt_trets import *
from class_experiment import *

sys.stdin = open(sys.argv[1], 'r')
comanda = read()

while comanda != "fi":
    
    print(comanda)

    if comanda == "experiment":
        #Must generate an instance of "conjunt trets" and "conjunt d'individus"
        """
        individus = conjunt_individus()
        trets = conjunt_trets()
        """    
        
    elif comanda == "consulta_individu":
        pass
    
    elif comanda == "afegir_tret":
        #Must add tret into trets instance
        """
        trets.afegir_tret()
        """
    elif comanda == "treure_tret":
        #Must remove tret from trets instance
        """
        trets.treure_tret()
        """
        
        
    elif comanda == "consulta_tret":
        """
        trets.consulta_tret()
        """

    elif comanda == "distribució_tret":
        pass

    else:
        pass
    
    comanda = read()

        