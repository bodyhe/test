import os
import sys
from QRS_util import*
from count import *
import ecg
import pandas
import q_r_s_poitns
def R_test():
	global S, N_Hearts,A_Hearts,O_Hearts,others_Hearts
	SUM_N=0     				#N 心跳数目总和
	SUM_A =0         			#A 心跳数目总和
	SUM_O =0    				#O 心跳数目总和
	SUM_others =0 				#others 心跳数目总和
	# for i in range(0, len(sum_N)):
	# 	dataFile = ('D:\\Deep_learning\\training2017\\') + (sum_N[i]) + ('.mat')
	# 	data_file = scio.loadmat(dataFile)
	# 	data_p = data_file["val"][0]
	# 	res = ecg.ecg(data_p, fs, False)
	# 	SUM_N = SUM_N + S[i]
	# N_Hearts=np.array(N_Hearts)    #N的心跳数据

	# N_Hearts_all = pandas.DataFrame(N_Hearts)
	# N_Hearts_all.to_csv('C:\\Users\\s\\Desktop\\count-hearts\\N\\count_N.csv')

	# for i in range(0, len(sum_A)):
	# 	dataFile = ('D:\\Deep_learning\\training2017\\') + (sum_A[i]) + ('.mat')
	# 	data_file = scio.loadmat(dataFile)
	# 	data_p = data_file["val"][0]
	# 	res = ecg.ecg(data_p, fs, False)
	# 	# SUM_A = SUM_A + S[i]
	# A_Hearts = np.array(A_Hearts)

	# A_Hearts_all = pandas.DataFrame(A_Hearts)
	# A_Hearts_all.to_csv('C:\\Users\\s\\Desktop\\count-hearts\\A\\count_A.csv')

	# for i in range(0, len(sum_O)):
	# 	dataFile = ('D:\\Deep_learning\\training2017\\') + (sum_O[i]) + ('.mat')
	# 	data_file = scio.loadmat(dataFile)
	# 	data_p = data_file["val"][0]
	# 	res = ecg.ecg(data_p, fs, False)
	# 	SUM_O = SUM_O + S[i]
	# O_Hearts = np.array(O_Hearts)

	# O_Hearts_all = pandas.DataFrame(O_Hearts)
	# O_Hearts_all.to_csv('C:\\Users\\s\\Desktop\\count-hearts\\O\\count_O.csv')

	# for i in range(0, len(sum_ohters)):
	# 	dataFile = ('D:\\Deep_learning\\training2017\\') + (sum_ohters[i]) + ('.mat')
	# 	data_file = scio.loadmat(dataFile)
	# 	data_p = data_file["val"][0]
	# 	res = ecg.ecg(data_p, fs, False)
	# 	SUM_others = SUM_others + S[i]
	# others_Hearts = np.array(others_Hearts)

	# others_Hearts_all = pandas.DataFrame(others_Hearts)
	# others_Hearts_all.to_csv('C:\\Users\\s\\Desktop\\count-hearts\\others\\count_others.csv')

	# SUM_ALL = SUM_N + SUM_A + SUM_O + SUM_others   		#所有类别的心跳总和
res = ecg.ecg(data_p,360, True)


def Q_R_S_points():
	fs=1/360
	global Sum   #Sum存放各类所有的心跳的qrs值

	# for i in range(0, len(sum_N)):
	# 	dataFile = ('D:\\Deep_learning\\training2017\\') + (sum_N[i]) + ('.mat')
	# 	data_file = scio.loadmat(dataFile)
	# 	data_p = data_file["val"][0]
	# 	R_peaks, S_pint, Q_point = EKG_QRS_detect(data_p, fs, True, True)
	# 	Summary()
	# Sum = np.array(Sum)
	# qrs = pandas.DataFrame(Sum,columns=['Q','R','S'])
	# qrs.to_csv('C:\\Users\\s\\Desktop\\count-hearts\\N\\count_N_QRS.csv')

	# for i in range(0, len(sum_A)):
	# 	dataFile = ('D:\\Deep_learning\\training2017\\') + (sum_A[i]) + ('.mat')
	# 	data_file = scio.loadmat(dataFile)
	# 	data_p = data_file["val"][0]
	# 	R_peaks, S_pint, Q_point = EKG_QRS_detect(data_p, fs, True, True)
	# 	Summary()
	# Sum = np.array(Sum)
	# qrs = pandas.DataFrame(Sum,columns=['Q','R','S'])
	# qrs.to_csv('C:\\Users\\s\\Desktop\\count-hearts\\A\\count_A_QRS.csv')


	# for i in range(0, len(sum_O)):
	# 	dataFile = ('D:\\Deep_learning\\training2017\\') + (sum_O[i]) + ('.mat')
	# 	data_file = scio.loadmat(dataFile)
	# 	data_p = data_file["val"][0]
	# 	R_peaks, S_pint, Q_point = EKG_QRS_detect(data_p, fs, True, True)
	# 	Summary()
	# qrs = pandas.DataFrame(Sum,columns=['Q','R','S'])
	# qrs.to_csv('C:\\Users\\s\\Desktop\\count-hearts\\O\\count_O_QRS.csv')

	# for i in range(0, len(sum_ohters)):
	# 	dataFile = ('D:\\Deep_learning\\training2017\\') + (sum_ohters[i]) + ('.mat')
	# 	data_file = scio.loadmat(dataFile)
	# 	data_p = data_file["val"][0]
	# 	R_peaks, S_pint, Q_point=EKG_QRS_detect(data_p, fs, True, True)
	# 	Summary()
	# Sum = np.array(Sum)
	# qrs = pandas.DataFrame(Sum,columns=['Q','R','S'])
	# qrs.to_csv('C:\\Users\\s\\Desktop\\count-hearts\\others\\count_others_QRS.csv')

result=q_r_s_poitns.EKG_QRS_detect(data_p,360,True,True)
if __name__ == '__main__':
	Q_R_S_points()
	R_test()