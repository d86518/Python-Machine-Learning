# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:58:19 2017

@author: 黃大祐
"""
#每月第三個禮拜三過了後 會是下個月的報價 所以每天刷比較保險
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('TXF20112015.csv',sep=',',header=None)
TAIEX = df.values  #資料取出為dataframe 變為nrowX5col的array
#0time 1收 2開 3高 4低
tradeday = list(set(TAIEX[:,0]//10000)) #只有前面八碼的日期到日 set讓資料不重複
tradeday.sort()
profit = np.zeros((len(tradeday),1))
for i in range(len(tradeday)):
    date = tradeday[i]
    idx = np.nonzero(TAIEX[:,0]//10000==date)[0] #拿出index col=0 那天的第一分鐘(若index=0)買進來  等到最後一筆賣掉
    idx.sort()
    for j in range(len(idx)):
        if(TAIEX[idx[j],2]>=TAIEX[idx[0],2]+30): #當大於第一筆30才買進
            p1 = TAIEX[idx[j],2]
            idx2 = np.nonzero(TAIEX[idx,4]<=p1-30)[0] #看有沒有<=30 
            if(len(idx2)==0): 
                p2 = TAIEX[idx[-1],1]
            else:
                p2 = TAIEX[idx[idx2[0]],1]  
            profit[i] = p2-p1   
        elif(TAIEX[idx[j],2]<=TAIEX[idx[0],2]-30):
            p1 = TAIEX[idx[j],2]
            idx2 = np.nonzero(TAIEX[idx,4]>=p1+30)[0] #放空漲30是損
            if(len(idx2)==0): 
                p2 = TAIEX[idx[-1],1]
            else:
                p2 = TAIEX[idx[idx2[0]],1]
            profit[i] = p2-p1  
profit2 = np.cumsum(profit)#把profit做累積
plt.plot(profit2)
plt.show() #強制先畫出 就不會合起來
ans1 = profit2[-1]  #累積總獲利
ans2 = np.sum(profit>0) / len(profit) #>0為勝
ans3 = np.mean(profit[profit>0])
ans4 = np.mean(profit[profit<=0])
plt.hist(profit,bins=100) #切成100等分
plt.show()
#174筆為沒有買的 =>沒有買profit=0 =>算輸
nobuytimes=0
profit = profit.tolist()
for i in range(len(profit)):
    if(profit[i].count(0)==1):
        nobuytimes+=1 