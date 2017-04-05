import warnings

if ('maxDiff' not in locals() or maxDiff == []) or ('maxDiffAlong' not in locals() or maxDiffAlong == []):
    # print('Error: need to import stuff first (or run using %run -i scriptname.py)!')
    raise SystemExit('Error: need to import stuff first (or run using %run -i scriptname.py)!')

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

save_figure = True
# save_figure = False

if True:
    fig = plt.figure(
        figsize = [4.87,  2.94],
        );

    ax = fig.add_subplot(111)
    idx = 2 # temperature

    lines = []
    yAverage = averageRelativeDiffAlong
    yMax = relativeMaxDiffAlong
    factor = 100

    for i in range(len(yAverage[0][idx])):
        l, = ax.plot(x/1000.0, yAverage[0][idx][i]*factor, lw = 1, label = dataSetLabels[i])
        lines.append(l)

    ax.grid(color = [0.8]*3)
    ax.tick_params(axis = 'x', top = 'off', direction = 'out')
    ax.tick_params(axis = 'y', right = 'off', direction = 'out')

    ax.set_ylim([0, 0.14])
    ax.set_xlim([610, 650])
    ax.set_xlabel('Position [km]')
    ax.set_ylabel('Temperature difference [%]')

    leg = ax.legend(
        lines, dataSetLabels,
        loc = 'best',
        ncol = 3, 
        fontsize = 10
    )

    plt.draw()
    fig.tight_layout(pad = 0)

    if save_figure:
        plt.savefig(
            'outlet_temperature_detail.pdf'
        )

plt.show()