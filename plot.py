import pandas as pd
import sys

#from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt

# plt.style.use('seaborn-poster')

# t = [0, 2, 4, 6, 8, 10]
# v = [1, 2, 5, 3, 7, 9 ]

# # use bc_type = 'natural' adds the constraints as we described above
# # f = CubicSpline(t, v, bc_type='natural')
# # x_new = np.linspace(0, 10, 100)
# # y_new = f(x_new)

# plt.figure(figsize = (10,8))
# #plt.plot(x_new, y_new, 'b')
# plt.plot(t, v, 'ro')
# plt.title('Gelila Sahle')
# plt.xlabel('Time (s)')
# plt.ylabel('Velocity (ft/s)')
# plt.show()

# Gelila = np.array([0,0,0,0,13, 0, 1, 5, 0, 24])
# Olu = np.array([0,0,0,0,0, 1, 0, 0, 3, 27])
# Eshaan = np.array([0,0,0,0,0, 0, 4, 0, 0, 9])

Gelila = np.array([2,0,3,0,1,5,2,4])
Olu = np.array([5,0,0,1,1,0,2,5])
Eshaan = np.array([0,2,0,0,0,0,3,0])

# # #DP = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
# # #REC = [4, 8, 33, 81, 212, 328, 1179, 1603, 2204, 4523]

# # DP = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
# # REC = [0, 0, 0, 1, 2, 6, 22, 182, 1403, 10688]

X_axis = ['20','21','25','29','31','1','2','3']

#X_axis = [6, 9, 12, 15, 18, 21, 24, 27, 30, 33]

plt.plot( X_axis, Gelila, label = 'Gelila', color='blue')
plt.plot(X_axis, Olu, label = 'Oluwamayowa', color='green')
plt.plot( X_axis, Eshaan, label = 'Eshaan', color='purple')
plt.xlabel("Timeline (Dates)")
plt.ylabel("Number of daily posts")
plt.legend()
plt.show()
