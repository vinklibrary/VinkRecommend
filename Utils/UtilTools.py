# -*- coding: utf-8 -*-
'''
@File : UtilTools.py
@Date : 2020/7/21
@Auther : shenxudong3
'''
import random

def random_pick_weights(items: list[object], weights: list[int]) -> object:
    table = [z for x, y in zip(items, weights) for z in [x] * y]
    return random.choice(table)

def partition_num(num:int, workers:int)-> list[int]:
    if num % workers == 0:
        return [num // workers] * workers
    else:
        return [num // workers] * workers + [num % workers]