"""
Anisha Kadri 2017
ak4114@ic.ac.uk
This script creates a log data binning of the avalanche probabilities
"""

import os
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt


size = np.loadtxt('svals256A.txt')
frequency = np.loadtxt('sfreq256A.txt')
prob =  frequency /  np.sum(frequency)/Users/AnishaKadri/Desktop/Complexity/KadriA_ComplexityCode/Data processing/av_prob_binned.py

s256 = np.loadtxt('s_L256_1e6g')[65536:]
bins = np.logspace(1, np.log2(np.max(size)), num = 200, base= 10)
widths = (bins[1:] - bins[:-1])

# Calculate histogram L= 256
hist = np.histogram(s256, bins=bins)
# normalize by bin width
hist_norm = hist[0]/(widths*0.9e6)

# plot it!

#plt.loglog(size,prob, '.', alpha = 0.2, label = 'raw 256')
plt.plot(bins[:-1], hist_norm, '-', label = 'L = 256')
plt.xscale('log')
plt.yscale('log')
plt.show()
#

s128 = np.loadtxt('s_L128_1e6g')[16384:]
bins = np.logspace(1, np.log2(np.max(size)), num = 150, base= 10)
widths = (bins[1:] - bins[:-1])

# Calculate histogram L= 128
hist = np.histogram(s128, bins=bins)
# normalize by bin width
hist_norm = hist[0]/(widths*4e6)

# plot it!

#plt.loglog(size,prob, '.', alpha = 0.2)
plt.plot(bins[:-1], hist_norm, '-', label = 'L=128')
plt.xscale('log')
plt.yscale('log')
plt.show()

s64 = np.loadtxt('s_L64_1e6g')[4096:]
bins = np.logspace(1, np.log2(np.max(size)), num = 150, base= 10)
widths = (bins[1:] - bins[:-1])

# Calculate histogram L= 64
hist = np.histogram(s64, bins=bins)
# normalize by bin width
hist_norm = hist[0]/(widths*4e6)
hist_norm = hist_norm *((bins)**1.55)
# plot it!

#plt.loglog(size,prob, '.', alpha = 0.2)
plt.plot(bins[:-1], hist_norm, '-', label = 'L = 64')
plt.xscale('log')
plt.yscale('log')
    

plt.xlabel('Avalanche size / s')
plt.ylabel('Probability')
plt.legend()
plt.show()
print "done"