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
        """
        Encuentra la intersección entre dos instancias de parell_cromosomes y la devuelve como una nueva instancia
        de esta clase.
        """
        i=0
        a1,b1=list(self.__cromosoma1),list(self.__cromosoma2) #guardamos en forma de lista el primer y segundo cromosoma de la instancia self
        a2,b2=list(e1.__cromosoma1),list(e1.__cromosoma2)     #hacemos lo mismo con la instancia dada como argumento

        a1_a2=[]
        b1_b2=[]
        m=len(a1)
        p1=''
        p2=''
        while i<m: #mientras no hayamosrecorrido todos digitos de los cromosomas miramos la intersección
            if a1[i]==a2[i]: #si son iguales lo guardamos(intersección)
                a1_a2.append(a1[i])
            else: #si no ponemos un guión
                a1_a2.append('-')
            if b1[i]==b2[i]: #lo mismo pero con los segundos cromosomas de cada par
                b1_b2.append(b1[i])
            else:
                b1_b2.append('-')
            if a1_a2[i]=='-' or b1_b2[i]=='-': #si alguna de las dos elementos guardados es un guión, forzamos el guión en los dos 
                a1_a2[i]='-'
                b1_b2[i]='-'
            p1+=a1_a2[i] #guardamos las intersecciones encontradas como string
            p2+=b1_b2[i]
            i+=1
        a=p1+p2 #creamos una instancia de parell_cromosomes y eso retornamos.
        cl= parell_cromosomes(a)
        return cl
