import random


def run() :
    numero_adivinanza= random.randint(1 , 100)
    numero = int(input("Por favor Inserte el Número que cree que la computadora generó"))
    while numero != numero_adivinanza:
        if numero > numero_adivinanza :
            numero = int(input("Por favor ingresa un Número mas bajo"))
        else :
            numero = int(input("Por favor ingresA un Número mas alto"))
    print("Adivinaste, Haz Ganado")
          

if __name__ == "__main__":
 run()