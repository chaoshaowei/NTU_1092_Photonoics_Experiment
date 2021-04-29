import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import os
import math

# File stuffs
working_dir = (os.path.dirname(os.path.realpath(__file__)))
filenames = [
    [os.path.join('Data', 'Crystal LED', f'Crystal_LED_{i:03d}ma.Master.Scope') for i in range(10, 110, 10)],
    [os.path.join('Data', 'Market LED', f'Market_LED_{i:02d}ma.Master.Scope') for i in range(1, 11)],
    [os.path.join('Data', 'Crystal LED', f'Crystal_LED_IV_Curve.txt')],
    [os.path.join('Data', 'Market LED', f'Market_LED_IV_Curve.txt')],
]
titles = ['Spectrum of Crystal LED', 'Spectrum of Market LED', 'IV Curve of Crystal LED', 'IV Curve of Market LED']
xlabels = [r'Frequency $\lambda\rm{(nm)}$', r'Frequency $\lambda\rm{(nm)}$', r'Voltage $\rm{(V)}$', r'Voltage $\rm{(V)}$']
ylabels = [r'Intensity', r'Intensity', r'Current $\rm{(A)}$', r'Current $\rm{(A)}$']
legends = [[fr'${i}\rm{{(mA)}}$' for i in range(10, 110, 10)], [fr'${i}\rm{{(mA)}}$' for i in range(1, 11)], ['Crystal LED'], ['Market LED']]
major_locators = [50, 50, 1, 1]
minor_locators = [50, 50, 0.2, 0.2]
xmins = [350, 350, 0, 0]
xmaxs = [750, 750, 3.6, 3.6]
formatters = ['{x:.0f}', '{x:.0f}', '{x:.1f}', '{x:.1f}']
skip_headers = [19, 19, 2, 2]
skip_footers = [1, 1, 0, 0]

# plt stuffs
figs = []
axes = []
colors = ['navy', 'mediumblue', 'slateblue', 'mediumslateblue', 'mediumpurple', 'mediumorchid',
    'violet', 'orchid', 'hotpink', 'deeppink', 'crimson', 'firebrick']

# Axes parameters
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8

for i in range(len(filenames)):
    y_datas = []
    figs.append(plt.figure(figsize=(12, 6)))
    axes.append(figs[i].add_axes([left, bottom, width, height]))
    axes[i].set_title(f'{titles[i]}')
    axes[i].set_xlabel(xlabels[i])
    axes[i].set_ylabel(ylabels[i])

    for j in range(len(filenames[i])):
        my_data = np.genfromtxt(os.path.join(working_dir, filenames[i][j]), delimiter='\t', skip_header=skip_headers[i], skip_footer=skip_footers[i])
        x_datas = [d[0] for d in my_data]
        y_data = [d[1] for d in my_data]
        axes[i].plot(x_datas, y_data, label=legends[i][j], color=colors[j])
        
    axes[i].xaxis.set_major_locator(MultipleLocator(major_locators[i]))
    axes[i].xaxis.set_minor_locator(MultipleLocator(minor_locators[i]))
    axes[i].set_xlim(xmin=xmins[i], xmax=xmaxs[i])
    axes[i].xaxis.set_major_formatter(formatters[i])
    axes[i].legend(loc='upper right')
    figs[i].savefig(os.path.join(working_dir, f'fig{i+1}.png'))

plt.show()
