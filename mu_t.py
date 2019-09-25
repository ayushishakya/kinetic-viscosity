#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:38:33 2019

@author: ayushi
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:47:15 2019

@author: SUNIL
"""

import pandas as pd
import os
from sympy import *
import numpy as np

grid_df = pd.read_csv('dns.csv', header =None)
data = pd.DataFrame(columns = ['X', 'Y', 'uV_mean', 'ux', 'uy', 'mu_t'])
sum=0
dx = 0.5
dy = 0.5
time_steps = 100

'''
mean_df = pd.read_csv('Mean_flow_values.csv')
new_data = pd.DataFrame(columns = ['Uf', 'Vf', 'Wf','Pf'])

for filename in os.listdir(os.getcwd()+'/dns data'):
    df = pd.read_csv(os.getcwd()+'/dns data/'+filename)
    new_data = pd.DataFrame(columns = ['Uf', 'Vf', 'Wf','Pf'])
    for i in range(0, 14400):
        Uf=df.iloc[i,0]-mean_df.iloc[i,0]
        Vf=df.iloc[i,1]-mean_df.iloc[i,1]
        Wf=df.iloc[i,2]-mean_df.iloc[i,2]
        Pf=df.iloc[i,3]-mean_df.iloc[i,3]
        new_data.loc[len(new_data)] = Uf, Vf, Wf,Pf
    new_data.to_csv(os.getcwd()+'/fluctuation/'+filename, index=False)
    print(os.getcwd()+'/fluctuation/'+filename)'''


for i in range(8001, 14400):
    sum=0
    for filename in os.listdir(os.getcwd()):
        df = pd.read_csv(os.getcwd()+'/'+filename)
        sum = sum+(df.iloc[i,1]*df.iloc[i,2])
        if (i==0):
            uy = (df.iloc[i+1,1]-df.iloc[i,1])/(2*dy)
            vx = (df.iloc[i+1,2]-df.iloc[i,2])/(2*dx)
        elif(i==len(grid_df)-1):
            uy = (df.iloc[i-1,1]-df.iloc[i,1])/(2*dy)
            vx = (df.iloc[i-1,2]-df.iloc[i,2])/(2*dx)
        else:
            uy = (df.iloc[i+1,1]-df.iloc[i-1,1])/(2*dy)
            vx = (df.iloc[i+1,2]-df.iloc[i-1,2])/(2*dx)
    uv_mean = sum/time_steps
    mu_t = uv_mean/(uy+vx)
    X,Y = grid_df.iloc[i,0], grid_df.iloc[i,1]
    data.loc[len(data)] = X, Y, uv_mean,uy,vx, mu_t
    print(str(i) + " Done")

data.to_csv('data.csv', sep='\t')