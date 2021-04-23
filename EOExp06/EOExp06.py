import matplotlib.pyplot as plt
import numpy as np
import os
import csv

# File stuffs
working_dir = (os.path.dirname(os.path.realpath(__file__)))
filenames = ['EOExp06-1.csv', 'EOExp06-2.csv', 'EOExp06-3.csv']
titles = ['measured power to angle difference', 'measured power to angle difference', 'measured power to applied voltage']
xlabels = [r'Angle difference $\rm{(deg)}$', r'Angle difference $\rm{(deg)}$', r'Applied voltage $\rm{(V)}$']
ylabels = [r'Measured power $\rm{(mw)}$', r'Measured power $\rm{(mw)}$', r'Measured power $\rm{(mw)}$']
legends = [['Linear polarization'], [r'$\lambda/2$', r'$\lambda/4$'], ['Normal white liquid crystal']]

# plt stuffs
figs = []
axes = []
colors = ['crimson', 'mediumpurple', 'orchid']

# Axes parameters
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8

for i in range(3):
    y_datas = []
    figs.append(plt.figure(figsize=(12, 6)))
    axes.append(figs[i].add_axes([left, bottom, width, height]))
    axes[i].set_title(f'Plot of {titles[i]}')
    axes[i].set_xlabel(xlabels[i])
    axes[i].set_ylabel(ylabels[i])

    my_data = np.genfromtxt(os.path.join(working_dir, filenames[i]), delimiter='\t', skip_header=1)
    x_datas = [d[0] for d in my_data]
    for j in range(1, len(my_data[0])):
        y_datas.append([])
        y_datas[j-1] = [d[j] for d in my_data]
        axes[i].plot(x_datas, y_datas[j-1], label=legends[i][j-1], color=colors[j-1])
    
    axes[i].legend(loc='upper right')
    figs[i].savefig(os.path.join(working_dir, f'fig{i+1}.png'))

plt.show()
