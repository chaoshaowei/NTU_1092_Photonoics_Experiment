import matplotlib.pyplot as plt
import numpy as np
import os

wl1 = 600
wl2 = 660

seperate_fig = False

scopes = ['15k', '30k', '60k', '90k', '120k', '150k', '180k', '210k', '240k', '270k', '300k', '330k']
colors = ['navy', 'mediumblue', 'slateblue', 'mediumslateblue', 'mediumpurple', 'mediumorchid',
    'violet', 'orchid', 'hotpink', 'deeppink', 'crimson', 'firebrick']

if seperate_fig:
    fig1 = plt.figure(figsize=(12,8))
    fig2 = plt.figure(figsize=(12,8))
    fig3 = plt.figure(figsize=(12,8))

    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax1 = fig1.add_axes([left, bottom, width, height])
    ax2 = fig2.add_axes([left, bottom, width, height])
    ax3 = fig3.add_axes([left, bottom, width, height])
else:
    left  = 0.1    # the left side of the subplots of the figure
    right = 0.9    # the right side of the subplots of the figure
    bottom = 0.1   # the bottom of the subplots of the figure
    top = 0.9      # the top of the subplots of the figure
    wspace = 0.2   # the amount of width reserved for blank space between subplots
    hspace = 0.1   # the amount of height reserved for white space between subplots

    fig = plt.figure(figsize=(15,5))
    plt.subplots_adjust(left=left, right=right, bottom=bottom, top=top, wspace=wspace, hspace=hspace)
    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2)
    ax3 = fig.add_subplot(1, 3, 3)

ax1.set_title('Plot of intensity to wavelength')
ax1.axis([340, 1020, 0, 4096])
ax1.set_xlabel(r'wavelength $\rm{(nm)}$')
ax1.set_ylabel('intensity')

ax2.set_title('Plot of intensity to wavelength')
ax2.axis([wl1, wl2, 100, 550])
ax2.set_xlabel(r'wavelength $\rm{(nm)}$')
ax2.set_ylabel('intensity')

ax3.set_title('Plot of total intensity to temperature')
ax3.axis([0, 350, 0, 15])
ax3.set_xlabel(r'temperature $\rm{(K)}$')
ax3.set_ylabel(r'total intensity$(\times 10^{3}) $')

wavelength = []
intensity = []
intensities = []
total = 0

for n, c in zip(scopes, colors):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.join('Scope',  n + '.Master.Scope')), 'r') as f:
        line = f.readline()
        x = 1
        while line != ">>>>>Begin Spectral Data<<<<<":
            line = f.readline()[:-1]
            x += 1
        while line != ">>>>>End Spectral Data<<<<<":
            line = f.readline()[:-1]
            x += 1
            try:
                w = float(line.split('\t')[0])
                i = float(line.split('\t')[1])
                wavelength.append(w)
                intensity.append(i)
                if w < wl2 and w > wl1:
                    total += i - 150
            except ValueError:
                break
    intensities.append(total/1000)
    ax1.plot(wavelength, intensity, c, label=n)
    ax2.plot(wavelength, intensity, c, label=n)
    wavelength = []
    intensity = []
    total = 0

ax3.plot([int(n[:-1]) for n in scopes], intensities, color='orchid', linestyle='-', marker='o')
ax1.legend()
ax2.legend()
if seperate_fig:
    fig1.savefig(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fig1png'))
    fig3.savefig(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fig2.png'))
    fig2.savefig(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fig3.png'))
else:
    fig.savefig(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fig.png'))

fig4 = plt.figure(figsize=(12, 6))
ax4 = fig4.add_axes([0.1, 0.1, 0.8, 0.8])

ax4.set_title('Plot of IQE to temperature')
ax4.axis([0, 350, 0, 100])
ax4.set_xlabel(r'temperature $\rm{(K)}$')
ax4.set_ylabel(r'IQE$(\%)$')

cent = [100]
for i in intensities[1:]:
    cent.append(100*i/intensities[0])
ax4.plot([int(n[:-1]) for n in scopes], cent, color='orchid', linestyle='-', marker='o')
fig4.savefig(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fig4.png'))

plt.show()
