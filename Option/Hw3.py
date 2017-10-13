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
    
def Bisection2(left,right,S,L,T,r,call,iteration):
    center = (left+right)/2
    if(iteration==0):
        return center
    if((blscall(S,L,T,r,left)-call)*(blscall(S,L,T,r,center)-call)<0):
        return Bisection2(left,center,S,L,T,r,call,iteration-1)
    else:
        return Bisection2(center,right,S,L,T,r,call,iteration-1)

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
#sigma = Bisection2(0.0000001,1,S,L,T,r,121.0,1)
#for i in range(20):
#     = [Bisection(0.0000001,1,S,L,T,r,121.0,i)]
print(sigma)
print(blscall(S,L,T,r,sigma))
sigmanew=[Newton(0.5,S,L,T,r,121.0,1),Newton(0.5,S,L,T,r,121.0,2),Newton(0.5,S,L,T,r,121.0,3),Newton(0.5,S,L,T,r,121.0,4),Newton(0.5,S,L,T,r,121.0,5),Newton(0.5,S,L,T,r,121.0,6),Newton(0.5,S,L,T,r,121.0,7),Newton(0.5,S,L,T,r,121.0,8),Newton(0.5,S,L,T,r,121.0,9),Newton(0.5,S,L,T,r,121.0,10),Newton(0.5,S,L,T,r,121.0,11),Newton(0.5,S,L,T,r,121.0,12),Newton(0.5,S,L,T,r,121.0,13),Newton(0.5,S,L,T,r,121.0,14),Newton(0.5,S,L,T,r,121.0,15),Newton(0.5,S,L,T,r,121.0,16),Newton(0.5,S,L,T,r,121.0,17),Newton(0.5,S,L,T,r,121.0,18),Newton(0.5,S,L,T,r,121.0,18),Newton(0.5,S,L,T,r,121.0,19)]
sigmabis=[Bisection2(0.0000001,1,S,L,T,r,121.0,1),Bisection2(0.0000001,1,S,L,T,r,121.0,2),Bisection2(0.0000001,1,S,L,T,r,121.0,3),Bisection2(0.0000001,1,S,L,T,r,121.0,4),Bisection2(0.0000001,1,S,L,T,r,121.0,5),Bisection2(0.0000001,1,S,L,T,r,121.0,6),Bisection2(0.0000001,1,S,L,T,r,121.0,7),Bisection2(0.0000001,1,S,L,T,r,121.0,8),Bisection2(0.0000001,1,S,L,T,r,121.0,9),Bisection2(0.0000001,1,S,L,T,r,121.0,10),Bisection2(0.0000001,1,S,L,T,r,121.0,11),Bisection2(0.0000001,1,S,L,T,r,121.0,12),Bisection2(0.0000001,1,S,L,T,r,121.0,13),Bisection2(0.0000001,1,S,L,T,r,121.0,14),Bisection2(0.0000001,1,S,L,T,r,121.0,15),Bisection2(0.0000001,1,S,L,T,r,121.0,16),Bisection2(0.0000001,1,S,L,T,r,121.0,17),Bisection2(0.0000001,1,S,L,T,r,121.0,18),Bisection2(0.0000001,1,S,L,T,r,121.0,19)]
plt.plot(sigmanew)
plt.plot(sigmabis)