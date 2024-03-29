# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,request
from threading import Thread
from datetime import datetime
import pandas as pd
import random


app = Flask(__name__)
 
@app.route('/hist')
def All_data():
    global all_data
    
    df = pd.DataFrame(all_data,columns=['Datetime','Text'])
    df = df.sort_values(by=['Datetime'], ascending=False)
    return df.to_html(header="true", table_id="table")

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    global lastTrades
    temp = lastTrades[-6:]
    print(temp)
    html = hadeging(temp)
    return html

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
    for data in list(set(singleData)):
        sss += changeDate(data) + "#"
        
    return sss


def read_file():
    while True:
        try:
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
        except:
            print('Data reading not working!')



# main driver function
if __name__ == '__main__':
    dataFile = ''
    all_data = [ ]
    text_list = []
    lastTrades = []
    fingalSignals = {}
    thread = Thread(target = read_file)
    thread.start()
    app.run(host= "199.247.31.183" , port="80")
    # app.run(host='0.0.0.0' , port='80')
    
	
