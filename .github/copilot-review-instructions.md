# 代码审查指南

## 审查范围

对代码进行全面的审查和评估，包括以下方面：

### 1. 代码质量

- 代码是否清晰易读
- 命名规范是否合适
- 代码结构是否合理
- 是否遵循 PEP 8 规范

### 2. 功能性

- 代码是否实现了预期功能
- 是否存在潜在的 bug
- 边界条件是否考虑完善
- 错误处理是否充分

### 3. 性能

- 是否存在性能优化空间
- 是否有资源使用效率问题
- 是否存在潜在的性能瓶颈

### 4. 安全性

- 是否存在安全漏洞
- 敏感数据处理是否安全
- 输入验证是否充分

### 5. 可维护性

- 代码注释是否充分
- 是否有重复代码
- 模块化程度是否合适
- 是否便于测试

### 6. 建议改进

- 具体的改进建议
- 代码优化方案
- 最佳实践建议

## 注意事项

审查人员应该针对每个方面提供详细的分析和具体的改进建议，确保反馈的实用性和可操作性。

## Python 代码示例

以下是一些 Python 优秀代码示例，展示了良好的编程实践：

### 函数定义示例

```python
def calculate_average(numbers: list[float]) -> float:
    """计算数字列表的平均值
    
    Args:
        numbers: 需要计算平均值的数字列表
        
    Returns:
        float: 计算得到的平均值
        
    Raises:
        ValueError: 当输入列表为空时抛出
    """
    if not numbers:
        raise ValueError("输入列表不能为空")
    return sum(numbers) / len(numbers)
```

### 类定义示例

```python
from typing import Optional
from datetime import datetime

class User:
    """用户类，展示了良好的类设计实践"""
    
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self._email = email  # 使用下划线表示保护属性
        self._created_at: datetime = datetime.now()
        
    @property
    def email(self) -> str:
        """电子邮件地址的getter方法"""
        return self._email
    
    @email.setter
    def email(self, value: str) -> None:
        """电子邮件地址的setter方法，包含验证"""
        if '@' not in value:
            raise ValueError("无效的邮件地址")
        self._email = value
        
    def get_user_info(self) -> dict:
        """返回用户信息字典"""
        return {
            "username": self.username,
            "email": self._email,
            "created_at": self._created_at
        }
```

### 错误处理示例

```python
def read_config(filepath: str) -> dict:
    """读取配置文件的示例，展示了良好的错误处理实践
    
    Args:
        filepath: 配置文件路径
        
    Returns:
        dict: 配置信息字典
        
    Raises:
        FileNotFoundError: 当文件不存在时抛出
        json.JSONDecodeError: 当JSON格式无效时抛出
    """
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"配置文件不存在: {filepath}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"配置文件格式错误: {e}")
        raise
```

## 最佳实践要点

- 使用类型注解提高代码可读性
- 编写清晰的文档字符串
- 适当的错误处理和日志记录
- 使用有意义的变量和函数名称
- 遵循 PEP 8 编码规范
- 合理使用面向对象特性
