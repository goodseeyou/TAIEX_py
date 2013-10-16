'''
Created on 2013/10/16

@author: PaulLin
'''

class OptionInstance():

    def __init__(self,filepath):
        try:
            with open(filepath) as data: #week, exercise price, call or put,trading day,trading time, open, high, low, trading price, volume
                self.instances = []
                for line in data:
                    line = line.rstrip('\n').strip()
                    (sdate,eprice,action,date,time,openp,highp,lowp,tprice,volume) = str(line).split(sep=',', maxsplit=10)
                    '''
                    substring (comprehension)
                    |a|b|c|d|e|f|
                    0 1 2 3 4 5 6
                    abc = 0:3
                    ''' 
                    syear = sdate[0:4]
                    smonth = sdate[4:6]
                    if len(sdate)<7:
                        sweek = 'W3'
                    else:
                        sweek = sdate[6:8]
                    tyear = date[0:4]
                    tmonth = date[4:6]
                    tday = date[6:8]
                    thour = time[0:2]
                    tminute = time[2:4]
                    tsecond = time[4:6]
                    self.instances.append({'settlementYear':str(syear)
                                           ,'settlementMonth':smonth
                                           ,'settlementWeek':sweek
                                           ,'tradingYear':tyear
                                           ,'tradingMonth':tmonth
                                           ,'tradingDay':tday
                                           ,'tradingHour':thour
                                           ,'tradingMinute':tminute
                                           ,'tradingSecond':tsecond
                                           ,'exercisePrice':eprice
                                           ,'action':action
                                           ,'open':float(openp)
                                           ,'high':float(highp)
                                           ,'low':float(lowp)
                                           ,'tradingPrice':float(tprice)
                                           ,'volume':volume})
        except IOError as ioerror:
            print("error occurs: "+ioerror)
        
    def getOptionInstances(self):
        return self.instances
                    

class OptionSettlement():
    def __init__(self,filepath):
        try:
            with open(filepath) as data: #settlementTime,week,price
                lines = [line.rstrip('\n').strip() for line in data]
                self.lst = []
                for line in lines:
                    (time,name,price)=str(line).split(sep=',', maxsplit=3)
                    time = str(time).split(sep='/', maxsplit=3)
                    year = time[0]
                    month = time[1]
                    day = time[2]
                    if len(name)<7:
                        week = 'W3'
                    else:
                        week = name[6:8]
                    self.lst.append({'settlementYear':year,'settlementMonth':month,'settlementWeek':week,'settlementDay':day,'settlementPrice':price})
        except IOError as ioError:
            print("error occurs: "+str(ioError))
    
    def getSettlementList(self):
        return self.lst
    
    def getSettlementDay(self,year,month,week):
        for settlement in self.lst:
            if int(settlement['settlementYear'])==int(year) and int(settlement['settlementMonth']) ==int(month) and settlement['settlementWeek']==week:
                return int(settlement['settlementDay'])
    
    def getSettlementPrice(self,year,month,weekOrDay):
        for settlement in self.lst:
            if int(settlement['settlementYear'])==int(year) and int(settlement['settlementMonth']) ==int(month):
                try:
                    settlementDay = int(weekOrDay)
                    if int(settlement['settlementDay']) == settlementDay:
                        return int(settlement['settlementPrice'])
                except:
                    settlementWeek = weekOrDay
                    if settlementWeek == settlement['settlementWeek']:
                        return int(settlement['settlementPrice'])
            
            