"""
Herramientas de Big Data - Taller OOP
Estudiantes: Daniel Pareja, John Jairo Rojas, Caren Natalia Piñeros
Universidad de la Sabana
Profesor: Hugo Franco, Ph.D.
27 de agosto de 2025

Programa principal para demostrar los 7 challenges del taller de POO
"""

import math
from Calculadora import Calculadora
from CalcContinua import CalculadoraContinua
from CalcCientifica import CalculadoraCientifica


def print_separator(title):
    """Función auxiliar para imprimir separadores visuales"""
    print("\n" + "="*60)
    print(f" {title} ")
    print("="*60)


def challenge1():
    """Challenge 1: Refactorización del Constructor"""
    print_separator("CHALLENGE 1: Refactorización del Constructor")
    
    print("\nAntes: El constructor ejecutaba la operación automáticamente")
    print("Ahora: El constructor solo inicializa los atributos")
    
    # Crear calculadora sin ejecutar operación
    calc = Calculadora(5, 3, '+')
    print(f"\nCalculadora creada: {calc}")
    print("Nota: La operación NO se ejecutó automáticamente")
    
    # Ahora ejecutamos la operación manualmente
    resultado = calc.suma()
    print(f"Resultado al llamar suma(): {resultado}")


def challenge2():
    """Challenge 2: Consistencia en las Operaciones"""
    print_separator("CHALLENGE 2: Consistencia en las Operaciones")
    
    calc = Calculadora()
    
    print("\nProbando que todos los métodos establecen self.operacion:")
    
    # Probar suma
    calc.suma(5, 3)
    print(f"Después de suma(5,3): {calc}")
    
    # Probar multiplicación
    calc.multiplicacion(4, 2)
    print(f"Después de multiplicacion(4,2): {calc}")
    
    # Probar división
    calc.division(10, 2)
    print(f"Después de division(10,2): {calc}")
    
    # Probar resta
    calc.resta(8, 3)
    print(f"Después de resta(8,3): {calc}")


def challenge3():
    """Challenge 3: Mejora de la Representación String"""
    print_separator("CHALLENGE 3: Mejora de la Representación String")
    
    # Calculadora sin operación
    calc1 = Calculadora(5, 3)
    print(f"\nCalculadora sin operación: {calc1}")
    
    # Calculadora con operación
    calc2 = Calculadora(5, 3, '+')
    print(f"Calculadora con operación: {calc2}")
    
    # Ejecutar operación y mostrar
    calc1.multiplicacion(5, 3)
    print(f"Después de ejecutar multiplicación: {calc1}")


def challenge4():
    """Challenge 4: Operaciones de un Solo Operando"""
    print_separator("CHALLENGE 4: Operaciones de un Solo Operando")
    
    calc = Calculadora()
    
    # Probar potencia
    print("\nPrueba de potencia:")
    resultado = calc.potencia(2, 3)
    print(f"2^3 = {resultado}")
    print(f"Estado de la calculadora: {calc}")
    
    # Probar raíz cuadrada
    print("\nPrueba de raíz cuadrada:")
    resultado = calc.raiz(16)
    print(f"√16 = {resultado}")
    
    # Probar raíz de número negativo
    print("\nPrueba de raíz con número negativo:")
    resultado = calc.raiz(-4)
    print(f"√(-4) = {resultado}")


def challenge5():
    """Challenge 5: Method Chaining para Cálculos Continuos"""
    print_separator("CHALLENGE 5: Method Chaining")
    
    print("\nOperaciones encadenadas con CalculadoraContinua:")
    
    # Ejemplo básico
    calc = CalculadoraContinua(10)
    result = calc.suma(5).multiplicacion(2)
    print(f"\n10 + 5 = 15, 15 * 2 = {result.operando1}")
    
    # Cadena más compleja
    calc2 = CalculadoraContinua(100)
    calc2.suma(50).division(3).resta(20).multiplicacion(2)
    print(f"\n100 + 50 = 150")
    print(f"150 / 3 = 50")
    print(f"50 - 20 = 30")
    print(f"30 * 2 = {calc2.operando1}")
    
    # Demostrar que cada método retorna el objeto
    calc3 = CalculadoraContinua(5)
    print(f"\nTipo retornado por suma(): {type(calc3.suma(3))}")
    print(f"Es el mismo objeto: {calc3.suma(2) is calc3}")


def challenge6():
    """Challenge 6: CalculadoraCientifica con Herencia"""
    print_separator("CHALLENGE 6: CalculadoraCientifica con Herencia")
    
    calc = CalculadoraCientifica()
    
    print("\nFunciones trigonométricas:")
    
    # Seno
    print(f"\nsen(π/2) = {calc.sin(math.pi/2)}")
    print(f"sen(30°) = sen(π/6) = {calc.sin(math.pi/6)}")
    
    # Coseno
    print(f"\ncos(0) = {calc.cos(0)}")
    print(f"cos(π) = {calc.cos(math.pi)}")
    
    # Tangente
    print(f"\ntan(π/4) = {calc.tan(math.pi/4)}")
    print(f"tan(0) = {calc.tan(0)}")
    
    # Demostrar que hereda métodos de la clase padre
    print("\nMétodos heredados de Calculadora:")
    print(f"5 + 3 = {calc.suma(5, 3)}")
    print(f"10 * 2 = {calc.multiplicacion(10, 2)}")


def challenge7():
    """Challenge 7: Manejo Robusto de Errores"""
    print_separator("CHALLENGE 7: Manejo Robusto de Errores")
    
    calc = Calculadora()
    
    print("\nPruebas de manejo de errores:")
    
    # TypeError en suma
    print("\n1. Suma con string:")
    resultado = calc.suma(5, 'a')
    print(f"Resultado: {resultado}")
    
    # TypeError en división
    print("\n2. División con string:")
    resultado = calc.division(10, 'b')
    print(f"Resultado: {resultado}")
    
    # ZeroDivisionError
    print("\n3. División por cero:")
    resultado = calc.division(10, 0)
    print(f"Resultado: {resultado}")
    
    # Operación válida para comparar
    print("\n4. División válida:")
    resultado = calc.division(10, 2)
    print(f"10 / 2 = {resultado}")
    
    # Probar con otros tipos de datos
    print("\n5. Multiplicación con lista:")
    resultado = calc.multiplicacion([1, 2], 3)
    print(f"Resultado: {resultado}")


def main():
    """Función principal que ejecuta todos los challenges"""
    print("\n" + "*"*70)
    print("*" + " "*68 + "*")
    print("*" + " "*15 + "TALLER POO - CLASES Y OBJETOS EN PYTHON" + " "*14 + "*")
    print("*" + " "*68 + "*")
    print("*"*70)
    
    # Ejecutar todos los challenges
    challenge1()
    challenge2()
    challenge3()
    challenge4()
    challenge5()
    challenge6()
    challenge7()
    
    print("\n" + "*"*70)
    print("*" + " "*25 + "FIN DEL PROGRAMA" + " "*27 + "*")
    print("*"*70 + "\n")


if __name__ == "__main__":
    main()