import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import scipy
import scipy.optimize
import os

# File stuffs
working_dir = (os.path.dirname(os.path.realpath(__file__)))
filenames = [
    [os.path.join('Data', 'Crystal LED', f'Crystal_LED_{i:03d}ma.Master.Scope') for i in range(10, 110, 10)],
    [os.path.join('Data', 'Market LED', f'Market_LED_{i:02d}ma.Master.Scope') for i in range(1, 11)],
]
titles = ['EQE of Crystal LED', 'EQE of Market LED']
xlabels = [r'Current $I_d \rm{(A)}$', r'Current $I_d \rm{(A)}$']
ylabels = [r'EQE (unit unknown)', r'EQE (unit unknown)']
legends = [['Crystal LED'], ['Market LED']]
major_locators = [10, 1]
minor_locators = [10, 1]
xmins = [0, 0]
xmaxs = [100, 10]
formatters = ['{x:.0f}', '{x:.0f}']
skip_headers = [19, 19]
skip_footers = [1, 1]

exposure_time = 0.045 # sec
electons_per_C = 6.241e18

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
    y_datas = []
    x_values.append([])
    y_values.append([])
    figs.append(plt.figure(figsize=(12, 6)))
    axes.append(figs[i].add_axes([left, bottom, width, height]))
    axes[i].set_title(f'{titles[i]}')
    axes[i].set_xlabel(xlabels[i])
    axes[i].set_ylabel(ylabels[i])

    for j in range(len(filenames[i])):
        my_data = np.genfromtxt(os.path.join(working_dir, filenames[i][j]), delimiter='\t',
            skip_header=skip_headers[i], skip_footer=skip_footers[i])
        y_data = [d[1] for d in my_data]
        x_values[i].append(minor_locators[i]*(j+1))
        base = sum(y_data[650:])/len(y_data[650:])
        y_values[i].append( (sum(y_data)-base*len(y_data)) / (1e-3*minor_locators[i]*(j+1)*exposure_time*electons_per_C))

    axes[i].plot(x_values[i], y_values[i], label=legends[i][0], color=colors[i])
        
    axes[i].xaxis.set_major_locator(MultipleLocator(major_locators[i]))
    axes[i].xaxis.set_minor_locator(MultipleLocator(minor_locators[i]))
    axes[i].set_xlim(xmin=xmins[i], xmax=xmaxs[i])
    axes[i].xaxis.set_major_formatter(formatters[i])
    axes[i].legend(loc='upper right')
    figs[i].savefig(os.path.join(working_dir, f'fig{i+5}.png'))

plt.show()
