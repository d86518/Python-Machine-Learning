# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import math
import matplotlib.pyplot as plt
def f(t,tc,s):
    return (tc-t)**s
                
def F2(t,A,B,C,tc,s,w,phi):
    return A+B*(tc-t)**s*(1+C*np.cos(w*np.log(tc-t)+phi))+np.random.normal(0,1)
def E(b,A,B,C,t,tc,s,w,phi):
    return np.sum(abs(F2(t,A,B,C,tc,s,w,phi)-b))

def g(t,tc,s,w,phi):
    return (tc-t)**s*np.cos(w*np.log(tc-t)+phi)   
n = 1000
b = np.zeros((n,1))
A3 = np.zeros((n,5))

data = np.loadtxt('Bubble.txt',usecols=range(2),dtype=float)
b = np.log(data[:,1]) 
t = np.arange(1,len(b)+1)

pop = np.random.randint(0,2,(1000,29))
fit = np.zeros((1000,1))
for generation in range(10):
    print(generation)
    for i in range(1000):
        gene = pop[i,:]
        tc = (np.sum(2**np.array(range(5))*gene[0:5])+579)
        s = np.sum(2**np.array(range(10))*gene[5:15])/1023
        w = np.sum(2**np.array(range(4))*gene[15:19])
        phi = ((np.sum(2**np.array(range(10)*gene[19:29])))%(2*math.pi))
        
        A3 = np.zeros((len(t),3))
        time = math.ceil(tc-1)
        A3p = A3[:time]
        bp = b[:time]
        tp = t[:time]
        A3[:,0] = f(t,tc,s)
        A3[:,1] = g(t,tc,s,w,phi)
        A3[:,2] = 1
        x = np.linalg.lstsq(A3p,bp)[0]
        B,C,A=x
        fit[i]=E(bp,tp,A,B,C,tc,s,w,phi)
    sortf = np.argsort(fit[:,0])
    pop = pop[sortf,:]
    for i in range(100,1000):
        fid = np.random.randint(0,100)
        mid = np.random.randint(0,100)
        while(mid==fid):
            mid = np.random.randint(0,100)
        mask = np.random.randint(0,2,(1,29))
        son = pop[mid,:]
        father = pop[fid,:]
        son[mask[0,:]==1]=father[mask[0,:]==1]
        pop[i,:] = son
    for i in range(100):
        m = np.random.randint(0,1000)
        n = np.random.randint(0,29)
        if(pop[m,n]==0):
            pop[m,n]=1
        else:
            pop[m,n]=0


for i in range(1000):
    gene = pop[i,:]
    tc = (np.sum(2**np.array(range(5))*gene[0:5])+579)
    s = np.sum(2**np.array(range(10))*gene[5:15])/1023
    w = np.sum(2**np.array(range(4))*gene[15:19])
    phi = ((np.sum(2**np.array(range(10)*gene[19:29])))%(2*math.pi))
    A3 = np.zeros((len(t),3))
    time = math.ceil(tc-1)
    A3p = A3[:time]
    bp = b[:time]
    tp = t[:time]
    A3[:,0] = f(t,tc,s)
    A3[:,1] = g(t,tc,s,w,phi)
    A3[:,2] = 1
    x = np.linalg.lstsq(A3p,bp)[0]
    B,C,A=x
    fit[i]=E(bp,tp,A,B,C,tc,s,w,phi)
sortf = np.argsort(fit[:,0])
pop = pop[sortf,:]

gene = pop[0,:]
tc = (np.sum(2**np.array(range(5))*gene[0:5])+579)
s = np.sum(2**np.array(range(10))*gene[5:15])/1023
w = np.sum(2**np.array(range(4))*gene[15:19])
phi = ((np.sum(2**np.array(range(10)*gene[19:29])))%(2*math.pi))
    
A3 = np.zeros((len(t),3))
time = math.ceil(tc-1)
A3p = A3[:time]
bp = b[:time]
tp = t[:time]
A3[:,0] = f(t,tc,s)
A3[:,1] = g(t,tc,s,w,phi)
A3[:,2] = 1
x = np.linalg.lstsq(A3p,bp)[0]
B,C,A=x
        
p=A+B*(tc-t)**s*(1+C*np.cos(w*np.log(tc-t)+phi))
plt.plot(p)
plt.plot(b)
#plt.show()

Bubble = p-b
#plt.plot(data)
#plt.plot(Bubble)

    

