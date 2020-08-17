# -*- coding: utf-8 -*-
'''
@File : walker.py
@Date : 2020/7/3
@Auther : shenxudong3
'''
import itertools
import networkx as nx
from joblib import Parallel, delayed

from Utils.UtilTools import *

class RandomWalker:
    def __init__(self, G:nx.DiGraph, p=1, q=1):
        """

        :param G:
        :param p: Return parameter, controls the likelihood of immediately revisiting a node in the walk.
        :param q: In-out parameter,allows the search to differentiate between "inward" and "outward" needs.
        """
        self.G = G
        self.p = p
        self.q = q

    def deepwalk_walk(self, walk_length, start_node):

        walk = [start_node]

        while len(walk) < walk_length:
            cur = walk[-1]
            cur_nbrs = list(self.G.neighbors(cur))
            if len(cur_nbrs) > 0:
                if len(self.G.get_edge_data(cur, cur_nbrs[0]))==0:
                    cur_weights = [1 for nbr in cur_nbrs]
                else:
                    cur_weights = [self.G.get_edge_data(cur, nbr)['weight'] for nbr in cur_nbrs]
                walk.append(random_pick_weights(cur_nbrs, cur_weights))
            else:
                break
        return walk

    def

    def simulate_walks(self, num_walks, walk_length, workers=1, verbose=0):
        '''

        :param num_walks: 随机游走条数的数量
        :param walk_length: 随机游走的长度
        :param workers: 并行数
        :param verbose: 并行可视化
        :return:
        '''
        G = self.G
        nodes = list(G.nodes())

        results = Parallel(n_jobs=workers, verbose=verbose, )(
            delayed(self._simulate_walks)(nodes, num, walk_length) for num in
                partition_num(num_walks, workers))

        walks = list(itertools.chain(*results))
        return walks

    def _simulate_walks(self, nodes, num_walks, walk_length,):
        walks = []
        for _ in range(num_walks):
            random.shuffle(nodes)
            for v in nodes:
                if self.p == 1 and self.q == 1:
                    walks.append(self.deepwalk_walk(
                        walk_length=walk_length, start_node=v))
                else:
                    walks.append(self.node2vec_walk(
                        walk_length=walk_length, start_node=v))
        return walks
