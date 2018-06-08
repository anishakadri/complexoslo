"""
Anisha Kadri 2017
ak4114@ic.ac.uk

This script contains the main algorithm for the Oslo Model.
It measurements a height time series and an avalanche size time series 
for specified system size (L) and time (t).
The values are saved as an array at the end.
"""

import os
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt


#for L in [16, 32, 64, 128, 256]: #choose not to loop for time convenience
L= 512 #system size 
sites = np.arange(0, L)
h = np.zeros(L) #heights at different sites, can be uncommented for plotting purposes
z = np.zeros(L)


thresholds = [2.0,1.0]
probabilities = [0.5,0.5] 
z_th = rand.choice(thresholds, L,  p= probabilities) 

time = 1e6 #time = no. of grains added

total_height = np.array([0])
av_size = np.array([0])

#Drive Mechanism

for t in np.arange(0, time):
    h[0] += 1
    z[0] += 1
    
    s = 0 
    #Relaxation Mechanism
    if L == 1:
        while z[0] > z_th[0]:
            h[0] -= 1
            z[0] -= 1 
            z_th[0] = rand.choice(thresholds, p= probabilities)
            s += 1	    
                
    else:
        relax_pos = np.array([0])
        while len(relax_pos) > 0:
            x = np.min(relax_pos)
            relax_pos = relax_pos[relax_pos != x]
            
            for i in sites[x:L]:
                if z[i] > z_th[i]:
                    relax_pos = np.append(relax_pos, [i])
                    z_th[i] = rand.choice(thresholds, p= probabilities)
                    s += 1
                    if i == 0:
	               h[0] -= 1
	               #h[1] += 1
	               z[0] -= 2 
	               z[1] += 1
	               
	            elif i == (L-1):
	               #h[L-1] -= 1
	               z[L-1] -= 1 
	               z[L-2] += 1
	           
	            else:
	               #h[i] -= 1
	               #h[i+1] += 1
	               z[i] -= 2
	               z[i+1] += 1
	               z[i-1] += 1
	           
    av_size = np.append(av_size, s)   	    
    total_height = np.append(total_height, h[0])

#print av_size
#print total_height
np.savetxt('h_L512_1e6g', total_height)
np.savetxt('s_L512_1e6g', av_size)
print "done"