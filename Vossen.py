# Program      : Euler's method
# Author       : MOOC team Mathematical Modelling Basics/wessel
# Created      : April, 2017

import numpy as np
import matplotlib.pyplot as plt

print("Solution for dP/dt = (b - c*x)*x - (d + a*x)*x ")
# Initializations

Dt = 1                                # timestep Delta t
P_init = 20                             # initial population 
t_init = 0                              # initial time
t_end = 800                               # stopping time
n_steps = int(round((t_end-t_init)/Dt)) # total number of timesteps

t_arr = np.zeros(n_steps + 1)           # create an array of zeros for t
P_arr = np.zeros(n_steps + 1)           # create an array of zeros for P
t_arr[0] = t_init                       # add the initial P to the array
P_arr[0] = P_init                       # add the initial t to the array

# Euler's method
"""
b = 0.1
c = 0.1/700
d = 0.0002737
a = 0.0002737/700
"""
b = 0.0245
c = 0
d = 0.0003044
a = 0.000000063
M = 919996

"""
def derif(x):
	return (b - c*x)*x - (d + a*x)*x
    """
def derif(x):
    return (b-d)*x*(1-x/M)

for i in range (1, n_steps + 1):
    P = P_arr[i-1]
    t = t_arr[i-1]
    dPdt = derif(P)                        # calculate the derivative 
    P_arr[i] = P + Dt*dPdt              # calculate P on the next time step
    t_arr[i] = t + Dt                   # adding the new t-value to the list

# Plot the results

fig = plt.figure()                      # create figure
plt.plot(t_arr, P_arr, linewidth = 4, label="Foxes", color="r")   # plot population vs. time

plt.title('Solution for dPf/dt = Rf*Pf*(1-Pf/Mf)', fontsize = 10)  
plt.xlabel('t (in days)', fontsize = 20)
plt.ylabel('P(t)', fontsize = 20)

plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.grid(True) 
plt.legend()                         # show grid                # define the axes
plt.show()                              # show the plot
# save the figure as .jpg
#fig.savefig('Rainbowfish.jpg', dpi=fig.dpi, bbox_inches = "tight")