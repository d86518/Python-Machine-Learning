# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 19:33:25 2017

@author: USER
"""
import math
#才能寫log
from scipy.stats import norm
import numpy as np
#做矩陣乘法常用
import matplotlib.pyplot as plt

def blscall(S,L,T,r,sigma):
    d1=(math.log(S/L)+(r+0.5*sigma*sigma)*T)/(sigma*math.sqrt(T))
    d2=d1-sigma*math.sqrt(T)    
    return S*norm.cdf(d1)-L*math.exp(-r*T)*norm.cdf(d2)
#cumulative density function    

S=50.0
L=40.0
T=2.0
r=0.08
sigma=0.2

print(blscall(S,L,T,r,sigma))
#買權定價
print(blscall(S,L,T,r,sigma)+L*math.exp(-r*T)-S)
#藉由買賣權平價找出賣權價格
d1=(math.log(S/L)+(r+0.5*sigma*sigma)*T)/(sigma*math.sqrt(T))
print(norm.cdf(d1))
#(Call對股價的變化)
print((blscall(S+0.01,L,T,r,sigma)-blscall(S-0.01,L,T,r,sigma))/0.02)
#沒辦法微分的時候用差分來代替 前後抓一個小delta
#--------------------------------------------------------------
N=100
dt=T/N
P=np.zeros([10000,N+1])
for i in range(10000):
    P[i,0]=S
    for j in range(N):
        P[i,j+1]=P[i,j]*math.exp((r-0.5*sigma*sigma)*dt+np.random.normal(0,1,1)*sigma*math.sqrt(dt))
#        mean是0 標準差是1 只產1個(npnormal)
C=0
#期望值
for i in range(10000):
    if(P[i,100]>L):
#    算模擬獲利最後一天的期望值 再換回今天
        C +=(P[i,100]-L)/10000
print(C*math.exp(-r*T))
#回到今天的價格
plt.xlabel("Time") 
plt.ylabel("Price")
for i in range(200):
    plt.plot(P[i])