''' 
processor.py
Jason Miles

a data processor class used to return data for backtesting trading methods
'''

import os

import numpy as np
import pandas as pd


class Processor:

    def __init__(self):
        self.size = 0
        
    
    def read_data(self, filename):
        '''open csv filename and read data
        Args:
            filename: a csv file with historical coin data
        '''

        # load and index
        self.df = pd.read_csv(filename, index_col='time')
        self.df.index = pd.to_datetime(self.df.index, unit='ms')

        # calc change
        self.df['change'] = (self.df.close - self.df.open) / self.df.open * 100

        # add previous close
        self.df['prev_close'] = self.df['close'].shift(1)

        self.size = len(self.df)
        # print(self.size)

    
    def get_close(self, stamp):
        '''returns closing price for a stamp index'''
        return self.df.iloc(0)[stamp]['close']
    

    def get_size(self):
        '''returns size of dataframe'''
        return self.size

    







