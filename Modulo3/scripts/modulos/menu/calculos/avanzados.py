def calcular_factorial_recursivo(numero:int)->int:
    """Funcion que realiza el calculo del factorial de un numero de forma recursiva"""

    # validando que numero no sea negativo
    assert numero>=0, 'Numero ingresado es negativo'

    if numero in [0,1]:
        return 1
    return calcular_factorial_recursivo(numero-1) * numero

if __name__ == '__main__':
    print(calcular_factorial_recursivo(5))