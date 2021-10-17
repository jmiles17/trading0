'''
backtest.py
Jason Miles

a testing bot used to backtest trading strategies
'''

from data.processor import *
from wallet.wallet import *
from analysis.strategies import *


class Backtest:

    def __init__(self):
        # wallet
        self.w = Wallet()
        # data proc
        self.proc = Processor()
        # strategy
        self.strat = None

    def add_balance(self, amt):
        self.w.deposit(amt)
    
    def load_data(self, filename):
        self.proc.read_data(filename)
    
    def set_strategy(self, strategy, short_avg=0, long_avg=0):
        if strategy == 'crosses':
            self.strat = Crosses(short_avg, long_avg)
        if strategy == 'curves':
            self.strat = Curves()
    
    def print_balance(self, price=None):
        self.w.print_balance(price)
    
    def buy(self, token, units, price):
        self.w.buy(token, units, price)
    
    def sell(self, token, units, price):
        self.w.sell(token, units, price)

    def backtest(self, interval, token, units, duration=None):

        # initialize dict of tokens
        self.buy(token, 0, 0)

        #duration = 1000

        if not duration:
            epochs = self.proc.get_size() // interval
        else:
            epochs = duration
        
        # init metrics
        buy_ct = 0
        sell_ct = 0
        
        # 
        for step in range(epochs // 10):

            # get price
            price = self.proc.get_close(step * interval)

            # test strategy
            decision = self.strat.decide(price)

            if decision == 'buy':
                buy_ct += 1
                self.buy(token, units, price)
            elif decision == 'sell':
                sell_ct += 1
                self.sell(token, units, price)
            
            if step % 10 == 0:
                self.print_balance(price)
        
        print("bought {} times".format(buy_ct))
        print("sold {} times".format(sell_ct))
        self.print_balance(price)
            


    





