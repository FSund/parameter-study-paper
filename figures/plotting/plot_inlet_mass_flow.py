# -*- coding: utf-8 -*-
from __future__ import unicode_literals # for degree sign in strings: °C
import os
cwd = os.getcwd()
dir = "D:/VirtualBox VMs/Shared folder/gas_flow/projects/sensitivityAnalysis/internalEnergy/newUnsteady/rampDown/massFlow/09"
os.chdir(dir)

import numpy as np
import matplotlib.pyplot as plt

# load files
m = np.loadtxt('massFlow.csv', delimiter = ','
               , usecols=(0,1) # only load time and inlet
               )

# change back to dir where we started
os.chdir(os.path.realpath(cwd))

# plot
plt.close('all')

golden = (1.0+np.sqrt(5))/2.0;
h = 3
# w = h/golden
w = 2
figsize = [h, w]
fig = plt.figure(
    figsize = figsize,
    tight_layout = {'pad': 0, 'w_pad': 0, 'h_pad': 0} # do this so figure size is correct when saved when removing padding
    )
ax = fig.add_subplot(111);

t = m[:,0]
t = t/60
t = t - t[0]
t = t-116 - 0.0783
ax.plot(t, m[:,1])
# plt.show()

ax.set_xlim([0, 124-116])
ax.set_ylim([100, 700])

ax.set_xlabel('Time [minutes]')
ax.set_ylabel('Inlet mass flow [kg/s]')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.tick_left()
ax.xaxis.tick_bottom()

plt.grid()

plt.show()

# plt.savefig('inlet_mass_flow.png', dpi = 300, transparency = True)
plt.savefig('inlet_mass_flow.pdf', dpi = 300)