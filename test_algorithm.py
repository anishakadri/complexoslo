"""
Anisha Kadri 2017
ak4114@ic.ac.uk

Test for algorithm
Calculates time average of pile heights of systems L=16 and L=32 over t =1e6.
"""
import os
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
os.chdir("/Users/AnishaKadri/Desktop/CompResults")

height4 = np.loadtxt('h_L16b_1e6g')
height5 = np.loadtxt('h_L32b_1e6g')

print "time average across t=1e6 for L=16", np.average(height4)
print "time average across t=1e6 for L=32", np.average(height5)
