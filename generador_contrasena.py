# Generamos contrasena de 15 digitos partiendo de los caracteres disponibles
import random


def generar_contrasena() :
    mayusculas = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
    minuscula =  ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']
    simbolos= ['!' , '@' , '#' , '$' , '%' , '&' , '/' , '(' , ')']
    numeros = ['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '0']
    todos_caracteres = mayusculas + minuscula + simbolos + numeros
    contrasena = []
#seleccionamos un caracter de todos_caracteres y vamos agregando a contrasena hasta tenter 15
    for i in range(15) :
        caracter_random= random.choice(todos_caracteres)
        contrasena.append(caracter_random)
#convertimos lista en string
    contrasena = ''.join(contrasena)
    return contrasena

def run() :
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es " + contrasena)
    print(10/2+5*7)



if __name__ == '__main__' :
    run()