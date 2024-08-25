import sys, os

from BeautifulReport import BeautifulReport
import unittest
import time
from utils.file_util import FileUtil
from testcase.test_hall import TestCase

now = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
ts = unittest.TestSuite()  # 实例化
# 按类加载全部testxxx测试用例,需要执行多个测试用例在此处修改就行（添加）
ts.addTest(unittest.makeSuite(TestCase))
# 按函数加载testxxx测试用例
# ts.addTest(HtmlReport('test_1'))
#定义测试的名称
report_name = '大厅UI遍历测试'
#定义报告的名称
filename = report_name + now + '.html'
# 加载执行用例生成报告
result = BeautifulReport(ts)
# 定义报告属性
result.report(description='大厅遍历报告', filename=filename, report_dir=FileUtil.get_report_path())