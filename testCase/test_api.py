# coding:utf-8
import json
import ssl
import unittest
import ddt
import os
import requests
import urllib3

from framework import base_api
from framework import readExcel
from framework import writeexcel

urllib3.disable_warnings()

# 获取demo_api.xlsx路径
curpath = os.path.dirname(os.path.realpath(__file__))
testxlsx = os.path.join(curpath, "TestCase.xlsx")

# 复制demo_api.xlsx文件到report下
report_path = os.path.join(os.path.dirname(curpath), "testReports")
reportxlsx = os.path.join(report_path, "result.xlsx")

testdata = readExcel.ExcelUtil(testxlsx).dict_data()
print(testdata)  # 获取Excel的数据

@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        # 如果有登录的话，就在这里先登录了

        context = ssl._create_unverified_context()
        cls.s = requests.session()
        url = "https://dsylogin.10333.com/dotoyo/login"

        body = {
            "username": "13711111111",
            "password": "88888888",
            "service": "http://dsyjg.10333.com/api/ent/index"
        }
        # r1 = s.post(url,data=body,verify=False)
        r1 = requests.post(url, data=body, verify=False)
        print(r1.text)

        uri = json.loads(r1.text)
        url_login = "https://dsyjg.10333.com/api/ent/index?ticket=" + uri['st'] + "&sysType=1"
        # 模拟登录系统，获取cookie
        resp = requests.get(url=url_login, verify=False)
        cookie_jar = resp.request._cookies
        cookie = requests.utils.dict_from_cookiejar(cookie_jar)  # Cookiejar类型转化为字典
        print(cookie)
        USERID_SID = cookie['USERID_SID']
        print(USERID_SID)

        addCookies = requests.cookies.RequestsCookieJar()
        addCookies.set("USERID_SID", USERID_SID)  # 从传入登录的cookies
        print(type(addCookies))
        # addCookies.set("USERID_SID", "cd24db7a-ba63-45d1-b733-355f1ce94e25")   # 从fiddler4中抓过来的
        cls.s.cookies.update(addCookies)  # 更新cookies

        writeexcel.copy_excel(testxlsx, reportxlsx)  # 先复制excel数据到report



    @ddt.data(*testdata)
    def test_api(self, data):
        """测试日记日志接口"""
        # 接口返回结果
        res = base_api.send_requests(self.s, data)

        # 把接口的返回结果写入reportExcel
        base_api.wirte_result(res, filename=reportxlsx)

        # 检查点 checkpoint
        check = data["Check_field"]
        print("检查点->：%s"%check)
        response = res["response"]
        print("返回实际结果->：%s"%response)
        # 断言
        self.assertTrue(response.find(check))

if __name__ == "__main__":
    unittest.main()
