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
        '''各派对创建测试'''
        wait_time = 5
        for i in range(6):
            self.page.wake_phone()
            self.page.patry_mian()
            self.page.create_party(i)
            self.page.sleep(wait_time)
            self.page.move_around()
            self.page.close_party()
            self.page.sleep(wait_time)
            self.page.move_around()

                
                 
                 
        



if __name__ == '__main__':
    # # unittest.main()
    now = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
    ts = unittest.TestSuite()  # 实例化
    # 按类加载全部testxxx测试用例    
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