# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 04:26:45 2017

@author: 黃大祐
"""

f = open('ans.txt','r')
ans=f.read()
ans=ans.split()

f = open('ans02.txt','r')
ans02=f.read()
ans02=ans02.split()

f = open('ans12.txt','r')
ans12=f.read()
ans12=ans12.split()

error=0
for i in range(150):
     if(int(ans[i]+ans02[i]+ans12[i])<2):
         error+=1
#error計算為50  表示有50筆資料為錯誤
print("錯誤率為",error/150)