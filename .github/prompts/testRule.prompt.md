# Python 单元测试编写指南

## 基本结构
```python
import unittest

class TestYourClass(unittest.TestCase):
    def setUp(self):
        # 在每个测试方法前运行
        self.object = YourClass()

    def tearDown(self):
        # 在每个测试方法后运行
        pass
```

## 测试用例设计原则

### 1. 完整性测试
- 测试所有公共方法
- 测试每个方法的主要功能路径
- 包含所有边界条件

```python
def test_divide(self):
    # 正常情况
    self.assertEqual(self.calc.divide(10, 2), 5)
    
    # 边界值
    self.assertEqual(self.calc.divide(0, 5), 0)
    self.assertEqual(self.calc.divide(-10, 2), -5)
    
    # 异常情况
    with self.assertRaises(ZeroDivisionError):
        self.calc.divide(5, 0)
```

### 2. 边界值测试
针对数值类型：
- 最小值
- 最小值+1
- 正常值
- 最大值-1
- 最大值

```python
def test_array_operation(self):
    # 空数组
    self.assertEqual(self.calc.sum_array([]), 0)
    
    # 单元素数组
    self.assertEqual(self.calc.sum_array([1]), 1)
    
    # 正常数组
    self.assertEqual(self.calc.sum_array([1, 2, 3]), 6)
    
    # 包含负数
    self.assertEqual(self.calc.sum_array([-1, 0, 1]), 0)
```

### 3. 异常测试
```python
def test_error_handling(self):
    # 类型错误
    with self.assertRaises(TypeError):
        self.calc.add("1", 2)
    
    # 值错误
    with self.assertRaises(ValueError):
        self.calc.square_root(-1)
    
    # 自定义异常
    with self.assertRaises(CustomError):
        self.calc.custom_operation()
```

### 4. 精度测试
```python
def test_float_operations(self):
    # 使用assertAlmostEqual进行浮点数比较
    self.assertAlmostEqual(self.calc.divide(1, 3), 0.333333, places=6)
    
    # 或使用delta参数
    self.assertAlmostEqual(self.calc.sin(math.pi/2), 1.0, delta=1e-10)
```

## 最佳实践清单

1. 测试命名
   - 使用描述性名称
   - 遵循`test_[被测试的功能]_[测试场景]`格式

2. 测试隔离
   - 每个测试用例独立
   - 使用setUp和tearDown管理测试状态

3. 断言选择
   - assertEqual: 相等比较
   - assertNotEqual: 不相等比较
   - assertTrue/assertFalse: 布尔值测试
   - assertRaises: 异常测试
   - assertAlmostEqual: 浮点数比较

4. 测试覆盖率
   - 使用coverage工具检查覆盖率
   - 目标达到80%以上的代码覆盖率

## 示例：完整的测试类

```python
import unittest
import math

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        # 基本测试
        self.assertEqual(self.calc.add(1, 1), 2)
        
        # 边界测试
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-1, 1), 0)
        
        # 大数测试
        self.assertEqual(self.calc.add(999999, 1), 1000000)

    def test_string_operations(self):
        # 类型检查
        with self.assertRaises(TypeError):
            self.calc.add("1", 2)
```
