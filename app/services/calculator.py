from app.models.calculator import Calculator
class CalculatorService(object):
    def __init__(self) -> None:
        pass
    def caluclator(self, first, second):
        calculator = Calculator(first, second)
        print(f'첫번째수:{calculator.first}')
        print(f'두번째수:{calculator.second}')
        print(f'{calculator.first} + {calculator.second} = {calculator.add()}')
        print(f'{calculator.first} - {calculator.second} = {calculator.minus()}')
        print(f'{calculator.first} * {calculator.second} = {calculator.mult()}')
        print(f'{calculator.first} / {calculator.second} = {calculator.divide()}')