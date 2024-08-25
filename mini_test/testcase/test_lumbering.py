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
        for i in range(50):
            try:
                self.page.start_test()
                self.page.step_move((67.6,32.6))
                self.page.open_backpack()
                self.page.find_and_touch_element('tools','iron_axe.png')
                self.page.touch_recursively_default('main_ui','back.png')
                if self.page.exists_recursively_default('tools','apple_tree.png'):
                    self.page.touch_coordinate(0.89,0.77)
                    self.page.sleep(1.0)
                    if not self.page.exists_recursively_default('main_ui','backpack_text.png'):
                        print("程序异常")
                        url ='https://open.feishu.cn/open-apis/bot/v2/hook/f141b2da-847e-469e-9aaa-d9aabf3ee147'
                        self.page.send_message(url,'触发崩溃了')
                    self.page.gm_cmd('tree_growth')
                    if i%3 == 0:
                        self.page.gm_cmd('clean_all_refresh')
                        self.page.gm_cmd('kick')
                self.page.stop_game_now()
                self.page.sleep(2)
            except:
                print("遇到错误")
                if not self.page.exists_recursively_default('tools','apple_tree.png'):
                    self.page.gm_cmd('kick')
                    self.page.stop_game_now()


        



                
                 
                 
        



if __name__ == '__main__':
    # # unittest.main()
    now = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
    ts = unittest.TestSuite()  # 实例化
    # 按类加载全部testxxx测试用例
    for i in range(1):        
        ts.addTest(unittest.makeSuite(TestSmoking))
    # 按函数加载testxxx测试用例
    # ts.addTest(HtmlReport('test_1'))
    report_name = '砍树测试'
    filename = report_name + now + '.html'
    # 加载执行用例生成报告
    result = BeautifulReport(ts)
    # 定义报告属性
    result.report(description='砍树测试', filename=filename, report_dir=FileUtil.get_report_path())
    # print(FileUtil.get_report_path())