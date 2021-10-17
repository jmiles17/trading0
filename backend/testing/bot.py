#!/usr/bin/env python3.8

import os

import numpy as np
import pandas as pd

from data.processor import *
from wallet import *


class Bot:

    def __init__(self):
        # wallet
        self.w = Wallet()
        # data proc
        self.proc = Processor()
    

    def add_balance(self, amt):
        self.w.deposit(amt)
    
    def load_data(self, filename):
        self.proc.read_data(filename)
    
    def buy(self, units, price):
        token = 'alg'
        return self.w.buy(token, units, price)
    
    def sell(self, units, price):
        self.w.sell('alg', units, price)
    
    def test_signals(self, price, low_ma, high_ma):
        
        # signals: price_low, price_high, low_high
        print()

    def backtest(self, interval, duration, low, high):

        # shortest ma
        #low = 20
        # longest ma
        #high = 50

        unit = 200

        price_low = False # price < low
        price_high = False # price below 50 ma
        low_high = False  # 'short below long' - if 20 ma is below 50

        epochs = self.proc.get_size() // interval
        
        # skip first 50 timestamps ?
        for step in range(epochs):
            # get price
            price = self.proc.get_close(step * interval)

            # get calculations
            low_ma = self.proc.get_ma(low, price)
            high_ma = self.proc.get_ma(high, price)

            # 
            if step < 50:
                continue

            # test signals

            
            

            # update
            if price < low_ma:
                price_low = True
            else:
                price_low = False
            
            if low_ma < high_ma:
                low_high = True
            else:
                low_high = False

            if step % 20 == 0:
                print()
                self.w.get_balance(price)
                print()

        self.w.get_balance(price)




if __name__ == '__main__':

    b = Bot()

    b.add_balance(1000)

    b.load_data('./data/algusd.csv')

    b.backtest(60, 5000, 20, 50)

    





