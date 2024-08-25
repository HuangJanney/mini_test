import sys, os
import re

from BeautifulReport import BeautifulReport

cur_path = os.getcwd()
sys.path.append(cur_path[:cur_path.find('mini_test') + len('mini_test')])
import unittest
from page.backpack_page import BackpackPage
import time
from utils.file_util import FileUtil
from ddt import ddt,data






class TestSmoking(unittest.TestCase):
    backpack = BackpackPage()


    # @classmethod
    # def setUpClass(cls):
    #     # cls.page.start_test()
    #     cls.page.start_test_new()
   
    def test_01(self):
        list1 = ['20200001','20200002','20200003','20200004','20200005','20200006','20200007','20200008','20200009','20200010','20200011','20200012','20200013','20200014','20200015','20200016','20200017','20200018','20200019','20200020','20200021','20200022','20200023','20200024','20200025','20200026','20200027','20200028','20200029','20200030','20200031','20200032','20200033','20200034','20200035','20200036','20200037','20200038','20200039','20200040','20200041','20200042','20200043','20200044','20200045','20200046','20200047','20200048','20200049','20200050','20200051','20200052','20200053','20200054','20200055','20200056','20200057','20200058','20200059','20200060','20200061','20200062','20200063','20200064','20200065','20200066','20200067','20200068','20200069','20200070','20200071','20200072','20200073','20200074','20200075','20200076','20200077','20200078','20200079','20200080','20200081','20200082','20200083','20200084','20200085','20200086','20200087','20200088','20200089','20200090','20200091','20200092','20200093','20200094','20200095','20200096','20200097','20200098','20200099','20200100','20200101','20200102','20200103','20200104','20200105','20200106','20200107','20200108','20200109','20200110','20200111','20200112']
        for value in list1:
            aimg = self.backpack.get_snapshot_path('%s_a.png'%value)
            bimg = self.backpack.get_snapshot_path('%s_b.png'%value)
            result = not self.backpack.is_similar(aimg , bimg)
            
            self.backpack.write_to_excel(value, bimg, aimg,result,'对比')
        # self.assertFalse(self.backpack.is_similar(aimg , bimg))
    



if __name__ == '__main__':
    # # unittest.main()
    now = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
    ts = unittest.TestSuite()  # 实例化
    # 按类加载全部testxxx测试用例
    for i in range(1):        
        ts.addTest(unittest.makeSuite(TestSmoking))
    # 按函数加载testxxx测试用例
    # ts.addTest(HtmlReport('test_1'))
    report_name = '对比测试1'
    filename = report_name + now + '.html'
    # 加载执行用例生成报告
    result = BeautifulReport(ts)
    # 定义报告属性
    result.report(description='对比测试1', filename=filename, report_dir=FileUtil.get_report_path())
    # print(FileUtil.get_report_path())
        # 执行测试用例
