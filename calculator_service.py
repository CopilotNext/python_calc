from operations.operation_factory import OperationFactory
import re

class CalculatorService:
    def __init__(self):
        self.operation_factory = OperationFactory()

    def calculate(self, expression: str) -> str:
        try:
            if not expression:
                return "0"
            
            if not any(c.isdigit() for c in expression):
                return "错误: 无效输入"

            # 解析表达式
            # 支持形如 "123+456" 的简单表达式
            match = re.match(r'^([-]?\d*\.?\d+)([\+\-\*\/])([-]?\d*\.?\d+)$', expression)
            if not match:
                return "错误: 格式无效"

            x = float(match.group(1))
            operator = match.group(2)
            y = float(match.group(3))

            # 获取对应的运算类
            operation = self.operation_factory.create_operation(operator)
            if not operation:
                return "错误: 无效运算符"

            # 执行计算
            result = operation.calculate(x, y)

            # 格式化结果
            if isinstance(result, float) and result.is_integer():
                return str(int(result))
            return str(result)

        except ZeroDivisionError:
            return "错误: 除数不能为0"
        except:
            return "错误: 无效计算"
