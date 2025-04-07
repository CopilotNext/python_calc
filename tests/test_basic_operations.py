import unittest
import sys
import os

# 添加项目根目录到系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from operations.basic_operations import (
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation
)

class TestBasicOperations(unittest.TestCase):
    def setUp(self):
        self.add = AddOperation()
        self.subtract = SubtractOperation()
        self.multiply = MultiplyOperation()
        self.divide = DivideOperation()

    def test_add_operation(self):
        # 测试正数加法
        self.assertEqual(self.add.calculate(1, 2), 3)
        # 测试负数加法
        self.assertEqual(self.add.calculate(-1, -2), -3)
        # 测试小数加法
        self.assertAlmostEqual(self.add.calculate(1.1, 2.2), 3.3)
        # 测试零的加法
        self.assertEqual(self.add.calculate(0, 5), 5)

    def test_subtract_operation(self):
        # 测试正数减法
        self.assertEqual(self.subtract.calculate(5, 3), 2)
        # 测试负数减法
        self.assertEqual(self.subtract.calculate(-5, -3), -2)
        # 测试小数减法
        self.assertAlmostEqual(self.subtract.calculate(5.5, 2.2), 3.3)
        # 测试零的减法
        self.assertEqual(self.subtract.calculate(5, 0), 5)

    def test_multiply_operation(self):
        # 测试正数乘法
        self.assertEqual(self.multiply.calculate(2, 3), 6)
        # 测试负数乘法
        self.assertEqual(self.multiply.calculate(-2, 3), -6)
        # 测试小数乘法
        self.assertAlmostEqual(self.multiply.calculate(2.5, 2), 5)
        # 测试零的乘法
        self.assertEqual(self.multiply.calculate(5, 0), 0)

    def test_divide_operation(self):
        # 测试正数除法
        self.assertEqual(self.divide.calculate(6, 2), 3)
        # 测试负数除法
        self.assertEqual(self.divide.calculate(-6, 2), -3)
        # 测试小数除法
        self.assertAlmostEqual(self.divide.calculate(5.5, 2), 2.75)
        # 测试除以1
        self.assertEqual(self.divide.calculate(5, 1), 5)
        
        # 测试除零异常
        with self.assertRaises(ZeroDivisionError):
            self.divide.calculate(5, 0)

if __name__ == '__main__':
    unittest.main()
