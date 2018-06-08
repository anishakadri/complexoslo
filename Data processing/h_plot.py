"""
Anisha Kadri 2017
ak4114@ic.ac.uk
This script creates an animation of height time sequences, 
it was developed as an intuitive test for the algorithm.

Plots a height time series.
"""

import os
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt


height1 = np.loadtxt('h_L1_1e6g')
height2 = np.loadtxt('h_L2_1e6g')
height3 = np.loadtxt('h_L8_1e6g')
height4 = np.loadtxt('h_L16_1e6g')
height5 = np.loadtxt('h_L32_1e6g')
height6 = np.loadtxt('h_L64_1e6g')
height7 = np.loadtxt('h_L128_1e6g')
height8 = np.loadtxt('h_L256_1e6g')
height9 = np.loadtxt('h_L512_1e6g')

ha = np.delete(height1, 0)
hb = height2[1:]
hc = height3[1:]
hd = height4[1:]
he = height5[1:]
hf = height6[1:]
hg = height7[1:]
hh = height8[1:]
hi = height9[1:]

time = np.arange(0,len(height1))
time1 = np.arange(0, len(ha))

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.plot(time, height1, label= 'L= 1')
plt.plot(time, height2, label = 'L= 2')
plt.plot(time, height3, label = 'L= 8')
plt.plot(time, height4, label = 'L= 16')
plt.plot(time, height5, label = 'L= 32')
plt.plot(time, height6, label = 'L= 64')
plt.plot(time, height7, label = 'L= 128')
plt.plot(time, height8, label = 'L= 256')
plt.plot(time, height9, label = 'L=512')

#plt.loglog(time1, ha, label= 'L= 1')
#plt.loglog(time1, hb, label = 'L= 2')
#plt.loglog(time1, hc, label = 'L= 8')
#plt.loglog(time1, hd, label = 'L= 16')
#plt.loglog(time1, he, label = 'L= 32')
#plt.loglog(time1, hf, label = 'L= 64')
#plt.loglog(time1, hg, label = 'L= 128')
#plt.loglog(time1, hh, label = 'L= 256')
#plt.loglog(time1, hi, label = 'l=512')

plt.ylabel(r'\textbf{height} h(t;L)')
plt.xlabel(r'\textbf{time} (t = grains added)')
plt.legend()
plt.show()
print "data plotted"
