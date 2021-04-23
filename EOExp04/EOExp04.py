import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import os
import math

# File stuffs
working_dir = (os.path.dirname(os.path.realpath(__file__)))
filenames = ['EOExp04-1.csv']
titles = ['measured power to voltage']
xlabels = [r'Applied voltage $\rm{(V)}$']
ylabels = [r'Measured power $\rm{(\mu w)}$']
legends = [['Measured powe']]
major_locators = [4]
minor_locators = [1]
xmins = [-12]
xmaxs = [12]
formatters = ['{x:.0f}']

# plt stuffs
figs = []
axes = []
colors = ['crimson', 'mediumpurple', 'orchid']

# Axes parameters
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8

for i in range(1):
    y_datas = []
    figs.append(plt.figure(figsize=(12, 6)))
    axes.append(figs[i].add_axes([left, bottom, width, height]))
    axes[i].set_title(f'Plot of {titles[i]}')
    axes[i].set_xlabel(xlabels[i])
    axes[i].set_ylabel(ylabels[i])

    my_data = np.genfromtxt(os.path.join(working_dir, filenames[i]), delimiter=',', skip_header=1)
    x_datas = [d[0] for d in my_data]
    for j in range(1, len(my_data[0])):
        y_datas.append([])
        y_datas[j-1] = [d[j] for d in my_data]
        axes[i].plot(x_datas, y_datas[j-1], label=legends[i][j-1], color=colors[j-1])
    
    axes[i].xaxis.set_major_locator(MultipleLocator(major_locators[i]))
    axes[i].xaxis.set_minor_locator(MultipleLocator(minor_locators[i]))
    axes[i].set_xlim(xmin=xmins[i], xmax=xmaxs[i])
    axes[i].xaxis.set_major_formatter(formatters[i])
    axes[i].legend(loc='upper right')
    figs[i].savefig(os.path.join(working_dir, f'fig{i+1}.png'))

plt.show()
