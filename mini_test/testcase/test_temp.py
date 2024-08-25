import sys, os

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
        '''传送及派对创建&关闭'''
        #传送至家园
        wait_time = 10
        self.page.sleep(wait_time)
        self.page.move_around()
        self.page.wake_phone()
        self.page.home_tp()
        self.page.sleep(wait_time)
        self.page.move_around()
        self.page.enter_by_gm('inroom')
        self.page.sleep(wait_time)
        self.page.wake_phone()
        self.page.world_tp()
        self.page.sleep(wait_time)
        self.page.move_around()
        for i in range(6):
            self.page.wake_phone()
            self.page.patry_mian()
            self.page.create_party(i)
            self.page.sleep(wait_time)
            self.page.move_around()
            self.page.close_party()
            self.page.sleep(wait_time)
            self.page.move_around()
        command_list = ['goto_hair_salon','goto_shop','goto_camp','goto_cloth']
        for command in command_list:
            self.page.enter_by_gm(command)
            self.page.sleep(wait_time)
            self.page.wake_phone()
            self.page.home_tp()
            self.page.sleep(wait_time)
            self.page.move_around()
            self.page.wake_phone()
            self.page.world_tp()
            self.page.sleep(wait_time)
            self.page.move_around()



    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.page.stop_game_now()


    # def test_01(self):
    # #     for i in range(50):
    # #         self.page.start_test()
    # #         self.page.sleep(5)
    # #         self.page.stop_game_now()
    #     self.page.rookie_guidance()



if __name__ == '__main__':
    # # unittest.main()
    now = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
    ts = unittest.TestSuite()  # 实例化
    # 按类加载全部testxxx测试用例
    for i in range(1):        
        ts.addTest(unittest.makeSuite(TestSmoking))
    # 按函数加载testxxx测试用例
    # ts.addTest(HtmlReport('test_1'))
    report_name = '压力测试'
    filename = report_name + now + '.html'
    # 加载执行用例生成报告
    result = BeautifulReport(ts)
    # 定义报告属性
    result.report(description='压力测试', filename=filename, report_dir=FileUtil.get_report_path())
    # print(FileUtil.get_report_path())