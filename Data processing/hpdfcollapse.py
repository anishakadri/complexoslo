"""
Anisha Kadri 2017
ak4114@ic.ac.uk

This script attempts to produce a data collapse for height PDFs
"""

import os
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt


h32 = np.loadtxt('smoothL32.txt')[1024:]
h64 = np.loadtxt('smoothL64.txt')[4096:]
h128 = np.loadtxt('smoothL128.txt')[16384:]
h256 = np.loadtxt('smoothL256.txt')[65536:]
h512 = np.loadtxt('smoothL512.txt')[262144:]

bins = np.linspace(min(h512), max(h512), 50)  
widths = (bins[1:] - bins[:-1])/ (512** 0.101 )

# Calculate histogram
hist = np.histogram(h512, bins=bins)
# normalize by bin width
hist_norm = (hist[0]/widths)

# plot it!
plt.plot(bins[:-1], hist_norm, '-', label = 'L = 512')
plt.show()

#L=256
bins = np.linspace(min(h256), max(h256), 50)  
hist = np.histogram(h256, bins=bins)
for i in np.arange(0, len(bins)):
    bins[i] = (bins[i]- 1.75*(256))*(256**- 0.101)
widths = (bins[1:] - bins[:-1])/ (256** 0.101 )
hist_norm = (hist[0]/widths)
plt.plot(bins[:-1], hist_norm, '-', label = 'L = 256')
plt.show()

#L=128
bins = np.linspace(min(h128), max(h128), 50)  
hist = np.histogram(h128, bins=bins)

for i in np.arange(0, len(bins)):
    bins[i] = (bins[i]- 1.75*(128))*(128**- 0.101)
widths = (bins[1:] - bins[:-1])/ (128** 0.101 )
hist_norm = (hist[0]/widths)
plt.plot(bins[:-1], hist_norm, '-', label = 'L = 128')
plt.show()

#L=64
bins = np.linspace(min(h64), max(h64), 50)  

hist = np.histogram(h64, bins=bins)
for i in np.arange(0, len(bins)):
    bins[i] = (bins[i]- 1.75*(128))*(128**- 0.101)
widths = (bins[1:] - bins[:-1])/(64** 0.101 )
hist_norm = (hist[0]/widths)
plt.plot(bins[:-1], hist_norm, '-', label = 'L = 64')
plt.show()

#L=32
bins = np.linspace(min(h32), max(h32), 50)  

hist = np.histogram(h32, bins=bins)
for i in np.arange(0, len(bins)):
    bins[i] = (bins[i]- 1.75*(128))*(128**- 0.101)
widths = (bins[1:] - bins[:-1])/ (32** 0.101 )
hist_norm = (hist[0]/widths)
plt.plot(bins[:-1], hist_norm, '-', label = 'L = 32')




for i in np.arange(0, len(h512)):
    h512[i] = (h512[i]- 1.75*(512))*(512**- 0.101
)

plt.ylabel('Probability density')
plt.xlabel('height values')
plt.legend()
plt.show()
print "complete"