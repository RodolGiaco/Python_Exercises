
#https://colab.research.google.com/drive/1gTZ96xhfMalGUv1SAuWQJKnApdyGIn35?usp=sharing 
class mamifero():
    #Contructor
    def __init__ (self,cantMamas,esperanzaDeVida):
        #Atributos
        self.cantMamas = cantMamas
        self.__esperanzaDeVida = esperanzaDeVida

    #Metodos
    def mamar(self):
        print("Estoy alimentandome")

    def nacer(self):
        print("Estoy naciendo")

class animalMarino(mamifero):
    #Contructor  
    def __init__ (self,tieneBranqueas,especie):
        #Atributos
        self.__tieneBranqueas = tieneBranqueas
        self.__especie = especie
    #Metodos
    def nadar(self):
        print("Estoy nadando")
        

class cetaceo(animalMarino,mamifero):
    #Contructor
    def __init__(self, notas, viveEn, peso):
        mamifero.__init__(self,cantMamas=None,esperanzaDeVida=None)
        self.__notas = notas
        self.__viveEn = viveEn 
        self.__peso = peso

    #Metodos 
    def nacer(self):
        padre = mamifero.nacer(self)
        #Entiendo que la linea de abajo es porque animalMarino hereda de mamifero pero si la borro funciona igual
        #animalMarino.nacer(self) 
        return padre
    


cetaceo1 = cetaceo("Nose","Mendoza",100)
cetaceo1.mamar()
cetaceo1.nadar()
cetaceo1.nacer()
