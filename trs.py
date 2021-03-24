# Program      : Euler's method
# Author       : MOOC team Mathematical Modelling Basics
# Created      : April, 2017

import numpy as np
import matplotlib.pyplot as plt

print("Solution for dP/dt = (b - c*x)*x - (d + a*x)*x ")
# Initializations

Dt = 1                                # timestep Delta t
Pk_init = 13                            # initial population rabbits
Pg_init = 0                            # initial population goats
t_init = 0                              # initial time
t_end = 250                               # stopping time
n_steps = int(round((t_end-t_init)/Dt)) # total number of timesteps

t_arr = np.zeros(n_steps + 1)           # create an array of zeros for t
Pk_arr = np.zeros(n_steps + 1)           # create an array of zeros for Pk
Pg_arr = np.zeros(n_steps + 1)          # create an array of zeros for Pg
t_arr[0] = t_init                       # add the initial t to the array
Pk_arr[0] = Pk_init                       # add the initial Pk to the array
Pg_arr[0] = Pg_init                        #add the initial Pg to the array

# Euler's method
bk = 0.1
ck = bk/12395840734
dk = 0.0002737
#ak = 0.0002737/700
ak = 0
bg = 1/150
cg = bg/12395840734
dg = 1/4197.5
#ag = dg/700
ag = 0

def derifk(xk):
	return (0.1-0.000312109862672)*xk


for i in range (1, n_steps + 1):
    Pk = Pk_arr[i-1]
    t = t_arr[i-1]
    dPkdt = derifk(Pk)               # calculate the derivative for rabbits              # calculate the derivative for goats
    Pk_arr[i] = Pk + Dt*dPkdt           # calculate Pk on the next time step         # calculate Pg on the next time step
    t_arr[i] = t + Dt                   # adding the new t-value to the list

# Plot the results

fig = plt.figure()                      # create figure
plt.plot(t_arr, Pk_arr, linewidth = 3, label = "Rabbits")   # plot population vs. time

plt.title('Solution for dP/dt = (0.1-0.000312109862672)P', fontsize = 10)  
plt.xlabel('t (in days)', fontsize = 10)
plt.ylabel('P(t)', fontsize = 10)

plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.legend()
plt.grid(True)                          # show grid                # define the axes
plt.show()                              # show the plot
# save the figure as .jpg
fig.savefig('unr_rabbitts.jpg', dpi=fig.dpi, bbox_inches = "tight")
