# Program      : Euler's method
# Author       : MOOC team Mathematical Modelling Basics
# Created      : April, 2017

import numpy as np
import matplotlib.pyplot as plt

print("Solution for dP/dt = (b - c*x)*x - (d + a*x)*x ")
# Initializations

Dt = 1                                # timestep Delta t
Pk_init = 20                            # initial population rabbits
Pg_init = 0                            # initial population goats
t_init = 0                              # initial time
t_end = 1500                               # stopping time
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
ak = 0
bg = 1/150
cg = bg/12395840734
dg = 1/4197.5
ag = 0

def derifk(xk, xg):
	return (bk - (ck+(xg/700))*xk)*xk - (dk + ak*xk)*xk

def derifg (xg, xk):
    return (bg - (cg+(xk/700))*xg)*xg - (dg + ag*xg)*xg

for i in range (1, n_steps + 1):
    Pk = Pk_arr[i-1]
    Pg = Pg_arr[i-1]
    t = t_arr[i-1]
    dPkdt = derifk(Pk,Pg)               # calculate the derivative for rabbits
    dPgdt = derifg(Pg,Pk)               # calculate the derivative for goats
    Pk_arr[i] = Pk + Dt*dPkdt           # calculate Pk on the next time step
    Pg_arr[i] = Pg + Dt*dPgdt           # calculate Pg on the next time step
    t_arr[i] = t + Dt                   # adding the new t-value to the list

# Plot the results

fig = plt.figure()                      # create figure
plt.plot(t_arr, Pk_arr, linewidth = 4, label = "Rabbits")   # plot population vs. time
plt.plot(t_arr, Pg_arr, linewidth = 4, label = "Goats")

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
