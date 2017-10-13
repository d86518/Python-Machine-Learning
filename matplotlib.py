# -*- coding: utf-8 -*-
# -*- coding: big5 -*-
"""
Created on Sun Oct  1 12:59:45 2017

@author: 黃大祐
"""

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(1,5)
y = [] 
z = []
t = []
l = []
for i in range(1,5):
    y.append(math.exp(i))
    z.append(2**i)
    t.append(i**2)
    l.append(i)
sv = plt.gcf()
plt.plot(x,y,'b--',marker='+',label="$e^x$")
plt.plot(x,z,'r',linestyle='--',marker='*',label="$2^x$",linewidth=2)  
plt.plot(x,t,'g',marker='+',label="$x^2$")
plt.plot(x,l,'black',marker='*',label="$x$")
#plt.xlim(0.5,4.5) 
#plt.ylim(-1.5,1.5)
plt.legend(loc=2)
plt.xlabel("x-axis") 
plt.ylabel("y-axis") 
plt.title("X growth") 
plt.show() 
sv.savefig('example2', dpi=600)