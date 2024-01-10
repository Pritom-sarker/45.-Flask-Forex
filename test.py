s = "ORDER_9_1704660010000_ETHUSD_BUY_TP.0.13_SL.0.13_1#ORDER_8_22660120000_BTCUSD_BUY_TP.0.05_SL.0.05_1#ORDER_9_1704660120000_BTCUSD_SELL_TP.0.05_SL.0.05_0#ORDER_8_1704660720000_BTCUSD_BUY_TP.0.05_SL.0.05_1#ORDER_9_1704660720000_BTCUSD_SELL_TP.0.05_SL.0.05_5#"

newS =s
singleData = []
lines =  s.split("#")
for line in lines:
    temp = line.split('_')
    # print(temp)
    if len(temp) < 2:
        continue
    flag = 0
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
                    flag =1
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
                            revisedSignal2 = str(str(line)[:-2] + "_" +str(finalPrefix)).replace(thisTimeStamp,str(int(thisTimeStamp)+1))
                            print(revisedSignal2)
                            singleData.append(revisedSignal1)
                            singleData.append(revisedSignal2)
                

    

print('----------------------------')
print(s.replace('#','\n'))
sss = ""
for data in list(set(singleData)):
    sss += data + "#"
print('----------------------------')
print(sss.replace('#','\n'))
    
