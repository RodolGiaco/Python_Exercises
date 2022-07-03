#https://colab.research.google.com/drive/1bpQDVkLEQrBX8KNen2fbQOpqy-f2pJBh?usp=sharing
class cuenta():
    #El contructor
    def __init__(self,titular,cantidad):
        #Atributos
        self.titular = titular 
        self.cantidad = cantidad


    def mostrar(self,titular,cuenta):
        print(f"El titular de la cuenta es {titular} y tiene un saldo en su cuenta de {cuenta}$")

    def ingresar(self,aux):
        global saldo
        dinero = int(input("Ingresar la cantidad de dinero a depositar?\n>>>"))
        while True:
            if dinero < 0:
                print("Saldo negativo, ingresar de nuevo\n>>>")
            else:
                print("Dinero ingresado con exito")
                saldo += dinero
                break
        
    def retirar(self,aux):
        global saldo
        retiro = int(input("Cuanto desea retirar?\n>>>"))
        saldo = aux - retiro
        print(f"Su saldo es {saldo}$")

titular = input("Ingresar titular de la cuenta\n>>>")     
saldo = int(input("Ingresar saldo disponible en su cuenta:\n>>>"))

cuenta1 = cuenta(titular,saldo)

cuenta1.mostrar(titular,saldo)
cuenta1.ingresar(saldo)
cuenta1.retirar(saldo)
cuenta1.mostrar(titular,saldo)

