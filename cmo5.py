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
        self.needFields = [t.HIGH, t.LOW, t.CLOSE, t.ADJFCT, t.AMOUNT, t.PCTCHG, t.TRDSTAT]  # 设置需要的字段


    def factor_definition(self):
        s = time.time()
        needData = self.needData                                # 计算所需数据

        amt = needData[t.AMOUNT]
        ret = needData[t.PCTCHG]
        adjLow = needData[t.LOW] * needData[t.ADJFCT]
        adjHigh = needData[t.HIGH] * needData[t.ADJFCT]
        adjClose = needData[t.CLOSE] * needData[t.ADJFCT]
        hmc = adjLow + adjHigh + adjClose
        idx = ((ret > 0) | (self.calculator.Diff(x=hmc, num=1) > 0)) & (self.calculator.Diff(x=amt, num=1) > 0)
        absret = ret.abs()
        posRet = self.calculator.Sumif(x=absret, condition=idx, num=5)
        negRet = self.calculator.Sumif(x=absret, condition=~idx, num=5)
        factor = -(posRet + negRet) / (posRet - negRet)        # 计算5日动量
        factor[np.isinf(factor)] = np.nan

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()