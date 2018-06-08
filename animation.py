import os

"""
Anisha Kadri 2017
ak4114@ic.ac.uk
This script creates an animation of height time sequences, 
it was developed as an intuitive test for the algorithm.
"""

import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt


#for L in [16, 32, 64, 128, 256]: #choose not to loop for time convenience
L= 5 #system size
sites = np.arange(0, L)
h = np.zeros(L) #heights at different sites, can be uncommented for plotting purposes
z = np.zeros(L)


thresholds = [2.0,1.0]
probabilities = [0.5,0.5] 
z_th = rand.choice(thresholds, L,  p= probabilities) 

time = 100 #time = no. of grains added

#Drive Mechanism
plt.ion()
plt.pause(5)

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
    plt.clf()
        plt.ylabel('height')
        plt.xlabel('site number')
        plt.title('Oslo model')
        plt.bar(site_index, h, align='center', alpha=0.5)
        plt.xticks(site_index, site_index)
        plt.draw()
        plt.pause(0.25)

print "done"