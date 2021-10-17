'''
wallet.py
jason miles 

a wallet class to track account balances and holdings
'''

from collections import defaultdict

class Wallet:
    '''
    Wallet:
        available balance   : self.avail
        holding             : a dictionary that holds coin : tokens
        deposited           : history count of $ deposited
    '''
    
    def __init__(self, balance=0):
        # 
        self.avail = balance
        
        # $ deposited
        self.deposited = balance
        
        # dictionary of tokens holding
        # token : units
        self.holding = {}


    def deposit(self, amt):
        self.deposited += amt
        self.avail += amt
    
    def withdraw(self, amt):
        if self.avail > amt:
            self.avail -= amt
        else:
            print("not enough to withdraw")

    
    def buy(self, token, units, price):
        # print('buying..')

        # check if can buy
        if self.avail < (price * units):
            units = self.avail // price
        
        amt = units * price        
        
        self.avail -= amt            
        
        # update dictionary
        #print("Bought {} {} at {}!".format(units, token, price))

        self.holding[token] = self.holding.get(token, 0) + units

        # success
        return self.avail
    

    def sell(self, token, units, price):
        #print('selling..')

        # check
        if self.holding.get(token, 0) < units:
            units = self.holding.get(token, 0)
        
        # sell some
        amt = units * price
        
        self.avail += amt

        #print("sold {} {} at {}!".format(units, token, price))

        self.holding[token] -= units

        return amt
    
    def print_balance(self, price=None):
        print("Deposited: {}".format(self.deposited))
        print("Available: {}".format(self.avail))
        print("Holding:")
        for coin in self.holding.keys():
            print("    coin: {}  |  amount: {}".format(coin, self.holding[coin]))
            if price:
                print("     total: ${}".format(self.holding[coin] * price))
        print()
    
    def calc_profit(self):
        return self.balance - self.deposited




