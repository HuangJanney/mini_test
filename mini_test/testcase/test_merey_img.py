import sys, os
cur_path = os.getcwd()
sys.path.append(cur_path[:cur_path.find('mini_test') + len('mini_test')])
import unittest
from utils.image_util import ImageUtil

class TestSmoking(unittest.TestCase):
    image = ImageUtil()

    def test_01(self):
        org = "D:\\MyFileTools\\test_files\\My_repositories\\mini_test\\assets\\img\\Main_icon_25.png"
        back = "D:\\MyFileTools\\test_files\\My_repositories\\mini_test\\assets\img\\main_frame_03.png"
        save_path = "D:\\MyFileTools\\test_files\\My_repositories\\mini_test\\assets\\img\\fish.png"
        self.image.merge_images(org,back,save_path)    


if __name__ == '__main__':
    unittest.main()