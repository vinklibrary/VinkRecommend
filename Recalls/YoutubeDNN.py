import tensorflow as tf
import numpy as np


class YoutubeDNNRecall:
    def __init__(self, args):
        self.video_total_num = args.video_total_num
        self.search_total_num = args.search_total_num
        
# import numpy as np
# from tensorflow.contrib import layers
# from tensorflow.python.ops import nn_impl
# from tensorflow.python.ops import array_ops
# from tensorflow.python.ops import nn_ops
# from recall.data_process import get_batch
# from utils.utils import list2array
# from utils.config import SuperPrams
