from Calculadora import Calculadora
import math

class CalculadoraCientifica(Calculadora):
    def __init__(self, operando1=0, operando2=0, operacion=None):
        super().__init__(operando1, operando2, operacion)

    def sin(self, operando1=None):
        self.operacion = "sin"
        if operando1 is not None:
            self.operando1 = operando1
        
        return math.sin(self.operando1)
    
    def cos(self, operando1=None):
        self.operacion = "cos"
        if operando1 is not None:
            self.operando1 = operando1
        
        return math.cos(self.operando1)
    
    def tan(self, operando1=None):
        self.operacion = "tan"
        if operando1 is not None:
            self.operando1 = operando1
        
        return math.tan(self.operando1)