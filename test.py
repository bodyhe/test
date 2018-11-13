import matplotlib.pyplot as plt
import scipy.io as scio
import numpy
dataFile =('D:\\Deep_learning\\training2017\\')+('A00002.mat')
data = scio.loadmat(dataFile)
data_p=data["val"][0]
# fig, ax = plt.subplots()
# ax.plot(data_p)
# plt.show()