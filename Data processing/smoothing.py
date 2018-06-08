"""
This script attempts to produce a data collapse for height PDFs

Processing pile height time series.
Script does the following:-
    (a) Smooths heights
"""
import os
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt


#import window as win

def rectangle(data, W = 25):
    """
    Data is the array of data to smooth, 2W + 1 is the window length.
    """
    running_avg = np.array([])

    for i in np.arange(0,len(data)) :
        tmin = (i - W)
        if tmin < 0 :
            tmin = 0

        tmax = (i + W) 
        if tmax > len(data) :
            tmax = len(data)
        running_avg = np.append(running_avg, np.average(data[tmin:tmax]))
        
    return running_avg


height1 = np.loadtxt('h_L1_1e6g')
height2 = np.loadtxt('h_L2_1e6g')
height3 = np.loadtxt('h_L8_1e6g')
height4 = np.loadtxt('h_L16_1e6g')
height5 = np.loadtxt('h_L32_1e6g')
height6 = np.loadtxt('h_L64_1e6g')
height7 = np.loadtxt('h_L128_1e6g')
height8 = np.loadtxt('h_L256_1e6g')
height9 = np.loadtxt('h_L512_1e6g')

#time = np.arange(0,len(height1))

smooth_h1 = rectangle(height1, 50)
smooth_h2 = rectangle(height2, 50)
smooth_h3 = rectangle(height3, 50)
smooth_h4 = rectangle(height4, 50)
smooth_h5 = rectangle(height5, 50)
smooth_h6 = rectangle(height6, 50)
smooth_h7 = rectangle(height7, 50)
smooth_h8 = rectangle(height8, 50)
smooth_h9 = rectangle(height9, 50)

np.savetxt('smoothL1.txt', smooth_h1)
np.savetxt('smoothL2.txt', smooth_h2)
np.savetxt('smoothL8.txt', smooth_h3)
np.savetxt('smoothL16.txt', smooth_h4)
np.savetxt('smoothL32.txt', smooth_h5)
np.savetxt('smoothL64.txt', smooth_h6)
np.savetxt('smoothL128.txt', smooth_h7)
np.savetxt('smoothL256.txt', smooth_h8)
np.savetxt('smoothL512.txt', smooth_h9)

print "done"
