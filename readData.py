

'''
Read Financial Datas by Tushare
author:FanGhost
Time:2016-3-15 21:34:01
'''
import tushare as ts
import numpy as np
import pandas as pd
#get the main stock
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Data:
    def __init__(self):
        return

    def get_data(self):
        # get stock basics
        stock_basics=ts.get_stock_basics()
        # get report data

    def getReportData(self,year,month):

        return
if __name__=='__main__':
    print 'stock_basics:'
    print ts.get_stock_basics()
#read data by