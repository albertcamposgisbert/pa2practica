
import sys
from easyinput import read

#Clases
from class_conjunt_individus import *
from class_conjunt_trets import *

sys.stdin = open(sys.argv[1], 'r')
comanda = read()



while comanda != "fi":
    
    print(comanda)

    if comanda == "experiment":
        #Must generate an instance of "conjunt trets" and "conjunt d'individus"
        conjunt_indivudus = conjunt_individus()
        conjunt_trets_instance= conjunt_trets()

        
    elif comanda == "consulta_individu":
        individu_id = read(int)
        conjunt_individus.consulta_individu(individu_id)
    
    elif comanda == "afegir_tret":
        #Must add tret into trets instance
        #Modificar (Incluir en trets o conjunt trets)
        tret, individu_id = read(str), read(int)
        conjunt_individus.afegir_tret(tret, individu_id)
        conjunt_trets.afegir_tret(tret, individu_id) #Falta aclarar
        
        pass
        
    elif comanda == "treure_tret":
        #Must remove tret from trets instance
        tret, individu_id = read(str), read(int)
        conjunt_trets.treure_tret(tret, individu_id)
        conjunt_individus.treure(tret, individu_id) #Falta aclarar

    elif comanda == "consulta_tret":  #Si que tiene que imprimir el main porque lo que la clase le devolverá será dos cosas, la intersección y los individuos que la tienen
        
        tret = read(str)
        info= conjunt_trets.consulta_tret(tret)
        if info is None:
            return 'error'
        else:
            print(f"consulta tret {tret}",f"tiene intersección{info[0]}")
            print("individuos:")
            for i in info[1]:
                print(i.get_id_by_individu())
            # Llamar función que muestre el id del tret, los cromosomas, i los individuos involucrados (quizás __str__ de clase tret)
            

    elif comanda == "distribució_tret":
        pass
    
    comanda = read()

        

