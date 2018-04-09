# coding: UTF-8
import json
import unittest

import requests
from framework import readConfigFile
from framework.logger import Logger

config = readConfigFile.ReadConfig()
mylog = Logger(logger="SearchResultPage").getlog()


class SearchResultPage(unittest.TestCase):


    @classmethod
    def setUp(cls):

        cls.host = config.get_http("baseurl")
        cls.url = cls.host + "/web/basic/appquery"
        cls.data = {
            "appdevice": {
                "userid": "",
                "token": ""
            },
            "params": {
                "text":"",
                "version": "v1.0",
                "size": 20,
                "page": 1,
            }
        }

    def test_SearchWithKeyword(cls):
        """
        药物全量检索
        :return:
        """
        mylog.info("药物列表接口-全量检索，测试开始")
        # 调用requests中的post方法，发送一个接口请求
        r = requests.post(cls.url, data=json.dumps(cls.data))

        # 返回的内容是json格式
        response_data = json.loads(r.text)

        # print(response_data) #一般在degbug测试的时候，需要看看是否接口请求正常
        # 自动化断言

        try:
            cls.assertEqual(response_data['message'],"success","断言失败，两个不相等")
            cls.assertEqual(response_data['businessCode'], "basic", "断言失败，两个不相等")
            cls.assertEqual(response_data['code'],"YD200","断言失败，两个不相等")
            mylog.info("药物列表接口-全量检索，测试完成")
        except AssertionError as e:
            mylog.error("断言出现失败：%s" % e)

    def test_SearchWithoutKeyword(cls):
        """
        药物列表带关键字检索
        :return:
        """
        cls.data = {
            "appdevice": {
                "userid": "",
                "token": ""
            },
            "params": {
                "text": "afatinib",
                "version": "v1.0",
                "size": 20,
                "page": 1,
            }
        }
        mylog.info("药物列表接口-关键字检索，测试开始")
        # 调用requests中的post方法，发送一个接口请求
        r = requests.post(cls.url, data=json.dumps(cls.data))

        # 返回的内容是json格式
        response_data = json.loads(r.text)

        #print(response_data)
        # 自动化断言
        try:
            cls.assertEqual(response_data['message'], "success", "断言失败，两个不相等")
            cls.assertEqual(response_data['businessCode'], "basic", "断言失败，两个不相等")
            cls.assertEqual(response_data['code'], "YD200", "断言失败，两个不相等")
            cls.assertEqual(response_data['data']['pager']['list'][0]['drug_name_cn'], "马来酸阿法替尼", "断言失败，两个不相等")
            mylog.info("药物列表接口-关键字检索，测试完成")

        except AssertionError as e:
            mylog.error("断言出现失败：%s" % e)

