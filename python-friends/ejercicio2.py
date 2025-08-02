def verificar_numero(numero):
    
    if numero == 10:
        return "Se ingresó el número 10"
    
    elif numero == 7:
        return "Se agregó un comodín"
    
    elif numero % 2 == 0:
        return f"El número {numero} es par"
    else:
        return f"El número {numero} es impar"


def main():
   
        numero = int(input("Ingrese un número: "))
        print ("nueva linea")
        
        resultado = verificar_numero(numero)
        print(resultado)

# Ejecutar el programa si se ejecuta directamente
if __name__ == "__main__":
    main()