

__author__ = 'wjp'

import time

import numpy as np
import pandas as pd
from FactorModule.FactorBase import FactorBase
from DataReaderModule.Constants import ALIAS_FIELDS as t

class Factor(FactorBase):

    def __init__(self):
        super(Factor,self).__init__()
        self.factorName = __name__.split('.')[-1]
        self.needFields = [t.TRDSTAT, t.AMOUNT, t.PCTCHG,t.OPEN,t.CLOSE,t.HIGH,t.LOW]  # 设置需要的字段


    def factor_definition(self):
        s = time.time()
        needData = self.needData                                # 计算所需数据

        amt = needData[t.AMOUNT]
        ret = needData[t.PCTCHG]
        close = needData[t.CLOSE]
        open = needData[t.OPEN]
        high=needData[t.HIGH]
        low=needData[t.LOW]
        num = 10  # num=5
        direction = [(high - low) - (close - open)]
        amtret = (amt)/ self.calculator.Mean(x=amt, num=num) * ret
        retdiff = self.calculator.Diff(x=amtret,num=2)  # (x=amtret,num=1)
        factor = self.calculator.Corr(x=amtret, y=retdiff, num=num)

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()