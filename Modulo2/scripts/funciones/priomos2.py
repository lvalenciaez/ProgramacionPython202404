"""
Evaluame los siguientes numeros para saber si son primos o no lo son [50, 20, 78, 96, 45]
"""

# 1. Importacion de librerias
import math

# 2. Colocamo constantes
LISTADO_NUMERO_EVALUAR = [50, 20, 78, 96, 45]

# 3. Funciones y/o clases
def validar_primo(numero):
    """Valida si un número dado es primo o no lo es"""
    es_primo = True

    limite_numero = int(math.sqrt(numero))

    for i in range(2, limite_numero+1):
        # busco un divisor
        if numero % i ==0:
            es_primo=False
            break
    # returno un boleano
    return es_primo

def main():
    for numero_evaluar in LISTADO_NUMERO_EVALUAR:
        # evaluo si es primo o no
        y = validar_primo(numero_evaluar)
        if y:
            print(f'El número {numero_evaluar} es Primo')
        else:
            print(f'El número {numero_evaluar} es NO Primo') 

    print('Programa finalizado')

# 4. llamo a mi programa
main()


# x = validar_primo(100000000000000081)
# print(x)