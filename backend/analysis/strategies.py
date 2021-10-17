'''
strategies.py
Jason Miles

a class of trading methods and strategies
'''



# Curves
class Curves:

    def __init__(self):
        print()
    
    def decide(self):
        print()



# Crosses
class Crosses:

    def __init__(self, short, far):
        '''
        short : shortest period duration
        far   : longest period duration
        '''
        
        # bounds
        self.short_bnd = short
        self.long_bnd = far
        
        # history
        self.short_ma = [0]
        self.long_ma = [0]
        
        # signals
        # price < low
        self.price_low = False
        # low < high
        self.low_high = False
    

    def decide(self, price):
        '''
        function that all strategies implement
        returns either buy / sell / hold

        calculates position of price in regards to moving averages
        '''
        # calculate moving averages
        sma, lma = self.calc_ma(price)
        # print("price: ", price)
        # print("shortest ma: ", sma)
        # print("longest ma: ", lma)

        if self.price_low and ( price > sma ):
            self.price_low = False
            return 'buy'
        if self.low_high and ( sma > lma ):
            self.price_low = False
            return 'buy'
        
        if not self.price_low and ( price < sma ):
            self.price_low = True
            return 'sell'
        if not self.low_high and ( sma < lma ):
            self.low_high = True
            return 'sell'

        
        # update booleans
        if price < sma:
            self.price_low = True
        else:
            self.price_low = False
        
        if sma < lma:
            self.low_high = True
        else:
            self.price_low = False


        return 'hold'

    def calc_ma(self, price):

        # append to arrays
        self.short_ma.append(price)
        self.long_ma.append(price)

        # update totals
        self.short_ma[0] += price
        self.long_ma[0]  += price

        # test if need to remove least recent element
        if len(self.short_ma) > ( self.short_bnd + 1 ):
            # remove
            short_least = self.short_ma.pop(1)
            # update total
            self.short_ma[0] -= short_least
        
        if len(self.long_ma) > ( self.long_bnd + 1 ):
            long_least = self.long_ma.pop(1)
            self.long_ma[0] -= long_least
        
        sma = self.short_ma[0] / self.short_bnd
        lma = self.long_ma[0] / self.long_bnd

        return sma, lma

