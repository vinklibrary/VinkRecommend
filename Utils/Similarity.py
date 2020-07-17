# -*- coding: utf-8 -*-
'''
@File : Similarity.py
@Date : 2020/7/17
@Auther : shenxudong3
'''
import math

class similarity:
    def __init__(self):
        pass

    def JaccardSim(self, user1:set, user2:set):
        return len(user1.intersection(user2))/len(user1+user2)

    def CosinSim(self, user1:set, user2:set):
        return len(user1.intersection(user2))/math.sqrt(len(user1) * len(user2) * 1.0)



