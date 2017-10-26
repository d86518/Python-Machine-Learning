# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import math
import random
#import random
import matplotlib.pyplot as plt
from sklearn import datasets
iris = datasets.load_iris()

def kmeans(sample,K,maxiter): #跑maxiter次停
    N = sample.shape[0]
    D = sample.shape[1]
    C = np.zeros((K,D))
    L = np.zeros((N,1))
    L1 = np.zeros((N,1))#更新後L1 若與L1相同 暫停用
    dist = np.zeros((N,K))
    idx = random.sample(range(N),K) #範圍為N 跑K群資料 不重複!!!
    C = sample[idx,:] #預設的中心點
    iter = 0
#    wicdbest = 100
    while(iter<maxiter):
        for i in range(K):
            dist[:,i] =np.sum((sample - np.tile(C[i,:],(N,1)))**2,1) #把C的矩陣 變N便
            #針對每一個center copy n次 對檢平方算出距離存到dist
        L1 = np.argmin(dist,1) #argmin 告訴最小值 L1是最小那群
        if(iter>0 and np.array_equal(L,L1)):
            break #相同就break掉
        L = L1
        for i in range(K):#之後Center會隨便坐落 有可能兩邊的群中間沒人投票給他
            idx = np.nonzero(L==i)[0] #L==i的那些人的index取出來
            if(len(idx)>0): #如果有人投票給我 更新center
                C[i,:] = np.mean(sample[idx,:],0) #每條col分別做平均 回傳1xD大小的array裝
        iter += 1
#    Practice 4-2 WICD計算
    wicd = np.sum(np.sqrt(np.sum((sample-C[L,:])**2,1))) #L像一張表0 1 2一直跑 全表摳過來 每個ROW為L的摳出來
    return C,L,wicd
#    wicd 每個sample減自己center的distance留起來

#    np.sum(x,1) 1把整col值sum
#mean std size
G1 = np.random.normal(0,1,(5000,2)) #5000X2的data量 5000row 2col 
G1 = G1+4
G2 = np.random.normal(0,1,(3000,2))
G2[:,1] = G2[:,1]*3 - 3
G=np.append(G1,G2,axis=0)
G3 = np.random.normal(0,1,(2000,2)) 
G3[:,1] = G3[:,1]*4

#逆時針45度
c45 = math.cos(-45/180*math.pi)
s45 = math.sin(-45/180*math.pi)
R = np.array([[c45,-s45],[s45,c45]])
G3 = G3.dot(R)
G3[:,0] = G3[:,0]-4
G3[:,1] = G3[:,1]+6

#G=np.append(G,G3,axis=0)
#plt.plot(G[:,0],G[:,1],'.')
#C,L,wicd = kmeans(G,3,1000)
#G1 = G[L==0,:]
#G2 = G[L==1,:]
#G3 = G[L==2,:]
#
#print(wicd)
#plt.plot(G1[:,0],G1[:,1],'r.',G2[:,0],G2[:,1],'g.',G3[:,0],G3[:,1],'b.',C[:,0],C[:,1],'kx')
#plt.show()
#
#
#
##標準化 np.tile會直接copy出
#G = (G-np.tile(G.mean(0),(G.shape[0],1)))/np.tile(G.std(0),(G.shape[0],1))
#G1 = G[L==0,:]
#G2 = G[L==1,:]
#G3 = G[L==2,:]
#
#print(wicd)
#plt.plot(G1[:,0],G1[:,1],'r.',G2[:,0],G2[:,1],'g.',G3[:,0],G3[:,1],'b.',C[:,0],C[:,1],'kx')
#plt.show()

#避免停在奇怪的分法 Practice 4-3
wicdbest = 100;
wicdbad = 0;
for i in range(10000):
    C,L,wicd = kmeans(iris.data,3,1000)
    if (wicd < wicdbest):
        wicdbest = wicd
    if (wicd > wicdbad):
        wicdbad = wicd
        
plt.plot(iris.data[:,0],iris.data[:,1],'.')
G1 = iris.data[L==0,:]
G2 = iris.data[L==1,:]
G3 = iris.data[L==2,:]
G=np.append(G1,G2,axis=0)
G=np.append(G,G3,axis=0)
plt.plot(G1[:,0],G1[:,1],'r.',G2[:,0],G2[:,1],'g.',G3[:,0],G3[:,1],'b.',C[:,0],C[:,1],'kx')
print(wicdbest)
plt.show()
#normalization

#標準化 Practice 4-1
GG = (G-np.tile(G.mean(0),(G.shape[0],1)))/np.tile(G.std(0),(G.shape[0],1))
G1 = G[L==0,:]
G2 = G[L==1,:]
G3 = G[L==2,:]
plt.plot(G1[:,0],G1[:,1],'r.',G2[:,0],G2[:,1],'g.',G3[:,0],G3[:,1],'b.',C[:,0],C[:,1],'kx')
print(wicd)
plt.show()

##一筆筆標準 跟上面結果一樣
#for i in range(G.shape[i]):
#    meanv = np.mean(G[:,i])
#    std = np.std(G[:,i])
#    G[:,i] = (G[:,i] - meanV)/stdv