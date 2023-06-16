"""
Parell de Cromosomes: L'estat (privat!) de les instàncies d'aquesta classe pot
consistir en un (o més) contenidors amb els bits dels cromosomes. Quines operacions us
fan falta (els mètodes públics) és quelcom que heu de decidir vosaltres.

"""

class parell_cromosomes:
    
    def __init__(self, cromosomes = "") -> None:
        self.__mid=int(len(cromosomes)/2)
        self.__cromosoma1 = cromosomes[self.__mid:]
        self.__cromosoma2 = cromosomes[:self.__mid]
    def __str__(self):
        # str method must return "parell de cromosomes" in the data type in which they are contained.
        
        return f"{self.__cromosoma1}\n{self.__cromosoma2}"
    def get_cromosomas(self):
            
            return (self.__cromosoma1,self.__cromosoma2)	
    def interseccio(self,e1):
        i=0
        a1,b1=list(self.__cromosoma1[0]),list(self.__cromosoma2[1])
        a2,b2=list(e1.__cromosoma1[0]),list(e1.__cromosoma2[1])
        a1_a2=[]
        b1_b2=[]
        m=len(a1)
        p1=''
        p2=''
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
            p1+=a1_a2[i]
            p2+=b1_b2[i]
            i+=1
        #inter=(a1_a2,b1_b2)
        inter=(p1,p2)
        a=inter[0]
        a+=inter[1]    
        cl= parell_cromosomes(a)
        return cl
