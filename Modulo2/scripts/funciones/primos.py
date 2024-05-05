# funciones, es aquella que realiza un calculo -> Calculame la raiz cuadra de un numero retornan valores
# procedimiento, son aquellos que realizan una tarea -> Realiza un reporte

def validar_primo(numero):
    """Valida si un número dado es primo o no lo es"""
    es_primo = True
    for i in range(2, numero):
        # busco un divisor
        if numero % i ==0:
            es_primo=False
            break
    # returno un boleano
    return es_primo

def elevar_cuadrado(numero):
    """Retorna la potencia cuadratica de un numero"""
    return numero**2

# Evalua si el numero 103 es primo
x = validar_primo(numero=103)
# x = validar_primo(numero=100000000000000081)
# si true, es primo, else, no es primo
if x:
    print(f'El número  es Primo')
else:
    print(f'El número es NO Primo')


# Evaluame los siguientes numeros para saber si son primos o no lo son [50, 20, 78, 96, 45]


listado_numeros_evaluar = [50, 20, 78, 96, 45]


for numero_evaluar in listado_numeros_evaluar:
    # evaluo si es primo o no
    y = validar_primo(numero_evaluar)
    if y:
        print(f'El número {numero_evaluar} es Primo')
    else:
        print(f'El número {numero_evaluar} es NO Primo') 















