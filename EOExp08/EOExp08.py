import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import scipy.optimize
import os

# File stuffs
working_dir = (os.path.dirname(os.path.realpath(__file__)))
filenames = [
    [os.path.join('Exp08_Data', f'flash_light{i:01d}.txt') for i in range(1, 4)],
    [os.path.join('Exp08_Data', f'no_light{i:01d}.txt')    for i in range(1, 4)],
    [os.path.join('Exp08_Data', f'red_laser{i:01d}.txt')   for i in range(1, 4)],
]
titles = ['IV-Curve of Flash light','IV-Curve of No light','IV-Curve of Red Laser']
xlabels = [r'Voltage $V \rm{(V)}$'] * 3
ylabels = [r'Current $I \rm{(\mu A)}$'] * 3
legends = [['Flash light'], ['No Light'], ['Red Laser']]
major_locators = [2, 2, 1]
minor_locators = [1, 1, 0.5]
xmins = [-5, -5, -1]
xmaxs = [5, 5, 1]
ymins = [-5, -5, -15]
ymaxs = [5, 5, 25]
xformatters = ['{x:.0f}', '{x:.0f}', '{x:.1f}']
skip_headers = [2, 2, 2]
skip_footers = [1, 1, 1]

# plt stuffs
figs = []
axes = []
colors = ['navy', 'mediumblue', 'slateblue', 'mediumslateblue', 'mediumpurple', 'mediumorchid',
    'violet', 'orchid', 'hotpink', 'deeppink', 'crimson', 'firebrick']

x_values = []
y_values = []

# Axes parameters
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8

for i in range(len(filenames)):
    figs.append(plt.figure(figsize=(12, 6)))
    axes.append(figs[i].add_axes([left, bottom, width, height]))

figs.append(plt.figure(figsize=(12, 6)))
axes.append(figs[-1].add_axes([left, bottom, width, height]))
axes[-1].set_title('IV-Curve of Lights')
axes[-1].set_xlabel(xlabels[0])
axes[-1].set_ylabel(ylabels[0])

for i in range(len(filenames)):
    x_values.append([])
    y_values.append([])
    axes[i].set_title(f'{titles[i]}')
    axes[i].set_xlabel(xlabels[i])
    axes[i].set_ylabel(ylabels[i])

    for j in range(len(filenames[i])):
        my_data = np.genfromtxt(os.path.join(working_dir, filenames[i][j]), delimiter='\t',
            skip_header=skip_headers[i], skip_footer=skip_footers[i])
        x_data = [d[0] for d in my_data]
        y_data = [1000000*d[1] for d in my_data]
        x_values[i].append(x_data)
        y_values[i].append(y_data)
        axes[i].plot(x_values[i][j], y_values[i][j], label=f'{legends[i][0]} {j+1}', color=colors[i*4+j])
        axes[-1].plot(x_values[i][j], y_values[i][j], label=f'{legends[i][0]} {j+1}', color=colors[i*4+j])
    axes[i].xaxis.set_major_locator(MultipleLocator(major_locators[i]))
    axes[i].xaxis.set_minor_locator(MultipleLocator(minor_locators[i]))
    axes[i].set_xlim(xmin=xmins[i], xmax=xmaxs[i])
    axes[i].xaxis.set_major_formatter(xformatters[i])
    axes[i].legend(loc='upper left')
    figs[i].savefig(os.path.join(working_dir, f'fig_{legends[i][0]}.png'))

axes[-1].xaxis.set_major_locator(MultipleLocator(major_locators[0]))
axes[-1].xaxis.set_minor_locator(MultipleLocator(minor_locators[0]))
axes[-1].set_xlim(xmin=xmins[0], xmax=xmaxs[0])
axes[-1].xaxis.set_major_formatter(xformatters[0])
axes[-1].legend(loc='upper left')
figs[-1].savefig(os.path.join(working_dir, f'fig{1}.png'))


plt.show()
