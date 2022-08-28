#계산기 

class Calculator(object):
    def __init__ (self,first,second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def minus(self):
        result = self.first - self.second
        return result
    
    def mult(self):
        result = self.first * self.second
        return result
    
    def divide(self):
        result = self.first / self.second
        return result
    
# c = calculator(a, b)

                
from app.models.calculator import Calculator

class CalculatorService(object):
    def __init__(self) -> None:
        pass
    def Calculator(self,first,second):
        calculator = Calculator(self,first, second)
        print(f'첫번째수:{calculator.first}')
        print(f'두번째수:{calculator.second}')
        print(f'{calculator.first} + {calculator.second} = {calculator.add()}')
        print(f'{calculator.first} - {calculator.second} = {calculator.minus}')
        print(f'{calculator.first} * {calculator.second} = {calculator.mult()}')
        print(f'{calculator.first} / {calculator.second} = {calculator.divide()}')
