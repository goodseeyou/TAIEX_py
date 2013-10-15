# coding=big5
from preprocessing import Options
import os

'''
Created on 2013/10/15

@author: PaulLin
'''

if __name__ == '__main__':
    settlementDataPath = os.path.abspath("D:\\Dropbox\\Master work\\資料集\\結算\\option_settlment.csv")
    sop = Options.OptionSettlement(settlementDataPath)
    print(sop.getSettlementList()[0])
    print(sop.getSettlementPrice('2012', 11, '28'))
    optionsDataPath = os.path.abspath("D:\\Dropbox\\Master work\\資料集\\期貨選擇權交易紀錄\\選擇權\\周選擇權1分K\\TXO_1MIN_WEEKLY_rmTXO.csv")
    ops = Options.OptionInstance(optionsDataPath)
    ins = ops.getOptionInstances()
    print(ins[0])