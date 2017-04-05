import warnings

if ('maxDiff' not in locals() or maxDiff == []) or ('maxDiffAlong' not in locals() or maxDiffAlong == []):
    # print('Error: need to import stuff first (or run using %run -i scriptname.py)!')
    raise SystemExit('Error: need to import stuff first (or run using %run -i scriptname.py)!')

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

use_seaborn = False

# max and average temperature difference as function of position along pipe
if True:
    if use_seaborn:
        from seaborn.apionly import hls_palette
        # set default color cycle to use n individual colors using seaborn hls_palette,
        # where n is the number of data sets we have loaded
        defaultColorCycle = mpl.rcParams['axes.prop_cycle'] # keep this so we can reset it later
        mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color = hls_palette(len(dataSetLabels), l=0.5))

    idx = 2 # temperature
    # idx = 0 # mass flow

    # plot max and average temperature difference
    fig = plt.figure(
        figsize = np.array([16, 9])/2.54,
        # tight_layout = {'pad': 0} # do this so figure size is correct when saved when removing padding
        );

    ax = fig.add_subplot(111)

    for i in range(len(averageDiffAlong[0][idx])):
        plt.plot(x/1000.0, averageDiffAlong[0][idx][i], lw = 1)

    plt.legend(dataSetLabels, loc = 'upper center', ncol = 2, bbox_to_anchor = [0.55, 0.88], fontsize = 10)

    for i in range(len(maxDiffAlong[0][idx])):
        plt.plot(x/1000.0, maxDiffAlong[0][idx][i], linestyle = '--', lw = 1)

    plt.grid()
    ax.tick_params(axis = 'x', top = 'off', direction = 'out')
    ax.tick_params(axis = 'y', right = 'off', direction = 'out')

    # plt.title('Max and average (absolute) temperature difference along pipeline')
    plt.title('Max and average temperature difference along pipeline')
    plt.xlabel('Position [km]')
    plt.ylabel('Temperature difference [°C]')
    plt.xlim([0,650])
    plt.ylim([0, 1.2])

    fig.tight_layout(pad = 0) # fill figure

    if save_figure:
        plt.savefig(
            'temperature_difference_along_pipeline.pdf'
            # , dpi = 300
            # , bbox_inches='tight'
            # , pad_inches = 0
        )
        plt.axvspan(125, 625, facecolor='0', alpha=0.15, edgecolor = 'none')
        plt.savefig(
            'temperature_difference_along_pipeline_shaded.pdf'
            # , dpi = 300
            # , bbox_inches='tight'
            # , pad_inches = 0
        )

    if use_seaborn:
        mpl.rcParams['axes.prop_cycle'] = defaultColorCycle

plt.show()