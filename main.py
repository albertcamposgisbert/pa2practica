
import sys
from easyinput import read

#Clases
from class_conjunt_individus import *
from class_conjunt_trets import *
from class_experiment import *

sys.stdin = open(sys.argv[1], 'r')
comanda = read()

conjunt_trets=conjunt_trets()


while comanda != "fi":
    
    print(comanda)

    if comanda == "experiment":
        #Must generate an instance of "conjunt trets" and "conjunt d'individus"
        experiment = experiment()
        
    elif comanda == "consulta_individu":
        
        conjunt_individus.consulta_individu()
    
    elif comanda == "afegir_tret":
        #Must add tret into trets instance
        #Modificar (Incluir en trets o conjunt trets)
        conjunt_individus.afegir_tret()
        conjunt_trets.afegir_tret(tret) #Falta aclarar
        
        pass
        
    elif comanda == "treure_tret":
        #Must remove tret from trets instance
        conjunt_trets.treure_tret()
        conjunt_individus.treure(tret) #Falta aclarar

    elif comanda == "consulta_tret":  #Si que tiene que imprimir el main porque lo que la clase le devolverá será dos cosas, la intersección y los individuos que la tienen
        
        tret = read(str)
        inter,individ= conjunt_trets.consulta(tret)
        print(f"consulta tret {tret}")
        # Llamar función que muestre el id del tret, los cromosomas, i los individuos involucrados (quizás __str__ de clase tret)
        

    elif comanda == "distribució_tret":
        pass
    
    comanda = read()

        