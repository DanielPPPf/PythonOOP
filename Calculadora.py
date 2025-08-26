"""
Created on Wed Aug 2, 2025
@author: Hugo Franco
"""
import math

class Calculadora:
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
    
    def suma(self, operando1=None, operando2=None):
        self.operacion="+"
        if operando1 is not None and operando2 is not None:
            self.operando1=operando1
            self.operando2=operando2
        try:
            return self.operando1+self.operando2
        except TypeError as err:
            print('Entrada inválida:', err)
            return None
        
    def resta(self, operando1=None, operando2=None):
        self.operacion="-"
        if operando1 is not None and operando2 is not None:
            
            self.operando1=operando1
            self.operando2=operando2
        try:
            return self.operando1-self.operando2
        except TypeError as err:
            print('Entrada inválida:', err)
            return None

    def multiplicacion(self, operando1=None, operando2=None):
        self.operacion="*"
        if operando1 is not None and operando2 is not None:
            self.operando1=operando1
            self.operando2=operando2
        try:
           return self.operando1*self.operando2
        except TypeError as err:
            print('Entrada inválida:', err)
            return None
    
    def division(self, operando1=None, operando2=None):
        self.operacion="/"
        if operando1 is not None and operando2 is not None:
            self.operando1=operando1
            self.operando2=operando2
        try:
            return self.operando1/self.operando2
        except TypeError as err:
            print('Entrada inválida:', err)
            return None
        except ZeroDivisionError as err:
            print('División por cero:', err)
            return None

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