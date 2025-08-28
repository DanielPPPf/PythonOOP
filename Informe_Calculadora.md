# Herramientas de Big Data
## Taller: Programación Orientada a Objetos - Clases y Objetos en Python

**Estudiantes:** Daniel Pareja, John Jairo Rojas y Caren Natalia Piñeros  
**Carrera:** Ingeniería Informática
**Universidad de la Sabana**  
**Maestría en Analítica Aplicada**  
**Profesor:** Hugo Franco, Ph.D.  
**27 de agosto de 2025**

---

## 1. Challenge 1: Refactorización del Constructor

### 1.1. Descripción del Problema

El constructor original de la clase Calculadora viola el principio de responsabilidad única al combinar la inicialización de atributos con la lógica de cálculo. Cuando se crea un objeto con `Calculadora(5, 3, '+')`, el constructor no solo inicializa los atributos sino que también ejecuta la operación e imprime el resultado inmediatamente. Este comportamiento es problemático porque mezcla la construcción del objeto con su uso, lo cual dificulta el control del flujo del programa y limita la reutilización del código. La importancia de este refactoring radica en establecer una separación clara entre la creación del objeto y su utilización.

### 1.2. Método de Solución

**Datos empleados:** La clase utiliza tres atributos principales:
- `operando1`: tipo numérico (int/float), primer operando de la operación
- `operando2`: tipo numérico (int/float), segundo operando de la operación  
- `operacion`: tipo string, símbolo de la operación (+, -, *, /)

**Algoritmo 1.** Refactorización del Constructor
```
procedimiento __init__(operando1: numérico, operando2: numérico, operacion: string)
    self.operando1 ← operando1
    self.operando2 ← operando2
    self.operacion ← operacion
fin procedimiento
```

La solución consiste en eliminar toda la lógica condicional del constructor, dejando únicamente la asignación de valores a los atributos. El código implementado se encuentra en el archivo `Calculadora.py`.

### 1.3. Resultados

Para ejecutar el código:
```python
from Calculadora import Calculadora
calc = Calculadora(5, 3, '+')
print(calc)  # Salida: 5+3
```

Como se observa, ahora el objeto se crea sin ejecutar automáticamente la operación. La representación string muestra la operación pendiente pero no el resultado.

### 1.4. Discusión

La refactorización mejora significativamente la arquitectura del código al separar las responsabilidades. Ahora el usuario tiene control total sobre cuándo ejecutar las operaciones, lo que permite crear objetos calculadora para uso posterior o modificar sus valores antes de realizar cálculos.

---

## 2. Challenge 2: Consistencia en las Operaciones

### 2.1. Descripción del Problema

Los métodos de operación presentaban un comportamiento inconsistente: mientras que el método `resta` establecía el atributo `self.operacion`, los métodos `suma`, `multiplicacion` y `division` no lo hacían. Esta inconsistencia puede generar bugs, especialmente al usar el método `__str__` que depende del valor de `self.operacion` para mostrar la representación del objeto correctamente.

### 2.2. Método de Solución

**Algoritmo 2.** Establecimiento Consistente de Operación
```
función suma(operando1: numérico, operando2: numérico): numérico
    self.operacion ← "+"
    si operando1 ≠ None y operando2 ≠ None entonces
        self.operando1 ← operando1
        self.operando2 ← operando2
    fin si
    retornar self.operando1 + self.operando2
fin función
```

La solución implementa la asignación del símbolo de operación en todos los métodos matemáticos al inicio de cada función.

### 3. Resultados

```python
calc = Calculadora()
calc.suma(5, 3)
print(calc)  # Salida: 5+3

calc.multiplicacion(4, 2)
print(calc)  # Salida: 4*2
```

### 4. Discusión

La consistencia en el código es fundamental para su mantenibilidad. Al establecer el mismo patrón en todos los métodos, se facilita la comprensión y se previenen errores futuros.

---

## 3. Challenge 3: Mejora de la Representación String

### 3.1. Descripción del Problema

El método `__str__` original fallaba cuando se creaba un objeto Calculadora sin especificar una operación, causando un error al intentar concatenar `None` con strings. Este problema afecta la usabilidad de la clase, ya que no todos los objetos calculadora necesariamente tienen una operación definida desde su creación.

### 3.2. Método de Solución

**Algoritmo 3.** Representación String Robusta
```
función __str__(): string
    si self.operacion = None entonces
        retornar "Calculadora sin operación definida"
    sino
        retornar concatenar(str(self.operando1), self.operacion, str(self.operando2))
    fin si
fin función
```

### 3.3. Resultados

```python
calc1 = Calculadora(5, 3)
print(calc1)  # Salida: Calculadora sin operación definida

calc2 = Calculadora(5, 3, '+')
print(calc2)  # Salida: 5+3
```

### 3.4. Discusión

La validación de estados nulos es esencial para crear código robusto. Esta mejora permite que la clase maneje graciosamente los casos donde no se ha definido una operación.

---

## 4. Challenge 4: Operaciones de un Solo Operando

### 4.1. Descripción del Problema

Las calculadoras modernas incluyen funciones que operan sobre un solo número, como elevar a una potencia o calcular la raíz cuadrada. La clase original solo soportaba operaciones binarias (dos operandos), limitando su funcionalidad.

### 4.2. Método de Solución

**Algoritmo 4.** Implementación de Potencia y Raíz Cuadrada
```
función potencia(operando1: numérico, operando2: numérico): numérico
    self.operacion ← "**"
    si operando1 ≠ None y operando2 ≠ None entonces
        self.operando1 ← operando1
        self.operando2 ← operando2
    fin si
    retornar self.operando1 ** self.operando2
fin función

función raiz(operando1: numérico): numérico
    self.operacion ← "√"
    si operando1 ≠ None entonces
        self.operando1 ← operando1
    fin si
    intentar
        retornar sqrt(self.operando1)
    capturar Exception como err
        imprimir("Gestión de excepciones:", err)
        retornar "valor no definido"
    fin intentar
fin función
```

### 4.3. Resultados

```python
calc = Calculadora()
print(calc.potencia(2, 3))  # Salida: 8
print(calc.raiz(16))        # Salida: 4.0
```

### 4.4. Discusión

La adición de operaciones unarias expande significativamente la utilidad de la calculadora. El manejo de excepciones en la función raíz previene errores con números negativos.

---

## 5. Challenge 5: Method Chaining para Cálculos Continuos

### 5.1. Descripción del Problema

En la implementación original, realizar una serie de cálculos requería crear nuevos objetos o actualizar manualmente los operandos después de cada operación. Esto resulta en código verboso y poco elegante. El method chaining permite encadenar operaciones de forma fluida, similar al funcionamiento de una calculadora física donde el resultado de una operación se convierte en el primer operando de la siguiente.

### 5.2. Método de Solución

Para implementar method chaining, se creó una nueva clase `CalculadoraContinua` que modifica el comportamiento de los métodos de operación. Los cambios principales son:
- Los métodos solo reciben un parámetro (`operando2`)
- El resultado se almacena en `self.operando1`
- Los métodos retornan `self` en lugar del resultado

**Algoritmo 5.** Method Chaining en Operaciones
```
función suma(operando2: numérico): objeto
    self.operacion ← "+"
    si self.operando1 ≠ None y operando2 ≠ None entonces
        self.operando2 ← operando2
        self.operando1 ← self.operando1 + operando2
    fin si
    retornar self
fin función
```

La implementación completa se encuentra en el archivo `CalculadoraContinua.py`.

### 5.3. Resultados

```python
from CalculadoraContinua import CalculadoraContinua
calc = CalculadoraContinua(10)
result = calc.suma(5).multiplicacion(2)
print(result.operando1)  # Salida: 30

# Cadena más larga
calc2 = CalculadoraContinua(100)
calc2.suma(50).division(3).resta(20).multiplicacion(2)
print(calc2.operando1)  # Salida: 60
```

### 5.4. Discusión

El method chaining mejora dramáticamente la expresividad del código, permitiendo escribir secuencias de operaciones de forma natural. Esta técnica es ampliamente utilizada en bibliotecas modernas de Python como pandas y permite un código más legible y conciso.

---

## 6. Challenge 6: CalculadoraCientifica con Herencia

### 6.1. Descripción del Problema

La herencia es un concepto fundamental en la programación orientada a objetos que permite crear nuevas clases basadas en clases existentes. El objetivo era extender la funcionalidad de la calculadora básica agregando operaciones trigonométricas sin duplicar código.

### 6.2. Método de Solución

Se implementó la clase `CalculadoraCientifica` que hereda de `Calculadora`, agregando métodos para funciones trigonométricas:

**Algoritmo 6.** Implementación de Funciones Trigonométricas
```
clase CalculadoraCientifica hereda de Calculadora
    función sin(operando1: numérico): numérico
        self.operacion ← "sin"
        si operando1 ≠ None entonces
            self.operando1 ← operando1
        fin si
        retornar sin(self.operando1)
    fin función
    
    # Similar para cos() y tan()
fin clase
```

El código completo está en `CalculadoraCientifica.py`.

### 6.3. Resultados

```python
from CalculadoraCientifica import CalculadoraCientifica
import math

calc = CalculadoraCientifica(math.pi/2)
print(calc.sin())  # Salida: 1.0
print(calc.cos(0))  # Salida: 1.0
print(calc.tan(math.pi/4))  # Salida: 0.9999999999999999
```

### 6.4. Discusión

La herencia permite reutilizar todo el código de la calculadora básica mientras se agregan nuevas funcionalidades. Esto demuestra el poder de la POO para crear jerarquías de clases que extienden comportamientos sin duplicar código.

---

## 7. Challenge 7: Manejo Robusto de Errores

### 7.1. Descripción del Problema

El código original solo manejaba `ZeroDivisionError` en el método de división. Sin embargo, los usuarios podrían intentar realizar operaciones con entradas no numéricas (strings, listas, etc.), causando `TypeError`. Un manejo robusto de errores es esencial para crear software confiable.

### 7.2. Método de Solución

Se implementó manejo de excepciones en todos los métodos de operación:

**Algoritmo 7.** Manejo de Errores en Operaciones
```
función división(operando1: any, operando2: any): numérico o None
    self.operacion ← "/"
    si operando1 ≠ None y operando2 ≠ None entonces
        self.operando1 ← operando1
        self.operando2 ← operando2
    fin si
    intentar
        retornar self.operando1 / self.operando2
    capturar TypeError como err
        imprimir("Entrada inválida:", err)
        retornar None
    capturar ZeroDivisionError como err
        imprimir("División por cero:", err)
        retornar None
    fin intentar
fin función
```

### 7.3. Resultados

```python
calc = Calculadora()
print(calc.suma(5, 'a'))  # Salida: Entrada inválida: unsupported operand type(s) for +: 'int' and 'str'
                          # None

print(calc.division(10, 0))  # Salida: División por cero: division by zero
                            # None

print(calc.division(10, 'b'))  # Salida: Entrada inválida: unsupported operand type(s) for /: 'int' and 'str'
                              # None
```

### 7.4. Discusión

El manejo diferenciado de excepciones permite proporcionar mensajes de error específicos y útiles al usuario. Retornar `None` en lugar de propagar la excepción permite que el programa continúe ejecutándose, mientras que los mensajes informativos ayudan a identificar el problema.

---

## Conclusiones Generales

Este taller demostró la importancia de los principios de diseño en la programación orientada a objetos:

1. **Separación de responsabilidades**: El constructor debe solo inicializar, no ejecutar lógica de negocio
2. **Consistencia**: Los métodos similares deben comportarse de manera similar
3. **Robustez**: El código debe manejar casos extremos graciosamente
4. **Extensibilidad**: La herencia permite agregar funcionalidad sin modificar código existente
5. **Usabilidad**: Técnicas como method chaining mejoran la experiencia del usuario

El desarrollo incremental de la calculadora, desde una implementación básica hasta versiones especializadas, ilustra cómo los conceptos de POO permiten crear código mantenible, extensible y robusto.

---
