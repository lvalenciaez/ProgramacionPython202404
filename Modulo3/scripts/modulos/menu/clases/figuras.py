import math
# crear una clase triangulo
class Triangulo:
    def __init__(self, base, altura):

        self.base = base
        self.altura = altura
        pass
    def calcular_area(self):
        """Calcula el areá de un triangulo"""
        return self.base * self.altura /2
    def __str__(self) -> str:
        return f'Triangulo de base {self.base} y altura {self.altura}'

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        pass
    def calcular_area(self):
        return self.base * self.altura
    def __str__(self) -> str:
        return f'Rectangulo de base {self.base} y altura {self.altura}'


class Cuadrado(Rectangulo):
    def __init__(self, lado) -> None:
        # herencia -> propiedades que se va a heredar de una clase
        super().__init__(base=lado, altura=lado)
        pass

    def __str__(self) -> str:
        # sobreescribiendo metodo __str__ de clase Rectangulo
        return f'Se tiene un cudarado de lado {self.base}'


# Generar una clase circulo
class Circulo:
    PI = 3.14
    def __init__(self, radio:float):
        self.radio = radio 
        pass

    def calcular_area(self):
        return self.PI * math.pow(self.radio,2)

    def __str__(self) -> str:
        return f'Circulo de radio {self.radio}'



# Creo mi objeto triangulo
triangulo1 = Triangulo(base=5, altura=8)

print(triangulo1)

area = triangulo1.calcular_area()
print(area)

# genero un objeto rectangulo
rectangulo = Rectangulo(base=8, altura=16)

print(rectangulo)

area = rectangulo.calcular_area()
print(area)

# genero un objeto cuadrado
cuadrado = Cuadrado(lado=4)

print(cuadrado)

area = cuadrado.calcular_area()
print(area)

# Genero un circulo
circulo = Circulo(5)
print(circulo)

print(circulo.calcular_area())