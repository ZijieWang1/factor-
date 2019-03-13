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
        self.neutral = False
        self.factorName = __name__.split('.')[-1]
        self.needFields = [t.HIGH, t.LOW, t.CLOSE, t.OPEN,t.ADJFCT,t.PCTCHG,t.PB,t.PE]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData                                # 计算所需数据

        adjLow = needData[t.LOW] * needData[t.ADJFCT]     #列是时间，行是股票代码
        adjHigh = needData[t.HIGH] * needData[t.ADJFCT]
        adjClose = needData[t.CLOSE] * needData[t.ADJFCT]
        adjOpen=needData[t.OPEN]*needData[t.ADJFCT]
        Shortcut=2*(adjHigh-adjLow)-abs(adjOpen-adjClose)
        illiq=Shortcut/needData[t.PCTCHG]
        factor = self.calculator.Mean(x=Shortcut, num=10)

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()