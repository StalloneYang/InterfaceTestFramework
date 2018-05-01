#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/1 16:48
# @Author  : StalloneYang
# @File    : bs4res.py
# @desc: 抓取网页
import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()

browser = requests.session()
url = "http://www.uustv.com/"

data = {
    "fontcolor": "#000000",
    "fonts": "jfcs.ttf",
    "sizes": "60",
    "word": "杨大大"
}
re = browser.post(url,data =data)
print(re.content.decode("utf-8"))
print("=================分割线====================")
soup = BeautifulSoup(re.content, "html.parser")
tag = soup.img
src = tag['src']  # img中的 src="tmp/152516933098228.gif"
print(src)
picURL = url + src  # 拼接url
print(picURL)


