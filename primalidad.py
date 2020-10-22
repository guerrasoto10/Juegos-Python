#Todo número que sea solo divisible entre el mismo y el 1 (es decir con Resto==0 al dividir entre cualquier otro numero
# diferente a el mismo o a 1) es Primo
def es_primo(numero) :
    if numero == 1 :
        print (" El numero 1 por convenio no se considera numero primo")
        exit()
    contador = 0
    for i in range(1 , numero  + 1) :
        if i == 1 or i == numero :
            continue
        if numero % i == 0 :
            contador = contador + 1
            break
    if contador == 0 :
        return True
    else :
        return False


def run():
    numero=int(input("Ingrese el Número: "))
    if es_primo(numero) :
        print("El numero " + str(numero) + " SI es primo")
    else:
        print("El numero " + str(numero) + " NO es primo")



if __name__ == '__main__' :
    run()