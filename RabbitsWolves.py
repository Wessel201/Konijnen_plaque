# Program      : Euler's method
# Author       : MOOC team Mathematical Modelling Basics
# Created      : April, 2017

import numpy as np
import matplotlib.pyplot as plt

print("Solution for dP/dt = (b - c*x)*x - (d + a*x)*x ")
# Initializations

Dt = 0.1                                # timestep Delta t
Pk_init = 10000000000                            # initial population rabbits
Pw_init = 919996                           # initial population foxes
t_init = 0                              # initial time
t_end = 1000                               # stopping time
n_steps = int(round((t_end-t_init)/Dt)) # total number of timesteps

t_arr = np.zeros(n_steps + 1)           # create an array of zeros for t
Pk_arr = np.zeros(n_steps + 1)           # create an array of zeros for Pk
Pw_arr = np.zeros(n_steps + 1)          # create an array of zeros for Pf
t_arr[0] = t_init                       # add the initial t to the array
Pk_arr[0] = Pk_init                       # add the initial Pk to the array
Pw_arr[0] = Pw_init                        #add the initial Pf to the array

# Euler's method
# Everything per day
Mk = 12395840734
bk = 0.1
ck = 1/Mk
dk = 0.0002737
ak = 1.0978*10**(-10)
bw = 0.03968
cw = 0
dw = 0.00034247
aw = 0.000000063
Mw = 288785

def derifk(xk, xw):
	return (bk-dk)*xk*(1-ck*xk)-ak*xk*xw

def derifw (xw, xk):
   return (bw-dw)*xw*(1-1/Mw*xw)+cw*xw*xk

for i in range (1, n_steps + 1):
    Pk = Pk_arr[i-1]
    Pw = Pw_arr[i-1]
    t = t_arr[i-1]
    dPkdt = derifk(Pk,Pw)               # calculate the derivative for rabbits
    dPwdt = derifw(Pw,Pk)               # calculate the derivative for foxes
    Pk_arr[i] = Pk + Dt*dPkdt           # calculate Pk on the next time step
    Pw_arr[i] = Pw + Dt*dPwdt           # calculate Pf on the next time step
    t_arr[i] = t + Dt                   # adding the new t-value to the list

# Plot the results

fig = plt.figure()                      # create figure
plt.plot(t_arr, Pk_arr, linewidth = 4, label = "Rabbits")   # plot population vs. time
plt.plot(t_arr, Pw_arr, linewidth = 4, label = "Wolves")

plt.title('Solutions for dPk/dt = (bk-dk)*Pk*(1-ck*Pk)-ak*Pk*Pf \n and dPf/dt = (bf-df)*Pf*(1-Pf/Mf)+cf*Pf*Pk', fontsize = 10)  
plt.xlabel('t (in days)', fontsize = 20)
plt.ylabel('P(t)', fontsize = 20)

plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.legend()
plt.grid(True)                          # show grid                # define the axes
plt.show()                              # show the plot
# save the figure as .jpg
fig.savefig('Rainbowfish.jpg', dpi=fig.dpi, bbox_inches = "tight")