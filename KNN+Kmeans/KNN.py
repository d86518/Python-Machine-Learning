# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:35:25 2017

@author: USER
"""

#跟我最像的K個人投票，他們說我是誰，我就是誰
#缺點：運算量較大(>decision tree)，需要把所有data留住
#不需要training


import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import datasets
iris = datasets.load_iris()
    

def dist(instance1, instance2, dimension):
    distance = 0
    for x in range(dimension):
        distance += pow((instance1[x] - instance2[x]),2)
    return math.sqrt(distance)
#testdist
#test1 = [2,2,2,'a']
#test2 = [4,4,4,'b']
#distance = dist(test1,test2,3)
#print(repr(distance))

import operator
def neighbor(trainset,testins,k):
    distances = []
    length = len(testins)-1
    for x in range(len(trainset)):
        distan = dist(testins,trainset[x],length)
        distances.append((trainset[x],distan))
#    用operator.itemgetter可以更快取出想排序的元素
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
#trainset = [[2,2,2,'a'],[4,4,4,'b']]
#testins = [5,5,5]
#k=1
#neighbors = neighbor(trainset,testins,1)
#print(neighbors) 
# =>能抓到444b

n1=n2=n3=n4=n5=n6=n7=n8=n9=n10=[]
iriss=counter=[]
irisdata = iris.data
iristarget = iris.target
#轉成依樣格式
lsttarget=[[x] for x in iristarget]
iristest=np.hstack([irisdata,lsttarget])

#z=zero o=one t=two


##拿一筆與其他149筆做KNN
#一個個試 否則資料會重疊的樣子
#for i in range(150): 
#    data=np.delete(iristest,i,0)
#    n1.append(neighbor(data,iristest[i],1))

#for i in range(150): 
#    data=np.delete(iristest,i,0)
#    n2.append(neighbor(data,iristest[i],2))
#
#for i in range(150): 
#    data=np.delete(iristest,i,0)
#    n3.append(neighbor(data,iristest[i],3))
    
#for i in range(150): 
#    data=np.delete(iristest,i,0)
#    n4.append(neighbor(data,iristest[i],4))
#    
#for i in range(150): 
#    data=np.delete(iristest,i,0)
#    n5.append(neighbor(data,iristest[i],5))
    
#for i in range(150): 
#    data=np.delete(iristest,i,0)
#    n6.append(neighbor(data,iristest[i],6))
#    
#for i in range(150): 
#    data=np.delete(iristest,i,0)
#    n7.append(neighbor(data,iristest[i],7))
    
#for i in range(150): 
#    data=np.delete(iristest,i,0)
#    n8.append(neighbor(data,iristest[i],8))
    
#for i in range(150): 
#    data=np.delete(iristest,i,0)
#    n9.append(neighbor(data,iristest[i],9))
    
for i in range(150): 
    data=np.delete(iristest,i,0)
    n10.append(neighbor(data,iristest[i],100))
## 

confusion=np.zeros((3,3))
z1=o1=t1=0

#投票用
c0=c1=c2=0
for i in range(150):
    for j in range(99):
#        print(n2[i][j][4])
        if(n2[i][j][4]==0):
            c0+=1
        elif(n2[i][j][4]==1):    
            c1+=1
        elif(n2[i][j][4]==2):
            c2+=1
    if(c0>c1 and c0>c2):
        counter.append(0)
    elif(c1>c0 and c1>c2):
        counter.append(1)
    elif(c2>c1 and c2>c0):
        counter.append(2)
    else:
        counter.append(3)
    c0=c1=c2=0
        
#填入矩陣
#上面是truth 左邊predict
for i in range(150):
    if(counter[i]==0 and iristarget[i]==0):
        confusion[0][0]+=1
    elif(counter[i]==1 and iristarget[i]==0):
        confusion[1][0]+=1
    elif(counter[i]==2 and iristarget[i]==0):
        confusion[2][0]+=1
    elif(counter[i]==0 and iristarget[i]==1):
        confusion[0][1]+=1
    elif(counter[i]==1 and iristarget[i]==1):
        confusion[1][1]+=1
    elif(counter[i]==2 and iristarget[i]==1):
        confusion[2][1]+=1
    elif(counter[i]==0 and iristarget[i]==2):
        confusion[0][2]+=1
    elif(counter[i]==1 and iristarget[i]==2):
        confusion[1][2]+=1
    elif(counter[i]==2 and iristarget[i]==2):
        confusion[2][2]+=1
    
#
#for i in range(150):
#    for j in range(1):
#        counter.append(n2[i][j][4])
#        if((n2[i][j][4])==0):
#            z1+=1 
#        elif((n2[i][j][4])==1):    
#            o1+=1
#        elif((n2[i][j][4])==2):    
#            t1+=1

#if((n2[i][j][4])==2
#   c2+=1
#j=0
#for i in range(150):
#        if((neighbors1[i]==iris[j][0:4])[0][0]):
#            print(j)
#        else:
#            j+=1
        
#    neighbors2.append(neighbor(data,iris.data[i],2))
