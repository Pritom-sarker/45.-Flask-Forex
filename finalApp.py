# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,request
from threading import Thread
from datetime import datetime
import pandas as pd
import random
import time

def hadeging(s):
    singleData = []
    lines =  s
    for line in lines:
        temp = line.split('_')
        if len(temp) < 2:
            continue
        thisTimeStamp = temp[2]
        for step2 in lines:
                t2 = step2.split('_')
            
                if step2 == line:
                    continue
            # try:
                if thisTimeStamp in t2 :
                    pair1 = temp[3]
                    pair2 = t2[3]
                    
                    if pair1 == pair2:
                        if 'BUY' in t2 and 'SELL' in temp  or 'SELL' in t2 and 'BUY' in temp:
                            b2bL1 = t2[-1]
                            b2bL2 = temp[-1]
                            if int(b2bL1[-1]) == 0 or int(b2bL2[-1]) == 0:
                                revisedSignal1 = (str(step2)[:-2] +"_" +str(0))
                                revisedSignal2 = (str(line)[:-2] + "_" +str(0))
                                singleData.append(revisedSignal1)
                                singleData.append(revisedSignal2)
                            else:
                                prefix = [ int(b2bL1), int(b2bL2) ] 
                                finalPrefix = min(prefix)
                                revisedSignal1 = (str(step2)[:-2] +"_" +str(finalPrefix))
                                revisedSignal2 = str(str(line)[:-2] + "_" +str(finalPrefix))
                                singleData.append(revisedSignal1)
                                singleData.append(revisedSignal2)
                                
    def changeDate(temp):
        parts = str(temp).split('_')
        if parts[4] == 'BUY':
            parts[2] = str(int(parts[2]) - 1)
        s = ""
        for prt in parts:
            s+=prt+"_"
        return s[:-1]
    
    sss = ""
    print(list(set(singleData)))
    for data in list(set(singleData)):
        sss += changeDate(data) + "#"
        
    return sss


def main():
    global lastTrades
    
    temp = lastTrades[-3:]
    print(temp)
    new = hadeging(temp)
    print(new.replace("#","\n"))


def read_file():
    global tempTextList
    f = open('data.txt','r')
    s = ''
    for line in f:
        s+=line
    orders = s.split("#")
    for order in orders:
        if order not in lastTrades and len(order) > 4: 
            lastTrades.append(order)
            all_data.append([datetime.now().strftime("%d/%m/%Y %H:%M:%S"), order])
    f.close()


# main driver function
if __name__ == '__main__':
    all_data = [ ]
    lastTrades = []
    fingalSignals = {}
    tempTextList = []
    
    while True:
        thread = Thread(target = read_file)
        thread.start()
        print('-------------')
        main()
        print(len(lastTrades))
        input('Press')
    
	
