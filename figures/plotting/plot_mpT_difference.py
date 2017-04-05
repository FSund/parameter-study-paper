import warnings

if ('maxDiff' not in locals() or maxDiff == []) or ('maxDiffAlong' not in locals() or maxDiffAlong == []):
    # print('Error: need to import stuff first (or run using %run -i scriptname.py)!')
    raise SystemExit('Error: need to import stuff first (or run using %run -i scriptname.py)!')

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

use_seaborn = False
save_figure = True

show_abc = True

use_relative_temperature = True

# max and average temperature difference as function of position along pipe
if True:
    if use_seaborn:
        from seaborn.apionly import hls_palette
        # set default color cycle to use n individual colors using seaborn hls_palette,
        # where n is the number of data sets we have loaded
        defaultColorCycle = mpl.rcParams['axes.prop_cycle'] # keep this so we can reset it later
        mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color = hls_palette(len(dataSetLabels), l=0.5))

    # plot max and average temperature difference
    fig = plt.figure(
        figsize = np.array([16, 18])/2.54,
        # tight_layout = {'pad': 0} # do this so figure size is correct when saved when removing padding
        );

    ax2 = fig.add_subplot(313) # bottom
    ax1 = fig.add_subplot(312, sharex = ax2) # middle
    ax0 = fig.add_subplot(311, sharex = ax2) # top
    axes = [ax0, ax1, ax2]

    for idx in [0,1]: # mass flow, pressure
        ax = axes[idx]

        lines = []
        for i in range(len(averageRelativeDiffAlong[0][idx])):
            l, = ax.plot(x/1000.0, averageRelativeDiffAlong[0][idx][i]*100, lw = 1, label = dataSetLabels[i])
            lines.append(l)

        for i in range(len(relativeMaxDiffAlong[0][idx])):
            color = lines[i].get_color()
            ax.plot(x/1000.0, relativeMaxDiffAlong[0][idx][i]*100, linestyle = '--', lw = 1, color = color)

    for idx in [2]: # temperature
        ax = axes[idx]

        lines = []
        if use_relative_temperature:
            yAverage = averageRelativeDiffAlong
            yMax = relativeMaxDiffAlong
            factor = 100
        else:
            yAverage = averageDiffAlong
            yMax = maxDiffAlong
            factor = 1

        for i in range(len(yAverage[0][idx])):
            l, = ax.plot(x/1000.0, yAverage[0][idx][i]*factor, lw = 1, label = dataSetLabels[i])
            lines.append(l)

        for i in range(len(yMax[0][idx])):
            color = lines[i].get_color()
            ax.plot(x/1000.0, yMax[0][idx][i]*factor, linestyle = '--', lw = 1, color = color)

    for ax in axes:
        # ax.grid()
        ax.grid(color = [0.8]*3)
        ax.tick_params(axis = 'x', top = 'off', direction = 'out')
        ax.tick_params(axis = 'y', right = 'off', direction = 'out')

    # # plt.title('Max and average (absolute) temperature difference along pipeline')
    # plt.title('Max and average temperature difference along pipeline')
    # plt.xlabel('Position [km]')
    # plt.ylabel('Temperature difference [°C]')
    # plt.xlim([0,650])
    # plt.ylim([0, 1.2])

    # fig.tight_layout(pad = 0) # fill figure

    from matplotlib.ticker import MultipleLocator
    locator = MultipleLocator(1)
    ax1.yaxis.set_major_locator(locator)
    ax0.yaxis.set_major_locator(locator)

    if use_relative_temperature:
        ax2.set_ylim([0, 0.42])
    else:
        ax2.set_ylim([0, 1.18])
    ax1.set_ylim([0, 0.075*100])
    ax0.set_ylim([0, 0.075*100])

    ax2.set_xlim([0,650])
    ax2.set_xlabel('Position [km]')

    if use_relative_temperature:
        ax2.set_ylabel('Temperature difference [%]')
    else:
        ax2.set_ylabel('Temperature difference [°C]')
    ax1.set_ylabel('Pressure difference [%]')
    ax0.set_ylabel('Mass flow difference [%]')

    plt.setp(ax0.get_xticklabels(), visible = False)
    plt.setp(ax1.get_xticklabels(), visible = False)
    ax0.tick_params(axis = 'x', bottom = 'off')
    ax1.tick_params(axis = 'x', bottom = 'off')

    plt.draw()
    fig.tight_layout(pad = 0)
    fig.tight_layout(pad = 0)
    fig.subplots_adjust(top = 0.92) # make room for legend

    leg = fig.legend(
        lines, dataSetLabels,
        loc = 'upper center', 
        ncol = 5, 
        bbox_to_anchor = [0.5, 1.32], 
        bbox_transform = ax0.transAxes,
        fontsize = 10
    )

    if save_figure:
        plt.savefig(
            'difference_along_pipeline.pdf'
            # , dpi = 300
            # , bbox_inches='tight'
            # , pad_inches = 0
        )

        # ax2.axvspan(125, 625, facecolor='0', alpha=0.15, edgecolor = 'none')
        for ax in axes:
            ax.axvspan(0, 25, facecolor='0', alpha=0.15, edgecolor = 'none')
            ax.axvspan(625, 650, facecolor='0', alpha=0.15, edgecolor = 'none')
        plt.savefig(
            'difference_along_pipeline_shaded.pdf'
            # , dpi = 300
            # , bbox_inches='tight'
            # , pad_inches = 0
        )


        if show_abc:
            strings = ['a)', 'b)', 'c)']
            for ax, s in zip(axes, strings):
                t = plt.text(
                    0.1, 0.78, s, 
                    horizontalalignment='center', 
                    verticalalignment='top',
                    bbox = dict(facecolor = [0,0,0,0.3], edgecolor = 'none', boxstyle='round'),
                    transform = ax.transAxes,
                    fontsize = 11,
                    # fontweight = 1000 # no effect
                )

            plt.savefig('difference_along_pipeline_shaded_abc.pdf')


        if True:
            ax = fig.add_subplot(111)
            ax.set_position([0.62, 0.17, 0.25, 0.15])
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

            ax.set_ylim([0, 0.15])
            ax.set_xlim([610, 650])

            mark_inset(axes[2], ax, loc1=1, loc2=3)

            for tick in ax.xaxis.get_major_ticks():
                tick.label.set_fontsize(8)
            for tick in ax.yaxis.get_major_ticks():
                tick.label.set_fontsize(8)

            ax.yaxis.set_major_locator(MultipleLocator(0.05))
            ax.xaxis.set_major_locator(MultipleLocator(10))

            plt.savefig('difference_along_pipeline_shaded_abc_inset.pdf')

    if use_seaborn:
        mpl.rcParams['axes.prop_cycle'] = defaultColorCycle

plt.show()