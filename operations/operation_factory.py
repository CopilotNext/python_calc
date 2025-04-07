from .basic_operations import AddOperation, SubtractOperation, MultiplyOperation, DivideOperation

class OperationFactory:
    @staticmethod
    def create_operation(operator: str):
        operations = {
            '+': AddOperation(),
            '-': SubtractOperation(),
            '*': MultiplyOperation(),
            '/': DivideOperation()
        }
        return operations.get(operator)
