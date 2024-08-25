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


    @classmethod
    def setUpClass(cls):
        # cls.page.start_test_new()
        pass

    def test_01(self):
        '''登录与创角'''
        self.page.start_test_new()
        pass

    def test_02(self):
        '''新手引导'''
        self.page.rookie_guidance()

    def test_03(self):
        '''制造台放置'''
        self.page.open_backpack()