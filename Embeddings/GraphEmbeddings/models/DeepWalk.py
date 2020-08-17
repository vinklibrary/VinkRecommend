# -*- coding: utf-8 -*-
'''
@File : DeepWalk.py
@Date : 2020/7/3
@Auther : shenxudong3
DeepWalk 的 模型实现。 主要返回图中节点的 Embedding向量。
'''
from Embeddings.Utils import RandomWalker

class DeepWlak:
    def __init__(self, graph, window_size: int, embedding_size:int,  ):
        self.w2v_model = None  # 支持w2v模型导入
        self.walker = RandomWalker(graph, p=1, q=1, ) # 随机游走实现
        self.sentences = self.walker.simulate_walks()



