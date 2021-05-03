import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import scipy
import scipy.optimize
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
xlabels = [r'Wavelength $\lambda\rm{(nm)}$', r'Wavelength $\lambda\rm{(nm)}$', r'Voltage $V_d \rm{(V)}$', r'Voltage $V_d \rm{(V)}$']
ylabels = [r'Intensity', r'Intensity', r'Current $I_d \rm{(A)}$', r'Current $I_d \rm{(A)}$']
legends = [[fr'${i}\rm{{(mA)}}$' for i in range(10, 110, 10)], [fr'${i}\rm{{(mA)}}$' for i in range(1, 11)], ['Crystal LED'], ['Market LED']]
major_locators = [50, 50, 0.2, 0.2]
minor_locators = [10, 10, 0.1, 0.1]
xmins = [350, 350, 2, 2]
xmaxs = [750, 750, 3.4, 2.9]
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
        x_data = [d[0] for d in my_data]
        y_data = [d[1] for d in my_data]
        axes[i].plot(x_data, y_data, label=legends[i][j], color=colors[j])
        
    if i >= 2:
        fit = scipy.optimize.curve_fit(lambda t,a,b: a+b*t,  x_data[1000:],  y_data[1000:],  p0=(1, 0.1))
        axes[i].plot([i for i in np.arange(x_data[1000], x_data[-1], 0.01)], [fit[0][0]+fit[0][1]*i for i in np.arange(x_data[1000], x_data[-1], 0.01)], label=r'fit curve for $R_{S}$', color=colors[5], linewidth=3)
        axes[i].plot([i for i in np.arange(x_data[250], x_data[-1], 0.01)], [fit[0][0]+fit[0][1]*i for i in np.arange(x_data[250], x_data[-1], 0.01)], linestyle='--', color=colors[5])

        if(i==2):
            axes[i].text(2.75, 0.075, rf'$I_d={fit[0][0]:.4f} + {fit[0][1]:.4f} * V_d$', fontsize=14, color=colors[5])
        else:
            axes[i].text(2.5, 0.008, rf'$I_d={fit[0][0]:.4f} + {fit[0][1]:.4f} * V_d$', fontsize=14, color=colors[5])

        fit = scipy.optimize.curve_fit(lambda t,a,b: np.exp(a+b*t),  x_data[3:50], y_data[3:50], p0=(-10, 0.01), maxfev=4000)
        axes[i].plot([i for i in np.arange(x_data[3], x_data[50], 0.01)], [np.exp(fit[0][0]+fit[0][1]*i) for i in np.arange(x_data[3], x_data[50], 0.01)], label=r'fit curve for $n$', color=colors[9], linewidth=3)
        axes[i].plot([i for i in np.arange(x_data[0], x_data[300], 0.01)], [np.exp(fit[0][0]+fit[0][1]*i) for i in np.arange(x_data[0], x_data[300], 0.01)], linestyle='--', color=colors[9])

        if(i==2):
            axes[i].text(2.2, 0.02, rf'$I_d=e^{{({fit[0][0]:.4f} + {fit[0][1]:.4f} * V_d)}}$', fontsize=14, color=colors[9])
        else:
            axes[i].text(2.2, 0.002, rf'$I_d=e^{{({fit[0][0]:.4f} + {fit[0][1]:.4f} * V_d)}}$', fontsize=14, color=colors[9])
        
    axes[i].xaxis.set_major_locator(MultipleLocator(major_locators[i]))
    axes[i].xaxis.set_minor_locator(MultipleLocator(minor_locators[i]))
    axes[i].set_xlim(xmin=xmins[i], xmax=xmaxs[i])
    axes[i].xaxis.set_major_formatter(formatters[i])
    axes[i].legend(loc='upper right')
    figs[i].savefig(os.path.join(working_dir, f'fig{i+1}.png'))

plt.show()
