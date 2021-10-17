#!/usr/bin/env python3.8

'''
main.py
Jason Miles

currently used to run backtesting
'''

import sys

from testing.backtest import Backtest


def usage():
    print('''
    ./main.py [arguments]

    arguments:
        -p              : run in production mode

        -b <file>       : run backtesting on data from file
        -i <interval>   : data point interval in minutes
        
        -s <strategy>   : use a specific trading strategy
                            default: curves
                            other: crosses , prediction
        -d <amount>     : deposit a specific initial amount of $
        -t <token>      : token to buy/sell
        -u <units>      : amount of units to buy/sell per transaction
        -v              : verbose - print updates

        -l <n>          : low end moving average
        -h <n>          : high end moving average
    ''')



if __name__ == '__main__':

    usage()

    # setup vars
    production_mode = False
    backtest = True
    datafile = './data/sheets/algusd.csv'
    interval = 60
    strategy = 'curves'
    depo_amt = 1000
    token = 'alg'
    units = 100
    verbose = True
    short_avg = 10
    long_avg = 100

    # read args
    cmd_line = sys.argv[1:]
    arg = cmd_line.pop(0)

    while arg:
        if arg[0] == '-':
            if arg[1] == 'p':
                production_mode = True
                print("running in production mode")
            if arg[1] == 'b':
                backtest = True
                datafile = cmd_line.pop(0)
                print("backtesting: ", datafile)
            if arg[1] == 'i':
                interval = int(cmd_line.pop(0))
                print("testing points every {} minutes".format(interval))
            if arg[1] == 's':
                strategy = cmd_line.pop(0)
                print("strategy: ", strategy)
            if arg[1] == 'd':
                depo_amt = int(cmd_line.pop(0))
                print("depositing: $", depo_amt)
            if arg[1] == 't':
                token = cmd_line.pop(0)
                print("token: ", token)
            if arg[1] == 'u':
                units = int(cmd_line.pop(0))
                print("units: ", units)
        # update
        try:
            arg = cmd_line.pop(0)
        except:
            break
    

    # run
    if backtest:
        
        # setup testing
        bt = Backtest()
        bt.load_data(datafile)
        bt.add_balance(depo_amt)

        if strategy == 'crosses':
            bt.set_strategy(strategy, short_avg, long_avg)
        elif strategy == 'curves':
            bt.set_strategy(strategy)
        
        # run testing
        bt.backtest(interval, token, units)





