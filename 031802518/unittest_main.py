import unittest
import test_function
class TestAllTexts(unittest.TestCase):
    #@classmethod
    def setUp(self) :
        print("start")
    #@classmethod
    def tearDown(self) :
        print("end.....")
        print("--------------------")

    def test_orig(self):
        print("正在载入orig.txt")
        test_function.main_test('sim_0.8\orig.txt', 'sim_0.8\orig.txt', 'ans.txt')

    def test_orig_add(self):
        print("正在载入orig_0.8_add.txt")
        test_function.main_test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_add.txt', 'ans.txt')

    def test_orig_del(self):
        print("正在载入orig_0.8_del.txt")
        test_function.main_test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_del.txt', 'ans.txt')

    def test_orig_dis_1(self):
        print("正在载入orig_0.8_dis_1.txt")
        test_function.main_test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_1.txt', 'ans.txt')

    def test_orig_dis_3(self):
        print("正在载入orig_0.8_dis_3.txt")
        test_function.main_test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_3.txt', 'ans.txt')

    def test_orig_dis_7(self):
        print("正在载入orig_0.8_dis_7.txt")
        test_function.main_test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_7.txt', 'ans.txt')

    def test_orig_dis_10(self):
        print("正在载入orig_0.8_dis_10.txt")
        test_function.main_test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_10.txt', 'ans.txt')

    def test_orig_dis_15(self):
        print("正在载入orig_0.8_dis_15.txt")
        test_function.main_test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_15.txt', 'ans.txt')

    def test_mix_tfidf(self):
        print("正在载入orig_0.8_mix.txt")
        test_function.main_test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_mix.txt', 'ans.txt')

    def test_orig_rep(self):
        print("正在载入orig_0.8_rep.txt")
        test_function.main_test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_rep.txt', 'ans.txt')

    def test_mydata(self):
        print("mydata\mydata_mix.txt")
        test_function.main_test('mydata\mydata_add.txt', 'mydata\mydata_mix.txt', 'ans.txt')

    #异常检测
    def test_words(self):
        test_function.main_test('sim_0.8\orig.txt', 'NoWord.txt', 'ans.txt')

if __name__=='__main__':
    unittest.main()





