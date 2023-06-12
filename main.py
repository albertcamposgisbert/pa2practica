
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
        
        nombre_individus = read(int)  #Nombre d'individus
        nombre_gens = read(int)  #Nombre de gens de cada cromosoma
        pass
        """
        individus = conjunt_individus()
        trets = conjunt_trets()
        """
        
    elif comanda == "consulta_individu":
        
        numero_individu = read(int)
        individu = conjunt_individus.get_individu(numero_individu)
        print(f"consulta individu {numero_individu}")
        print(individu)
        pass
    
    elif comanda == "afegir_tret":
        #Must add tret into trets instance
        
        tret = read(str)
        numero_individu = read(int)
        conjunt_trets.afegir_tret(tret, numero_individu)
        print(f"afegir tret {tret} {individu}")
        pass
        
    elif comanda == "treure_tret":
        #Must remove tret from trets instance
        """
        trets.treure_tret()
        """
        
    elif comanda == "consulta_tret":
        
        tret = read(str)
        print(f"consulta tret {tret}")
        # Llamar función que muestre el id del tret, los cromosomas, i los individuos involucrados (quizás __str__ de clase tret)
        

    elif comanda == "distribució_tret":
        pass
    
    comanda = read()

        