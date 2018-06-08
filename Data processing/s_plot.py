"""
Anisha Kadri 2017
ak4114@ic.ac.uk

Plots an avalanche time series for L= 128 in its steady state.
"""
import os
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

av4 = np.loadtxt('s_L128_1e6g')
av4 = av4[323000:330000]
av4 = av4/np.max(av4)
time = np.arange(323000,330000)

plt.plot(time, av4, color ='grey', label = 'L= 128')
plt.ylabel("avalanche size (s/smax)")
plt.xlabel("time/ t (in grains added)")
plt.legend()
plt.show()
