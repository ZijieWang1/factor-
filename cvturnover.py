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
        self.needFields = [t.TRDSTAT, t.VOLUME, t.SHRFREE]  # ������Ҫ���ֶ�


    def factor_definition(self):
        s = time.time()
        needData = self.needData                                # ������������

        num = 5
        turn = needData[t.VOLUME] / needData[t.SHRFREE]
        factor = (turn-self.calculator.Mean(x=turn,num=num))/self.calculator.Std(x=turn, num=num)
        factor[np.isinf(factor)] = np.nan

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()