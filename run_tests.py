import unittest
import sys
import os
import time
from unittest.runner import TextTestRunner
from unittest.loader import TestLoader
from datetime import datetime

class CustomTestRunner(TextTestRunner):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_time = None
        self.end_time = None

    def run(self, test):
        self.start_time = time.time()
        result = super().run(test)
        self.end_time = time.time()
        return result

    def generate_report(self, result):
        duration = self.end_time - self.start_time
        report = [
            "\n=== 测试报告 ===",
            f"开始时间: {datetime.fromtimestamp(self.start_time).strftime('%Y-%m-%d %H:%M:%S')}",
            f"结束时间: {datetime.fromtimestamp(self.end_time).strftime('%Y-%m-%d %H:%M:%S')}",
            f"执行时间: {duration:.2f} 秒",
            f"总用例数: {result.testsRun}",
            f"成功用例: {result.testsRun - len(result.failures) - len(result.errors)}",
            f"失败用例: {len(result.failures)}",
            f"错误用例: {len(result.errors)}",
            "\n=== 详细信息 ===",
        ]

        if result.failures:
            report.append("\n失败的测试用例:")
            for failure in result.failures:
                report.append(f"- {failure[0]}")
                report.append(f"  原因: {failure[1]}")

        if result.errors:
            report.append("\n错误的测试用例:")
            for error in result.errors:
                report.append(f"- {error[0]}")
                report.append(f"  原因: {error[1]}")

        return "\n".join(report)

def run_tests():
    # 设置测试目录路径
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    
    # 创建测试加载器
    loader = TestLoader()
    
    # 发现并加载测试用例
    suite = loader.discover(test_dir, pattern='test_*.py')
    
    # 创建自定义测试运行器
    runner = CustomTestRunner(verbosity=2)
    
    # 运行测试
    result = runner.run(suite)
    
    # 生成报告
    report = runner.generate_report(result)
    
    # 打印报告
    print(report)
    
    # 将报告保存到文件
    report_path = os.path.join(os.path.dirname(__file__), 'test_report.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n测试报告已保存到: {report_path}")
    
    # 返回测试是否全部通过
    return result.wasSuccessful()

if __name__ == '__main__':
    sys.exit(not run_tests())
