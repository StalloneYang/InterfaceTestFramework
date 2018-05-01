#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/30 18:38
# @Author  : StalloneYang
# @File    : todict.py
# @desc:

class CallbackFunName_json():

    def callbackFunName_json(results):
        '''把返回的callbackFunName结果转换为字典'''

        #null值预处理（解决eval问题）
        global null
        null = 'null'
        #false值预处理（解决eval问题）
        global false
        false = 'false'
        #true值预处理（解决eval问题）
        global true
        true = 'true'


        # #正则取值
        # resultsed = re.findall(r"callbackFunName\((.*)\);",results)
        # #转换为字典方式
        # results_dict = eval(resultsed[0])
        # return results_dict
