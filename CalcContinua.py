"""
Created on Wed Aug 2, 2025
@author: Hugo Franco
"""
import math

class CalculadoraContinua:
    """
    Implementa una calculadora
    """

    tipo='cientifica'
    
    def __init__(self,operando1=0, operando2=0, operacion=None):
        self.operando1=operando1
        self.operando2=operando2
        self.operacion=operacion


    def __str__(self):

        if self.operacion is None:
            return "Calculadora sin operación definida"
        else:
            return str(self.operando1)+self.operacion+str(self.operando2)
    
    def suma(self, operando2=None):
        self.operacion="+"
        if self.operando1 is not None and operando2 is not None:
            self.operando2=operando2
            self.operando1=self.operando1+operando2
            #self.operando2=operando2
        return self
        #return self.operando1+self.operando2
    
    def resta(self, operando2=None):
        self.operacion="-"
        if self.operando1 is not None and operando2 is not None:
            self.operando2=operando2
            self.operando1=self.operando1-operando2
        return self
    
    def multiplicacion(self, operando2=None):
        self.operacion="*"
        if self.operando1 is not None and operando2 is not None:
            self.operando2=operando2
            self.operando1=self.operando1*operando2
        return self
    
    
    def division(self, operando2=None):
        self.operacion="/"
        if self.operando1 is not None and operando2 is not None:
            self.operando2=operando2
            self.operando1=self.operando1/operando2
        try:
            return self
        except Exception as err:
            print('Gestión de excepciones:', err)
            return "valor no definido"
        
    def potencia(self, operando1=None, operando2=None):
        self.operacion="**"
        if operando1 is not None and operando2 is not None:
            self.operando1=operando1
            self.operando2=operando2
        return self.operando1**self.operando2
    
    def raiz(self, operando1=None):
        self.operacion="√"
        if operando1 is not None:
            self.operando1=operando1
        try:
            return math.sqrt(self.operando1)
        except Exception as err:
            print('Gestión de excepciones:', err)
            return "valor no definido"