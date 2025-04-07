from .operation import Operation

class AddOperation(Operation):
    def calculate(self, x: float, y: float) -> float:
        return x + y

class SubtractOperation(Operation):
    def calculate(self, x: float, y: float) -> float:
        return x - y

class MultiplyOperation(Operation):
    def calculate(self, x: float, y: float) -> float:
        return x * y

class DivideOperation(Operation):
    def calculate(self, x: float, y: float) -> float:
        if y == 0:
            raise ZeroDivisionError("除数不能为0")
        return x / y
