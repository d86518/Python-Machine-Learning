# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:02:04 2017

@author: USER
"""
import math
from scipy.stats import norm
import matplotlib.pyplot as plt
def blscall(S,L,T,r,sigma):
    d1 = (math.log(S/L)+(r+0.5*sigma*sigma)*T)/(sigma*math.sqrt(T))
    d2 = d1- sigma*math.sqrt(T)
    return S*norm.cdf(d1)-L*math.exp(-r*T)*norm.cdf(d2)

def Bisection(left,right,S,L,T,r,call,error):
    center = (left+right)/2
    if((right-left)/2<error):
        return center
    if((blscall(S,L,T,r,left)-call)*(blscall(S,L,T,r,center)-call)<0):
        return Bisection(left,center,S,L,T,r,call,error)
    else:
        return Bisection(center,right,S,L,T,r,call,error)
    
def Newton(initsigma,S,L,T,r,call,iteration):
    sigma = initsigma
    for i in range(iteration):
        fx = blscall(S,L,T,r,sigma)-call
        fx2 = (blscall(S,L,T,r,sigma+0.00000001)-blscall(S,L,T,r,sigma-0.00000001))/0.00000002;
        sigma = sigma - fx/fx2
    return sigma

S = 10326.68
L = 10300.0
T = 21.0/365
r = 0.01065
sigma = 0.10508

print(blscall(S,L,T,r,sigma))
sigma = Bisection(0.0000001,1,S,L,T,r,121.0,0.000000001)
print(sigma)
print(blscall(S,L,T,r,sigma))
print(Newton(0.5,S,L,T,r,121.0,10))

smile=[Bisection(0.0000001,1,S,10000,T,r,354.0,0.000000001),
       Bisection(0.0000001,1,S,10100,T,r,267.0,0.000000001),
       Bisection(0.0000001,1,S,10200,T,r,187.0,0.000000001),
       Bisection(0.0000001,1,S,10300,T,r,121.0,0.000000001),
       Bisection(0.0000001,1,S,10400,T,r,69.0,0.000000001),
       Bisection(0.0000001,1,S,10500,T,r,34.0,0.000000001),
       Bisection(0.0000001,1,S,10600,T,r,14.50,0.000000001),
       Bisection(0.0000001,1,S,10700,T,r,5.90,0.000000001)]
price=[10000,10100,10200,10300,10400,10500,10600,10800]
for i in range(8):
    print(smile[i])
    plt.plot(price,smile)
    