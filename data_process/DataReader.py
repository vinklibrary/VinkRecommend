# -*- coding: utf-8 -*-
'''
@File : DataReader.py
@Date : 2020/7/17
@Auther : shenxudong3
'''


class DataReader:
    def __init__(self):
        self.read_func_dict = {
            1: self.read_version1
        }

    def ReadData(self, path, type=1):
        self.read_func_dict[type](path)

    def read_version1(self, path):
        file = open(path, 'r')
        data = {}
        for line in file.readlines():
            user, item, score = line.split('\t')
            data.setdefault(user, {})
            data[user].setdefault(item, score)
        return data

