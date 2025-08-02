class Numero:
    def __init__(self, numero):
        self.numero = numero
    def EvaluarNumero(self):
        if self.numero & 1:
            print("impar")
            if self.numero == 7:
                print("\n el numero ingresado es un comodin")
        else:
            print("par")
            if self.numero == 10:
                print("\n el numero ingresado es 10")
    def sumar(self, numerosumar):
        return self.numero + numerosumar
    
if __name__ == "__main__":
    # Create Numero instance with input value
    numero = int(input("Ingrese un número: \n"))
    numeroevaluar = Numero(numero)
    numeroevaluar.EvaluarNumero()
    sumarealizada = numeroevaluar.sumar(9)
    print("la suma realizada es", sumarealizada)
