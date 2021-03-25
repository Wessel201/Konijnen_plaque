# Program      : Euler's method
# Author       : MOOC team Mathematical Modelling Basics
# Created      : April, 2017

import numpy as np
import matplotlib.pyplot as plt

print("Solution for dP/dt = (b - c*x)*x - (d + a*x)*x ")
# Initializations

Dt = 0.1                                # timestep Delta t
Pk_init = 10000000000                            # initial population rabbits
Pf_init = 0                           # initial population foxes
t_init = 0                              # initial time
t_end = 150                               # stopping time
n_steps = int(round((t_end-t_init)/Dt)) # total number of timesteps

t_arr = np.zeros(n_steps + 1)           # create an array of zeros for t
Pk_arr = np.zeros(n_steps + 1)           # create an array of zeros for Pk
Pf_arr = np.zeros(n_steps + 1)          # create an array of zeros for Pf
t_arr[0] = t_init                       # add the initial t to the array
Pk_arr[0] = Pk_init                       # add the initial Pk to the array
Pf_arr[0] = Pf_init                        #add the initial Pf to the array

# Euler's method
# Everything per day
bk = 0.1
ck = bk/12395840734
dk = 0.0002737
ak = 0.25
bf = 5/102
cf = 0
df = 1/4197.5
af = 0

def derifk(xk, xf):
	return (bk - ck*xk)*xk - (dk + ak*xf)*xk

def deriff (xf, xk):
   return (bf + cf*xf)*xf - (df - af*xf)*xf

for i in range (1, n_steps + 1):
    Pk = Pk_arr[i-1]
    Pf = Pf_arr[i-1]
    t = t_arr[i-1]
    dPkdt = derifk(Pk,Pf)               # calculate the derivative for rabbits
    dPfdt = deriff(Pf,Pk)               # calculate the derivative for foxes
    Pk_arr[i] = Pk + Dt*dPkdt           # calculate Pk on the next time step
    Pf_arr[i] = Pf + Dt*dPfdt           # calculate Pf on the next time step
    t_arr[i] = t + Dt                   # adding the new t-value to the list

# Plot the results

fig = plt.figure()                      # create figure
plt.plot(t_arr, Pk_arr, linewidth = 4, label = "Rabbits")   # plot population vs. time
plt.plot(t_arr, Pf_arr, linewidth = 4, label = "Foxes")

plt.title('Solution for dx/dt = (b - c*x)*x - (d + a*x)*x', fontsize = 10)  
plt.xlabel('t (in days)', fontsize = 20)
plt.ylabel('P(t)', fontsize = 20)

plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.legend()
plt.grid(True)                          # show grid                # define the axes
plt.show()                              # show the plot
# save the figure as .jpg
fig.savefig('Rainbowfish.jpg', dpi=fig.dpi, bbox_inches = "tight")
