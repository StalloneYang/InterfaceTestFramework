#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import codecs
import configparser

# configPath = os.path.abspath(os.curdir) + '/testConfig/config.ini'
# configPath = os.path.dirname(os.path.abspath('.')) + '/testConfig/config.ini'  # run的时候用
configPath = os.path.join(os.path.dirname(os.getcwd())+ r'/testConfig/config.ini')  # 如果只运行当前脚本，用这个测试报告的路径

class ReadConfig(object):

    # 构造函数，读取配置文件
    def __init__(self):

        self.config = configparser.ConfigParser()
        self.config.read(configPath, encoding="utf-8-sig")

    def switch(self):
        """"""
        value = self.config.get("switch", "test")
        return value

    # get some http info from file :config.ini
    def get_testUrl(self, name):
        value = self.config.get("testUrl", name)
        return value

    def get_account(self, name):
        value = self.config.get("account", name)
        return value


print(configPath)
readConfig= ReadConfig()
name = readConfig.get_account("yz_loginName")
print(name)
