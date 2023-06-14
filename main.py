
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

conjunt_trets=conjunt_trets()


while comanda != "fi":
    
    print(comanda)

    if comanda == "experiment":
        #Must generate an instance of "conjunt trets" and "conjunt d'individus"
        experiment = experiment()
        
    elif comanda == "consulta_individu":
        
        numero_individu = read(int)
        individu = conjunt_individus.get_individu(numero_individu)
        print(f"consulta individu {numero_individu}")
        print(individu)
        pass
    
    elif comanda == "afegir_tret":
        #Must add tret into trets instance
        #Modificar (Incluir en trets o conjunt trets)
        tret = read(str)
        numero_individu = read(int)
        conjunt_trets.afegir_tret(tret,numero_individu)
        conjunt_individus.afegeix(tret,numero_individu)
        pass
        
    elif comanda == "treure_tret":
        #Must remove tret from trets instance
        
        conjunt_trets.treure_tret(tret,numero_individu)
        conjunt_individus.treure(tret,numero_individu)

                                      #Se tienen que crear en algun momento las instancias de las clases
    elif comanda == "consulta_tret":  #Si que tiene que imprimir el main porque lo que la clase le devolverá será dos cosas, la intersección y los individuos que la tienen
        
        tret = read(str)
        inter,individ= conjunt_trets.consulta(tret)
        print(f"consulta tret {tret}")
        # Llamar función que muestre el id del tret, los cromosomas, i los individuos involucrados (quizás __str__ de clase tret)
        

    elif comanda == "distribució_tret":
        pass
    
    comanda = read()

        