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
profitstrategy10 = np.zeros((len(tradeday),1))
for i in range(len(tradeday)):
    date = tradeday[i]
    idx = np.nonzero(TAIEX[:,0]//10000==date)[0] #拿出index col=0 那天的第一分鐘(若index=0)
    idx.sort()
    #想設停損為30點############################
    #空 變成越漲越賠 跌才會賺
    p1=TAIEX[idx[0],2] ##開盤價
    idx2 = np.nonzero(TAIEX[idx,4]>=p1+30)[0] #變成漲30是我的lose 
    if(len(idx2)==0): #哪天都沒撞到停損價用
        p2 = TAIEX[idx[-1],1]
    else:
        p2 = TAIEX[idx[idx2[0]],1]  #以第一次撞到為主
    profit[i] = p2-p1
    ###########################################
profit2 = np.cumsum(profit)#把profit做累積
plt.plot(profit2)
plt.show() #強制先畫出 就不會合起來

#總損益點數、勝率(不賠不賺也算輸)、賺錢時平均每次獲利點數、輸錢時平均每次損失點數、繪出每日損益的分布圖

ans1 = profit2[-1]  #最後一筆數值
ans2 = np.sum(profit>0) / len(profit) #>0為勝
ans3 = np.mean(profit[profit>0])
ans4 = np.mean(profit[profit<=0])
plt.hist(profit,bins=100) #切成100等分
plt.show()
#=> 勝率變低合理嗎? 合理=>一停損就出場(原本先虧後彈回來的情況被刪掉了)

