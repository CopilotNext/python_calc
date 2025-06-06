# Python 单元测试编写规范 - 基准提示词

## 1. 文件结构与导入规范

### 1.1 标准导入顺序
```python
import unittest
import sys
import os
import math  # 或其他标准库

# 添加项目路径（如需要）
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 导入被测试的模块
from module_name import ClassName, function_name
```

### 1.2 测试类命名
- 格式：`Test + 被测试类名`
- 示例：`TestBasicOperations`, `TestCalculatorService`

## 2. 测试方法设计原则

### 2.1 测试方法命名规范
```
test_[被测试功能]_[测试场景]
```

**示例：**
- `test_add_operation_normal_cases` - 加法运算正常情况
- `test_divide_operation_zero_division_error` - 除法运算除零异常
- `test_square_root_operation_boundary_values` - 平方根运算边界值

### 2.2 测试分类体系

#### A. 正常功能测试 (Normal Cases)
```python
def test_[function]_normal_cases(self):
    """测试[功能]的正常情况"""
    # 基本正数测试
    self.assertEqual(self.obj.method(positive_args), expected_result)
    
    # 负数测试
    self.assertEqual(self.obj.method(negative_args), expected_result)
    
    # 混合数值测试
    self.assertEqual(self.obj.method(mixed_args), expected_result)
    
    # 小数测试（使用assertAlmostEqual）
    self.assertAlmostEqual(self.obj.method(float_args), expected_result, places=10)
```

#### B. 边界值测试 (Boundary Values)
```python
def test_[function]_boundary_values(self):
    """测试[功能]的边界值"""
    # 零值测试
    self.assertEqual(self.obj.method(0, 0), expected)
    
    # 最小值测试
    self.assertEqual(self.obj.method(min_val), expected)
    
    # 最大值测试
    self.assertEqual(self.obj.method(max_val), expected)
    
    # 极值组合测试
    self.assertEqual(self.obj.method(extreme_combo), expected)
```

#### C. 异常测试 (Error Cases)
```python
def test_[function]_[error_type]_errors(self):
    """测试[功能]的[错误类型]异常"""
    # 类型错误
    with self.assertRaises(TypeError):
        self.obj.method(wrong_type_arg)
    
    # 值错误（带消息验证）
    with self.assertRaises(ValueError) as context:
        self.obj.method(invalid_value)
    self.assertIn("预期错误消息", str(context.exception))
    
    # 自定义异常
    with self.assertRaises(CustomError):
        self.obj.method(trigger_custom_error)
```

## 3. 具体测试场景清单

### 3.1 数值运算测试必覆盖场景

#### 加法运算测试
- [ ] 正数 + 正数
- [ ] 负数 + 负数  
- [ ] 正数 + 负数
- [ ] 零值测试（0+0, 0+n, n+0）
- [ ] 大数测试
- [ ] 浮点数精度测试
- [ ] 类型错误测试

#### 减法运算测试
- [ ] 基本减法
- [ ] 负数减法
- [ ] 相同数相减
- [ ] 零值测试
- [ ] 类型错误测试

#### 乘法运算测试
- [ ] 基本乘法
- [ ] 负数乘法
- [ ] 零乘法
- [ ] 一的乘法
- [ ] 大数乘法
- [ ] 类型错误测试

#### 除法运算测试
- [ ] 基本除法
- [ ] 负数除法
- [ ] 零被除
- [ ] 除以1和-1
- [ ] **除零异常测试**（必须）
- [ ] 类型错误测试

#### 幂运算测试
- [ ] 基本幂运算
- [ ] 零的幂、任何数的0次幂、1次幂
- [ ] 负指数测试
- [ ] 分数指数测试
- [ ] 类型错误测试

#### 平方根运算测试
- [ ] 完全平方数
- [ ] 非完全平方数
- [ ] 零和一的平方根
- [ ] **负数异常测试**（必须）
- [ ] 类型错误测试

### 3.2 通用测试场景

#### 精度测试
```python
def test_floating_point_precision(self):
    """测试浮点数精度相关的计算"""
    result = self.obj.calculate(0.1, 0.2)
    self.assertAlmostEqual(result, 0.3, places=10)
```

#### 大数测试
```python
def test_large_numbers(self):
    """测试大数运算"""
    large_num = 1e10
    result = self.obj.calculate(large_num, large_num)
    self.assertAlmostEqual(result, expected, places=5)
```

#### 性能边界测试
```python
def test_edge_case_combinations(self):
    """测试边界情况组合"""
    tiny_num = 1e-15
    result = self.obj.calculate(tiny_num, tiny_num)
    self.assertAlmostEqual(result, expected, places=20)
```

## 4. 断言方法选择指南

### 4.1 精确比较
```python
self.assertEqual(actual, expected)          # 精确相等
self.assertNotEqual(actual, unexpected)     # 不相等
self.assertTrue(condition)                  # 布尔值True
self.assertFalse(condition)                 # 布尔值False
```

### 4.2 浮点数比较
```python
self.assertAlmostEqual(actual, expected, places=10)     # 指定小数位数
self.assertAlmostEqual(actual, expected, delta=1e-10)   # 指定误差范围
```

### 4.3 异常测试
```python
# 简单异常检查
with self.assertRaises(ExceptionType):
    risky_operation()

# 带消息验证的异常检查
with self.assertRaises(ExceptionType) as context:
    risky_operation()
self.assertIn("期望的错误消息", str(context.exception))
```

## 5. 测试组织最佳实践

### 5.1 setUp和tearDown
```python
def setUp(self):
    """在每个测试方法前运行 - 准备测试环境"""
    self.obj = TestClass()
    self.test_data = prepare_test_data()

def tearDown(self):
    """在每个测试方法后运行 - 清理测试环境"""
    cleanup_resources()
```

### 5.2 测试注释规范
```python
def test_function_scenario(self):
    """测试功能的具体场景
    
    详细描述测试的目的、输入、预期输出
    """
    # 准备测试数据
    input_data = prepare_data()
    
    # 执行测试
    result = self.obj.method(input_data)
    
    # 验证结果
    self.assertEqual(result, expected_result)
```

## 6. 测试覆盖率要求

### 6.1 代码覆盖率指标
- **目标覆盖率：≥80%**
- **核心功能覆盖率：≥95%**
- **异常处理覆盖率：100%**

### 6.2 测试维度覆盖
- [ ] 所有公共方法
- [ ] 所有边界条件
- [ ] 所有异常路径
- [ ] 所有数据类型
- [ ] 所有错误状态

## 7. 质量检查清单

### 7.1 测试完整性检查
- [ ] 每个功能至少3个测试方法（正常、边界、异常）
- [ ] 所有异常都有对应的测试
- [ ] 浮点数运算使用appropriate精度比较
- [ ] 测试方法命名清晰描述性强

### 7.2 代码质量检查
- [ ] 测试独立性（测试间无依赖）
- [ ] 测试可重复性（多次运行结果一致）
- [ ] 测试可读性（清晰的注释和结构）
- [ ] 测试maintainability（易于维护和扩展）

## 8. 示例模板

```python
import unittest
import sys
import os

# 项目路径设置
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from module_name import ClassName

class TestClassName(unittest.TestCase):
    def setUp(self):
        self.obj = ClassName()

    def tearDown(self):
        pass

    # ===== 功能A测试 =====
    def test_function_a_normal_cases(self):
        """测试功能A的正常情况"""
        pass

    def test_function_a_boundary_values(self):
        """测试功能A的边界值"""
        pass

    def test_function_a_type_errors(self):
        """测试功能A的类型错误"""
        pass

    # ===== 功能B测试 =====
    def test_function_b_normal_cases(self):
        """测试功能B的正常情况"""
        pass

    def test_function_b_value_errors(self):
        """测试功能B的值错误"""
        pass

if __name__ == '__main__':
    unittest.main()
```

## 9. 执行和报告

### 9.1 测试执行命令
```bash
# 运行单个测试文件
python -m unittest test_module.py

# 运行所有测试
python -m unittest discover tests/

# 生成覆盖率报告
coverage run -m unittest discover tests/
coverage report
coverage html
```

### 9.2 持续集成要求
- 所有测试必须通过
- 覆盖率达到要求
- 无Linting错误
- 性能测试通过

---

**使用说明：**
此规范作为Python单元测试编写的基准提示词，确保测试的完整性、可靠性和可维护性。在编写任何单元测试时，请参照此规范进行设计和实现。
