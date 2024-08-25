import sys, os

from BeautifulReport import BeautifulReport

cur_path = os.getcwd()
sys.path.append(cur_path[:cur_path.find('mini_test') + len('mini_test')])
import unittest
from page.main_page import MainPage
import time
from utils.file_util import FileUtil


class TestCase(unittest.TestCase):
    page = MainPage()


    @classmethod
    def setUpClass(cls):
        cls.page.start_test()


    def test_01(self):
        '''大厅界面各入口UI完整检查'''
        self.page.sleep(5)
        self.assertTrue(self.page.poco(text="背包").exists())#背包
        self.assertTrue(self.page.poco(text="手机").exists())#手机
        self.assertTrue(self.page.poco(text="免费奖励").exists())#免费奖励
        self.assertTrue(self.page.poco(text="活动商城").exists())#活动商城


    def test_02(self):
        '''好友入口点击检查'''
        self.page.friend()
        self.page.sleep()
        self.assertTrue(self.page.poco(text="迷你好友").exists())
        self.page.close_friend()
        self.page.sleep()

    def test_03(self):
        '''商店入口点击检查'''
        self.page.shop()
        self.page.sleep()
        self.assertTrue(self.page.poco(text="推薦").exists())
        self.page.close_shop()
        self.page.sleep()

    def test_04(self):
        '''设置入口点击检查'''
        self.page.setting_hall()
        self.page.sleep()
        self.assertTrue(self.page.poco(text="繼續遊戲").exists())
        self.page.poco(text="繼續遊戲").click()
        self.page.sleep()

    def test_05(self):
        '''邮件入口点击检查'''
        self.page.mail_icon()
        self.page.sleep()
        self.assertTrue(self.page.poco(text="官方郵件").exists())
        self.page.close_mail()
        self.page.sleep()

    def test_06(self):
        '''活动入口点击检查'''
        self.page.activity()
        self.page.sleep()
        self.assertTrue(self.page.poco(text="活動").exists())
        self.page.close_activity()
        self.page.sleep()

    def test_07(self):
        '''个人中心入口点击检查'''
        self.page.personal_center()
        self.page.sleep()
        self.assertTrue(self.page.poco(text="迷你show").exists())
        self.page.close_personal_center()
        self.page.sleep()

    def test_08(self):
        '''存档入口点击检查'''
        self.page.local_map()
        self.page.sleep()
        self.assertTrue(self.page.poco(text="創建新世界").exists())
        self.page.close_local_map()
        self.page.sleep()

    def test_09(self):
        '''联机大厅入口点击检查'''
        self.page.multi_player()
        self.page.sleep()
        self.assertTrue(self.page.poco(text="房間").exists())
        self.page.close_room()
        self.page.sleep()

    def test_10(self):
        '''更多游戏（地图工坊）入口点击检查'''
        self.page.mini_works()
        self.page.sleep()
        self.assertTrue(self.page.poco(text="材質").exists())
        self.page.close_mini_works()
        self.page.sleep()

    def test_11(self):
        '''资源工坊入口点击检查'''
        self.page.resource_shop()
        self.page.sleep()
        self.assertTrue(self.page.poco(text="資源中心").exists())
        self.page.close_res_shop()
        self.page.sleep()

    def test_12(self):
        '''我的家园入口点击检查'''
        self.page.home_chest()
        self.page.sleep(5)
        self.assertTrue(self.page.poco(text="編輯家園").exists())
        self.page.setting_home()
        self.page.exit_home()
        self.page.sleep()

    def test_13(self):
        '''家园果实入口点击检查'''
        self.page.home_fruit()
        self.page.sleep(2)
        self.assertTrue(self.page.poco(text="圖鑒").exists())
        self.page.close_home_fruit()
        self.page.sleep()

    def tearDown(self):
        self.page.back_hall()

    @classmethod
    def tearDownClass(cls):
        cls.page.stop_game('com.playmini.miniworld')



if __name__ == '__main__':
    # # unittest.main()
    now = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
    ts = unittest.TestSuite()  # 实例化
    # 按类加载全部testxxx测试用例
    ts.addTest(unittest.makeSuite(TestCase))
    # 按函数加载testxxx测试用例
    # ts.addTest(HtmlReport('test_1'))
    report_name = '大厅UI遍历测试'
    filename = report_name + now + '.html'
    # 加载执行用例生成报告
    result = BeautifulReport(ts)
    # 定义报告属性
    result.report(description='大厅遍历报告', filename=filename, report_dir=FileUtil.get_report_path())
    # print(FileUtil.get_report_path())