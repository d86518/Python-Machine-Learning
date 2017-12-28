# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 19:50:30 2017

@author: USER
"""

import numpy as np
D = np.load('PCA_data.npy')

def PCAtrain(D,R):
    M,F = D.shape
    meanv = np.mean(D,axis=0)
    D2 = D-np.matlib.repmat(meanv,M,1)
    C = np.dot(np.transpose(D2),D2)
    EValue,Evector = np.linalg.eig(C)
    #eigenvalue小 維度小 所含資訊量低 丟掉沒關係
    EV2 = np.cumsum(EValue)/np.sum(EValue)
    num = np.where(EV2>=R)[0][0]+1
    return meanv,Evector[:,range(num)]

def PCAtest(D,meanv,W):
    M,F = D.shape
    D2 = D-np.matlib.repmat(meanv,M,1)
    D3 = np.dot(D2,W)
    return D3

meanv,W = PCAtrain(D,0.9)
newD = PCAtest(D,meanv,W)