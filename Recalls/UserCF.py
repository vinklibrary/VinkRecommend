# -*- coding: utf-8 -*-
'''
@File : UserCF.py
@Date : 2020/7/17
@Auther : shenxudong3
'''

def UserSimilarity(data):
    W = dict()
    for u in data.keys():
        for item in u.keys():
