# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:58:19 2017

@author: 黃大祐
"""
#每月第三個禮拜三過了後 會是下個月的報價 所以每天刷比較保險
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ansbest = 0
df = pd.read_csv('TXF20112015.csv',sep=',',header=None)
TAIEX = df.values  #資料取出為dataframe 變為nrowX5col的array
#0time 1收 2開 3高 4低
tradeday = list(set(TAIEX[:,0]//10000)) #只有前面八碼的日期到日 set讓資料不重複
tradeday.sort()
profit = np.zeros((len(tradeday),1))
for n in range(10,110,10): #m要>=n
    for m in range(10,110,10):
        if(m>=n):
            for i in range(len(tradeday)):
                date = tradeday[i]
                idx = np.nonzero(TAIEX[:,0]//10000==date)[0] #拿出index col=0 那天的第一分鐘(若index=0)
                idx.sort()
                #想設停損為30點############################
                p1=TAIEX[idx[0],2] ##開盤價
                idx2 = np.nonzero(TAIEX[idx,4]>=p1+n)[0] #漲30是我的lose 停損
                idx3 = np.nonzero(TAIEX[idx,3]<=p1-m)[0] #跌30是我的profit 停利
                if(len(idx2)==0 and len(idx3)==0): #沒停損沒停利 用收盤價做
                    p2 = TAIEX[idx[-1],1]
                elif(len(idx3)==0):  #必做停損
                    p2 = TAIEX[idx[idx2[0]],1]  #以第一次撞到為主
                elif(len(idx2)==0):  #必做停利
                    p2 = TAIEX[idx[idx3[0]],1]
                elif(idx2[0]<idx3[0]):
                    p2 = TAIEX[idx[idx2[0]],1]     
                else:
                    p2 = TAIEX[idx[idx3[0]],1]  #停利      
                profit[i] = p2-p1
            profit2 = np.cumsum(profit)#把profit做累積一直存到profit2
            ans1 = profit2[-1]  #最後一筆數值
            if(ans1>ansbest):
                ansbest = ans1
                mbest = m
                nbest = n           
            #mbest=>20  nbest=>20
#                plt.plot(profit2)
#                plt.show() #強制先畫出 就不會合起來
#                ans1 = profit2[-1]  #最後一筆數值
#                ans2 = np.sum(profit>0) / len(profit) #>0為勝
#                ans3 = np.mean(profit[profit>0])
#                ans4 = np.mean(profit[profit<=0])
#                plt.hist(profit,bins=100)
