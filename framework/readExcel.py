#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 23:19
# @Author  : StalloneYang
# @File    : readExcel.py
# @desc: 读取Excel
import xlrd


class ExcelUtil(object):
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为 key 值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于 1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应 values 值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == "__main__":
    filepath = r"D:\Workspace\InterfaceTestFramework\data\demo_api.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath, sheetName)
    print(data.dict_data())
