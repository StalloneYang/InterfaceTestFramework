# coding:utf-8
import unittest,time
class Test1(unittest.TestCase):
    u'''这里的测试集合的描述'''
    @classmethod
    def setUpClass(cls):
        print("setUpClass初始化操作：用例开始前只执行一次")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass收尾清理操作：用例结束时候只执行一次")

    def setUp(self):
        print("setUp每次用例开始前都会执行！！！")

    def tearDown(self):
        print("tearDown每次用例结构都会执行！！！")

    def test_01(self):
        u'''测试用例1描述：xxx'''
        time.sleep(1)
        print("正在执行用例01")

    def test_02(self):
        u'''测试用例2描述：xxx'''
        time.sleep(1)
        print("正在执行用例02")
if __name__ == "__main__":
    unittest.main()