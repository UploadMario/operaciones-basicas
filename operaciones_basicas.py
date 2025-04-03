"""
Módulo de operaciones básicas y cálculo de promedio.
Este script define clases para realizar operaciones matemáticas simples y calcular
el promedio de una lista de números.
"""


class OperacionesBasicas:
    """Clase para realizar operaciones matemáticas básicas."""

    def __init__(self):
        """Inicializa la clase con un atributo resultado."""
        self.resultado = 0

    def sumar(self, a, b):
        """Suma dos números y almacena el resultado."""
        self.resultado = a + b

    def restar(self, a, b):
        """Resta dos números y almacena el resultado."""
        self.resultado = a - b

    def obtener_resultado(self):
        """Devuelve el resultado de la última operación realizada."""
        return self.resultado


class CalculadoraPromedio:
    """Clase para calcular el promedio de una lista de valores."""

    def __init__(self, valores):
        """Inicializa la clase con una lista de valores."""
        self.valores = valores

    def calcular_promedio(self):
        """Calcula y devuelve el promedio de los valores proporcionados."""
        suma_total = sum(self.valores)
        return suma_total / len(self.valores) if self.valores else 0

    def obtener_valores(self):
        """Devuelve la lista de valores almacenados."""
        return self.valores


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20


# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora = CalculadoraPromedio(NUMEROS)
    promedio_resultado = calculadora.calcular_promedio()
    print(f"El promedio de los números es: {promedio_resultado}")
