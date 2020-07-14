# -*- coding: utf-8 -*-
'''
@File : walker.py
@Date : 2020/7/3
@Auther : shenxudong3
'''


class RandomWalker:
    def __init__(self, G, p=1, q=1):
        """

        :param G:
        :param p: Return parameter, controls the likelihood of immediately revisiting a node in the walk.
        :param q: In-out parameter,allows the search to differentiate between "inward" and "outward" needs.
        """
        self.G = G
        self.p = p
        self.q = q

    def