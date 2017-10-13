# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 19:50:58 2017

@author: USER
"""

import math
import numpy as np

from sklearn import datasets
iris = datasets.load_iris()

def entropy(p1,n1):
    if(p1==0 and n1==0):
        return 1
    value = 0
    pp = p1/(p1+n1)
    pn = n1/(p1+n1)
    if(pp>0):
        value -= pp*math.log2(pp)
    if(pn>0):
        value -= pn*math.log2(pn)
    return value

def IG(p1,n1,p2,n2):
    num = p1+n1+p2+n2
    num1 = p1+n1
    num2 = p2+n2
    return entropy(p1+p2,n1+n2)-num1/num*entropy(p1,n1)-num2/num*entropy(p2,n2)

#data = np.loadtxt('PlayTennis.txt',usecols=range(5),dtype=int)
#feature = data[:,0:4]
#target = data[:,4]-1

##1,2建樹
#feature1 = iris.data[50:150,]
#target1 = iris.target[50:150,]
#
##0,2建樹
#feature2 = np.vstack((iris.data[0:50,],iris.data[100:150,]))  
#target2 = np.hstack((iris.target[0:50,],iris.target[100:150,]))

rightc=0
wrongc=0
ans=[]
#0,1建樹
#irisall = np.vstack(iris.data,iris.target)
f = open('ans01.txt', 'w')
for tr in range(150):
    feature0=np.delete(iris.data,tr,0)
    target0=np.delete(iris.target,tr,0)
    if(tr<100):
        featuretree0 = feature0[0:99,]
        targettree0 = target0[0:99,]
    else: 
        featuretree0 = feature0[0:100,]
        targettree0 = target0[0:100,]
    #target=0,1的樹
    
    #target=1,2的樹
    if(tr<50):
        featuretree1 = feature0[49:149,] 
        targettree1 = target0[49:149,]
    else:
        featuretree1 = feature0[50:149,]
        targettree1 = target0[50:149,]
    
    #target=0,2的樹
    if(tr<50):
        featuretree2 = np.vstack((feature0[0:49,],feature0[99:149,]))
        targettree2 = np.hstack((target0[0:49,],target0[99:149,]))
    elif((tr>=100) and (tr<=150)):
        featuretree2 = np.vstack((feature0[0:50,],feature0[100:149,]))
        targettree2 = np.hstack((target0[0:50,],target0[100:149,]))
    else:
        featuretree2 = np.vstack((feature0[0:50,],feature0[100:150,]))
        targettree2 = np.hstack((target0[0:50,],target0[100:150,]))
       
        #target0,1跑出來的model
    node = dict()
    node['data'] = range(len(targettree0))
    Tree = [];
    Tree.append(node)
    t = 0
    while(t<len(Tree)):
        idx = Tree[t]['data']
        if(sum(targettree0[idx])==0):
            Tree[t]['leaf']=1
            Tree[t]['decision']=0
        elif(sum(targettree0[idx])==len(idx)):
            Tree[t]['leaf']=1
            Tree[t]['decision']=1
        else:
            bestIG = 0
            for i in range(featuretree0.shape[1]):
                pool = list(set(featuretree0[idx,i]))
                for j in range(len(pool)-1):
                    thres = (pool[j]+pool[j+1])/2
                    G1 = []
                    G2 = []
                    for k in idx:
                        if(featuretree0[k,i]<=thres):
                            G1.append(k)
                        else:
                            G2.append(k)
                    thisIG = IG(sum(targettree0[G1]==1),sum(targettree0[G1]==0),sum(targettree0[G2]==1),sum(targettree0[G2]==0))
                    if(thisIG>bestIG):
                        bestIG = thisIG
                        bestG1 = G1
                        bestG2 = G2
                        bestthres = thres
                        bestf = i
            if(bestIG>0):
                Tree[t]['leaf']=0
                Tree[t]['selectf']=bestf
                Tree[t]['threshold']=bestthres
                Tree[t]['child']=[len(Tree),len(Tree)+1]
                node = dict()
                node['data']=bestG1
                Tree.append(node)
                node = dict()
                node['data']=bestG2
                Tree.append(node)
            else:
                Tree[t]['leaf']=1
                if(sum(targettree0[idx]==1)>sum(targettree0[idx]==0)):
                    Tree[t]['decision']=1
                else:
                    Tree[t]['decision']=0
        t+=1
        
    test_feature = iris.data[tr,:]
    now = 0
    while(Tree[now]['leaf']==0):
        bestf = Tree[now]['selectf']
        thres = Tree[now]['threshold']
        if(test_feature[bestf]<=thres):
            now = Tree[now]['child'][0]
        else:
            now = Tree[now]['child'][1]
    print(iris.target[tr],Tree[now]['decision'])
    f = open('ans01.txt', 'a')
    if((iris.target[tr])==(Tree[now]['decision'])):
        f.write("1 ")
    else:
        f.write("0 ")
print("-------------------")
#--------------------------------------------------------------------------------------------------