
import sys
from easyinput import read

#Clases
from class_conjunt_individus import *
from class_conjunt_trets import *

sys.stdin = open(sys.argv[1], 'r')
comanda = read()



while comanda != "fi":
    
    print(comanda, end=' ')

    if comanda == "experiment":
        #Must generate an instance of "conjunt trets" and "conjunt d'individus"
        num_individus = read(int) # Nombre d'individus
        num_cromosomas = read(int) # Nombre de gens de cada cromosoma
        print(f"{num_individus} {num_cromosomas}")
        
        conjunt_individus_instance = conjunt_individus(num_individus, num_cromosomas)
        conjunt_trets_instance= conjunt_trets(conjunt_individus_instance)

        
    elif comanda == "consulta_individu":
        individu_id = read(int)
        print(individu_id)
        conjunt_individus_instance.consulta_individu(individu_id)
    
    elif comanda == "afegir_tret":
        #Must add tret into trets instance
        #Modificar (Incluir en trets o conjunt trets)
        tret, individu_id = read(str), read(int)
        conjunt_trets_instance.afegir_tret(tret, individu_id) #Falta aclarar
        
        
        
    elif comanda == "treure_tret":
        #Must remove tret from trets instance
        tret, individu_id = read(str), read(int)
        conjunt_trets_instance.treure_tret(tret, individu_id)

    elif comanda == "consulta_tret":  #Si que tiene que imprimir el main porque lo que la clase le devolverá será dos cosas, la intersección y los individuos que la tienen
        
        tret = read(str)
        info= conjunt_trets_instance.consulta_tret(tret)
        if info is None:
            print(f"{tret}")
            print("error")
        else:
            print(f"{tret}")
            print(f"{tret}")
            print(f"{info[0][0]}")
            print(f"{info[0][1]}")
            for i in info[1]:
                print(i.get_id_by_individu(),end='')
            print()
            

    elif comanda == "distribució_tret":
        pass
    
    comanda = read()

        

