# coding:utf-8
import json

import requests

from framework.readExcel import ExcelUtil
from framework.writeexcel import copy_excel, Write_excel

def send_requests(s, testdata):
    '''封装requests请求'''
    method = testdata["method"]
    url = testdata["url"]
    # url后面的params参数
    try:
        params = eval(testdata["params"])
    except:
        params = None
    # 请求头部headers
    try:
        headers = eval(testdata["headers"])
        print("请求头部：%s" % headers)
    except:
        headers = None
    # post请求body类型
    type = testdata["type"]

    test_nub = testdata['id']
    print("*******正在执行用例：-----  %s  ----**********" % test_nub)
    print("请求方式：%s, 请求url:%s" % (method, url))
    print("请求params：%s" % params)

    # post请求body内容
    try:
        bodydata = eval(testdata["body"])
    except:
        bodydata = {}

    # 判断传data数据还是json
    if type == "data":
        body = bodydata
    elif type == "json":
        body = json.dumps(bodydata)
    else:
        body = bodydata
    if method == "post": print("post请求body类型为：%s ,body内容为：%s" % (type, body))

    verify = False
    res = {}   # 接受返回数据

    try:
        r = s.request(method=method,
                      url=url,
                      params=params,
                      headers=headers,
                      data=body,
                      verify=verify
                       )
        print("页面返回信息：%s" % r.content.decode("utf-8"))
        res['id'] = testdata['id']
        res['rowNum'] = testdata['rowNum']
        res["statuscode"] = str(r.status_code)  # 状态码转成str
        res["text"] = r.content.decode("utf-8")
        res["times"] = str(r.elapsed.total_seconds())   # 接口请求时间转str
        if res["statuscode"] != "200":
            res["error"] = res["text"]
        else:
            res["error"] = ""
        res["msg"] = ""
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            print("用例测试结果:   %s---->%s" % (test_nub, res["result"]))
        else:
            res["result"] = "fail"
        return res
    except Exception as msg:
        res["msg"] = str(msg)
        return res

def wirte_result(result, filename="result.xlsx"):
    # 返回结果的行数row_nub
    row_nub = result['rowNum']  # 写入第几行
    wt = Write_excel(filename)
    # wt = Write_excel(r"D:/Workspace/InterfaceTestFramework/data/demo_api.xlsx") # 测试写入路径报告
    print(result['statuscode'])
    request_result= result['text']  # request_result  字符串类型
    try:
        wt.write(row_nub, 12, request_result)            # 写入返回结果
    except ValueError:
        print("写入request_result不是字符串！")
    except Exception as e:
        print("写入Excel报错，请检查，错误为：{}" .format(e))

    # request_result_ = json.loads(request_result)  # 如果取返回的相关字段，将字符串转为dict
    # # jsoninfo = json.dumps(dictinfo)   # （dict）转为字符串
    # print(request_result_["r"])
    # print(request_result_["m"])
    # print(request_result_["h"])
    # print(request_result_["d"])
    # dd = request_result_["d"]  # dd是dict，需转为字符串
    # r = request_result_["r"]
    # m = request_result_["m"]
    # h = request_result_["h"]
    # d = json.dumps(dd)

if __name__ == "__main__":
    data = ExcelUtil("debug_api.xlsx").dict_data()
    print(data[0])
    s = requests.session()
    res = send_requests(s, data[0])
    copy_excel("debug_api.xlsx", "result.xlsx")
    wirte_result(res, filename="result.xlsx")