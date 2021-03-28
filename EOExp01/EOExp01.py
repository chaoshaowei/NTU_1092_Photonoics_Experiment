import matplotlib.pyplot as plt
import numpy as np
import os

colors = ['crimson', 'mediumpurple', 'orchid']

fig1 = plt.figure(figsize=(12,6))
ax1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])

ax1.set_title('Plot of laser power to current')
ax1.axis([0.3, 1, 0, 60])
ax1.set_xlabel(r'current $\rm{(A)}$')
ax1.set_ylabel(r'laser power $\rm{(mw)}$')

current = range(13)
current = [0.95-0.05*i for i in current]
power1 = [58.3, 53.2, 46.8, 41.2, 35.5, 28.6, 26.4, 21.5, 20, 16, 11.8, 6.6, 3.6]
power2 = [47, 44.2, 41.2, 38.5, 34.8, 30.8, 26.9, 22.7, 21.4, 16.7, 12.1, 7.5, 3.8]

ax1.plot(current, power1, linestyle='-', marker='o', color=colors[0], label='95%')
ax1.plot(current, power2, linestyle='-', marker='o', color=colors[1], label='90%')
ax1.legend()
fig1.savefig('fig1.png')

fig2 = plt.figure(figsize=(12,6))
ax2 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])

ax2.set_title('Plot of laser power to current')
ax2.axis([0, 360, 0, 1])
ax2.set_xlabel(r'angle $( ^{\circ })$')
ax2.set_ylabel(r'brightness')

angles = [-30, 10, 55, 100, 140, 195, 240, 280, 330, 370]
brightness = [1, 0]*5

ax2.plot(angles, brightness, linestyle='-', marker='o', color=colors[2], label='brightness')
for x, y in zip(angles, brightness):#r'%.0f^{\circ' % x
    ax2.annotate(r'$%i^{\circ}$' % x,
    xy=(float(x), float(y)),
    xytext=(float(x)+10, (float(y)-0.5)*0.9+0.5),
    size=15)
ax2.legend()
fig2.savefig('fig2.png')

plt.show()
