import sys, os
import re

from BeautifulReport import BeautifulReport

cur_path = os.getcwd()
sys.path.append(cur_path[:cur_path.find('mini_test') + len('mini_test')])
import unittest
from page.main_page import MainPage
import time
from utils.file_util import FileUtil


class TestSmoking(unittest.TestCase):
    page = MainPage()


    # @classmethod
    # def setUpClass(cls):
    #     # cls.page.start_test()
    #     cls.page.start_test_new()

    def test_01(self):
        # self.page.step_move((58.2,11.4))
        while True:
            if self.page.exists_recursively_default('interaction','fishing1.png'):
                for i in range(20):
                    self.page.touch_coordinate(0.89,0.77)
                    self.page.sleep(0.1)
                    print("到这了")
            if self.page.exists_recursively_default('main_ui','accept.png'):
                self.page.touch_recursively_default('main_ui','accept.png')
                self.page.sleep(5)
                self.page.touch_coordinate(0.89,0.77)
            if self.page.exists_recursively_default('main_ui','x.png'):
                self.page.touch_coordinate(0.89,0.77)
                self.page.sleep(5)





                
                 
                 
        



if __name__ == '__main__':
    # # unittest.main()
    now = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
    ts = unittest.TestSuite()  # 实例化
    # 按类加载全部testxxx测试用例
    for i in range(1):        
        ts.addTest(unittest.makeSuite(TestSmoking))
    # 按函数加载testxxx测试用例
    # ts.addTest(HtmlReport('test_1'))
    report_name = '创建派对测试'
    filename = report_name + now + '.html'
    # 加载执行用例生成报告
    result = BeautifulReport(ts)
    # 定义报告属性
    result.report(description='创建派对测试', filename=filename, report_dir=FileUtil.get_report_path())
    # print(FileUtil.get_report_path())