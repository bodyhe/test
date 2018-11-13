import pandas as pd
import scipy.io as scio
from collections import Counter
from test import *
# from ecg import *
import plotting
data=pd.read_csv('D:\\Deep_learning\\training2017\\REFERENCE.csv')
dic_label=data.to_dict()['N']
dic_filename=data.to_dict()['A00001']
CPI_LABEL = data['N']
S_LABEL_COUNT={}   #统计各类别及总数目
sum_N=[]           # N类中的文件名
sum_A=[]           # A类中的文件名
sum_O=[]           # O类中的文件名
sum_ohters=[]      # others类中的文件名
for featVec in CPI_LABEL:
    currentLabel = featVec[-1]
    if currentLabel not in S_LABEL_COUNT.keys():
        S_LABEL_COUNT[currentLabel] = 0
    S_LABEL_COUNT[currentLabel] += 1

for i in range(0,len(CPI_LABEL)-1):
    if dic_label[i]=='N':
        sum_N.append(dic_filename[i])
    elif dic_label[i]=='A':
        sum_A.append(dic_filename[i])
    elif dic_label[i]=='O':
        sum_O.append(dic_filename[i])
    elif dic_label[i]=='~':
        sum_ohters.append(dic_filename[i])

currentFile={'N':sum_N,'A':sum_A,'o':sum_O,'~':sum_ohters}

# 去除不能读取的文件
sum_N.remove('A00598')
sum_N.remove('A01113')
sum_N.remove('A01211')
sum_N.remove('A01269')
sum_N.remove('A03626')
sum_N.remove('A04448')
sum_N.remove('A05887')
sum_N.remove('A06384')

sum_A.remove('A06431')
sum_A.remove('A07496')

sum_O.remove('A00698')
sum_O.remove('A03014')
sum_O.remove('A04322')
sum_O.remove('A05325')
sum_O.remove('A05818')
sum_O.remove('A06135')

sum_ohters.remove('A05507')


