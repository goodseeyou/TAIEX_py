# coding=big5
from preprocessing import Options
import os

'''
Created on 2013/10/15

@author: PaulLin
'''

if __name__ == '__main__':
    settlementDataPath = os.path.abspath("D:\\Dropbox\\Master work\\��ƶ�\\����\\option_settlment.csv")
    sop = Options.OptionSettlement(settlementDataPath)
    print(sop.getSettlementList()[0])
    print(sop.getSettlementPrice('2012', 11, '28'))
    optionsDataPath = os.path.abspath("D:\\Dropbox\\Master work\\��ƶ�\\���f����v�������\\����v\\�P����v1��K\\TXO_1MIN_WEEKLY_rmTXO.csv")
    ops = Options.OptionInstance(optionsDataPath)
    ins = ops.getOptionInstances()
    print(ins[0])
    
    newcsvpath = os.path.abspath("D:\\Dropbox\\Master work\\��ƶ�\\���f����v�������\\����v\\�P����v1��K\\preprocessing.csv")
    try:
        with open(newcsvpath,'w') as output:
            for instance in ins:
                settlementPrice = sop.getSettlementPrice(instance['settlementYear'],instance['settlementMonth'],instance['settlementWeek'])
                settlementDay = sop.getSettlementDay(instance['settlementYear'],instance['settlementMonth'],instance['settlementWeek'])
                print(str(instance['settlementYear'])+","+str(instance['settlementMonth'])+","+str(instance['settlementWeek'])+","+str(settlementDay)+","+str(instance['exercisePrice'])+","+str(instance['action'])+","+str(instance['tradingYear'])+","+str(instance['tradingMonth'])+","+str(instance['tradingDay'])+","+str(instance['tradingHour'])+","+str(instance['tradingMinute'])+","+str(instance['tradingSecond'])+","+str(instance['open'])+","+str(instance['high'])+","+str(instance['low'])+","+str(instance['tradingPrice'])+","+str(instance['volume'])+","+str(settlementPrice),file=output)
    except IOError as ioerror:
        print("ioerror occurs: "+str(ioerror))
    finally:
        print("OK")
        