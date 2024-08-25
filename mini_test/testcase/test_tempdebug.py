import sys, os
import re

from BeautifulReport import BeautifulReport

cur_path = os.getcwd()
sys.path.append(cur_path[:cur_path.find('mini_test') + len('mini_test')])
import unittest
from page.home_page import HomePage
import time
from utils.file_util import FileUtil
from utils.config_util import ConfigUtil
from ddt import ddt,data
from utils.image_util import ImageUtil

class TestSmoking(unittest.TestCase):
    # backpack = BackpackPage()
    # image = ImageUtil()
    homepage = HomePage()
    


    # @classmethod
    # def setUpClass(cls):
    #     # cls.page.start_test()
    #     cls.page.start_test_new()
    def test_01(self):
        # print(self.backpack.is_crash())
        # self.backpack.stop_game_now()
        # org = "D:\\MyFileTools\\test_files\\My_repositories\\mini_test\\assets\\img\\house_icon_fabricate.png"
        # back = "D:\\MyFileTools\\test_files\\My_repositories\\mini_test\\assets\img\\chat_frame_03n.png"
        # save_path = "D:\\MyFileTools\\test_files\\My_repositories\\mini_test\\assets\\img\\use.png"
        # self.image.merge_images(org,back,save_path)    
        # self.backpack.open_craft_station()
        print(self.homepage.poco(text="背包").exists())


if __name__ == '__main__':
    unittest.main()
    # now = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
    # ts = unittest.TestSuite()  # 实例化
    # # 按类加载全部testxxx测试用例
    # for i in range(1):        
    #     ts.addTest(unittest.makeSuite(TestSmoking))
    # # 按函数加载testxxx测试用例
    # # ts.addTest(HtmlReport('test_1'))
    # report_name = '对比测试1'
    # filename = report_name + now + '.html'
    # # 加载执行用例生成报告
    # result = BeautifulReport(ts)
    # # 定义报告属性
    # # result.report(description='对比测试1', filename=filename, report_dir=FileUtil.get_report_path())
    # # print(FileUtil.get_report_path())