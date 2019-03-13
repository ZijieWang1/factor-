# coding=utf8
__author__ = 'wangjp'

import time

import numpy as np
import pandas as pd
from FactorModule.FactorBase import FactorBase
from DataReaderModule.Constants import ALIAS_FIELDS as t

class Factor(FactorBase):

    def __init__(self):
        super(Factor,self).__init__()
        self.factorName = __name__.split('.')[-1]
        self.needFields = [t.OPEN, t.HIGH, t.LOW, t.CLOSE, t.ADJFCT, t.TRDSTAT]  # 设置需要的字段

    def factor_definition(self):
        """
        :return:
        """
        s = time.time()
        needData = self.needData                                # 计算所需数据

        adjLow = needData[t.LOW] * needData[t.ADJFCT]
        adjHigh = needData[t.HIGH] * needData[t.ADJFCT]
        adjOpen = needData[t.OPEN] * needData[t.ADJFCT]
        adjClose = needData[t.CLOSE] * needData[t.ADJFCT]
        hldiff = adjHigh-adjLow
        hldiff[hldiff == 0] = np.nan        # 避免除0导致inf
        factor = self.calculator.Sum(x=(adjClose-adjOpen).abs(), num=5)/self.calculator.Sum(x=hldiff, num=5)

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()