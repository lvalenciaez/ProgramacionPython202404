# 1. Librerias
import math

# import <nombre_archivo_python> [as alias_libreria]
import saludos

# from <nombre_carpeta> import <nombre_archivo> [as alias_libreria]
from calculos import basicos as b
from calculos.avanzados import calcular_factorial_recursivo 


# 2. Constantes
BIENVENIDA = 'Bienvenido al menu Interactivo'
OPCIONES_MENU = """
1. Saludar
2. Sumar dos numeros
3. Calcular factorial
4. Salir del Programa

"""
def get_number(msg:str='Ingrese un número: ')->int:
    """Funcion encargada del ingreso de un número entero"""

    try:
        return int(input(msg))
    except:
        print('Ingrese bien el numero ...')
        return get_number(msg=msg)
    
# Funciones y/o clases
def main():
    print(BIENVENIDA)

    while True:
        respuesta = input(OPCIONES_MENU)

        if respuesta=='1':
            saludos.saludar()
        elif respuesta=='2':
            numero1 = get_number()
            numero2 = get_number()

            suma = b.sumar(numero1, numero2)
            print(f'El resultado de la suma es {suma}')
        elif respuesta == '3':
            numero = get_number('Ingrese un número positivo para el calculo del factorial: ')
            factorial = calcular_factorial_recursivo(numero=numero)
            print(f'{numero}! = {factorial}')
        elif respuesta == '4':
            print('Saliendo del programa!')
            break
        else:
            break
    pass


# mi programa
if __name__ == '__main__':
    main()







