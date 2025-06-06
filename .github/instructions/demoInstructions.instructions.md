---
applyTo: '*.py'
---

# Python应用架构规范

## 1. 项目结构规范

### 1.1 目录结构
```
pythoncaldemo/
├── src/                    # 源代码目录
│   ├── __init__.py
│   ├── main.py            # 应用入口点
│   ├── config/            # 配置模块
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── models/            # 数据模型
│   │   ├── __init__.py
│   │   └── *.py
│   ├── services/          # 业务逻辑层
│   │   ├── __init__.py
│   │   └── *.py
│   ├── repositories/      # 数据访问层
│   │   ├── __init__.py
│   │   └── *.py
│   ├── controllers/       # 控制器层
│   │   ├── __init__.py
│   │   └── *.py
│   ├── utils/            # 工具函数
│   │   ├── __init__.py
│   │   └── *.py
│   └── exceptions/       # 自定义异常
│       ├── __init__.py
│       └── *.py
├── tests/                # 测试目录
├── docs/                 # 文档目录
├── requirements.txt      # 依赖管理
├── pyproject.toml       # 项目配置
└── README.md
```

## 2. 编码标准

### 2.1 PEP 8 合规性
- 严格遵循 PEP 8 代码风格指南
- 使用 black 进行代码格式化
- 使用 flake8 进行代码检查
- 行长度限制为 88 字符

### 2.2 命名约定
- **模块名**: 小写字母，下划线分隔 (snake_case)
- **类名**: 大驼峰命名 (PascalCase)
- **函数名**: 小写字母，下划线分隔 (snake_case)
- **变量名**: 小写字母，下划线分隔 (snake_case)
- **常量名**: 大写字母，下划线分隔 (UPPER_CASE)
- **私有成员**: 以单下划线开头 (_private)

### 2.3 类型注解
- 所有函数必须包含类型注解
- 使用 typing 模块进行复杂类型定义
- 支持向后兼容的类型注解格式

```python
from typing import List, Dict, Optional, Union
from dataclasses import dataclass

def process_data(items: List[str], config: Dict[str, Any]) -> Optional[str]:
    """处理数据并返回结果"""
    pass
```

## 3. 架构模式

### 3.1 分层架构
采用经典的三层架构模式：
- **表示层 (Controllers)**: 处理用户输入和输出
- **业务逻辑层 (Services)**: 实现核心业务逻辑
- **数据访问层 (Repositories)**: 处理数据持久化

### 3.2 依赖注入
- 使用依赖注入容器管理对象生命周期
- 避免硬编码依赖关系
- 支持接口抽象和实现分离

### 3.3 设计模式应用
- **工厂模式**: 用于对象创建
- **单例模式**: 用于配置管理和资源共享
- **观察者模式**: 用于事件处理
- **策略模式**: 用于算法选择

## 4. 错误处理规范

### 4.1 异常层次结构
```python
class AppBaseException(Exception):
    """应用基础异常类"""
    def __init__(self, message: str, error_code: str = None):
        super().__init__(message)
        self.error_code = error_code

class ValidationError(AppBaseException):
    """数据验证异常"""
    pass

class BusinessLogicError(AppBaseException):
    """业务逻辑异常"""
    pass
```

### 4.2 错误处理原则
- 使用具体的异常类型而非通用Exception
- 在适当的层级捕获和处理异常
- 记录详细的错误信息用于调试
- 向用户返回友好的错误消息

## 5. 日志记录规范

### 5.1 日志配置
```python
import logging
from logging.handlers import RotatingFileHandler

# 配置结构化日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('app.log', maxBytes=10485760, backupCount=5),
        logging.StreamHandler()
    ]
)
```

### 5.2 日志级别使用
- **DEBUG**: 详细的调试信息
- **INFO**: 一般信息记录
- **WARNING**: 警告信息
- **ERROR**: 错误信息
- **CRITICAL**: 严重错误

## 6. 数据库操作规范

### 6.1 ORM使用
- 优先使用 SQLAlchemy 或类似ORM框架
- 定义清晰的模型关系
- 使用数据库迁移管理schema变更

### 6.2 查询优化
- 避免N+1查询问题
- 使用适当的索引
- 实现查询缓存机制
- 使用数据库连接池

## 7. 测试规范

### 7.1 测试类型
- **单元测试**: 测试单个函数或方法
- **集成测试**: 测试模块间交互
- **端到端测试**: 测试完整业务流程

### 7.2 测试覆盖率
- 代码覆盖率要求达到80%以上
- 关键业务逻辑覆盖率要求90%以上
- 使用pytest作为测试框架

### 7.3 测试最佳实践
```python
import pytest
from unittest.mock import Mock, patch

class TestUserService:
    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.user_service = UserService()
    
    def test_create_user_success(self):
        """测试用户创建成功场景"""
        # Given
        user_data = {"name": "John", "email": "john@example.com"}
        
        # When
        result = self.user_service.create_user(user_data)
        
        # Then
        assert result.id is not None
        assert result.name == "John"
```

## 8. 性能优化规范

### 8.1 代码优化
- 使用生成器处理大数据集
- 避免过早优化
- 使用性能分析工具识别瓶颈
- 实现适当的缓存策略

### 8.2 内存管理
- 及时释放不需要的对象引用
- 使用上下文管理器管理资源
- 避免内存泄漏

## 9. 安全规范

### 9.1 输入验证
- 对所有用户输入进行验证
- 使用参数化查询防止SQL注入
- 实现适当的身份验证和授权

### 9.2 敏感数据处理
- 加密敏感数据
- 不在日志中记录敏感信息
- 使用环境变量管理配置

## 10. 文档规范

### 10.1 代码文档
```python
def calculate_total(items: List[Item], tax_rate: float) -> Decimal:
    """
    计算订单总金额包含税费
    
    Args:
        items: 订单项目列表
        tax_rate: 税率 (0.0 到 1.0 之间)
    
    Returns:
        包含税费的总金额
        
    Raises:
        ValueError: 当税率超出有效范围时
        
    Example:
        >>> items = [Item(price=10.0), Item(price=20.0)]
        >>> calculate_total(items, 0.1)
        Decimal('33.0')
    """
    pass
```

### 10.2 API文档
- 使用 FastAPI 自动生成API文档
- 提供清晰的请求/响应示例
- 包含错误代码说明

## 11. 部署和配置

### 11.1 环境配置
- 使用环境变量管理不同环境配置
- 实现配置验证机制
- 支持热重载配置

### 11.2 容器化
- 使用Docker进行应用容器化
- 优化Docker镜像大小
- 实现多阶段构建

这些规范将确保代码质量、可维护性和团队协作效率。所有Python代码都应遵循这些标准。