# -*- coding: utf-8 -*-
from __future__ import unicode_literals # for degree sign in strings: °C
import warnings

if ('maxDiff' not in locals() or maxDiff == []) or ('maxDiffAlong' not in locals() or maxDiffAlong == []):
    # print('Error: need to import stuff first (or run using %run -i scriptname.py)!')
    raise SystemExit('Error: need to import stuff first (or run using %run -i scriptname.py)!')

import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

save_figure = False
save_figure = True


# max and average difference as function of position along pipe
if True:
# if False:
    # from seaborn.apionly import hls_palette
    # set default color cycle to use n individual colors using seaborn hls_palette,
    # where n is the number of data sets we have loaded
    # defaultColorCycle = mpl.rcParams['axes.prop_cycle']
    # mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color = hls_palette(len(dataSetLabels), l=0.5))

    idx = 0 # Z factor
    # w =  5.6901
    w =  16/2.54
    h = 7/2.54
    figsize = np.array([w, h])

    lines = []
    dashlines = []

    # flow
    fig = plt.figure(
        figsize = figsize,
        # tight_layout = {'pad': 0} # do this so figure size is correct when saved when removing padding)
    )
    ax0 = fig.add_subplot(111)
    # box = ax0.get_position()
    # ax0.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    l, = plt.plot(x/1000.0, averageRelativeDiffAlong[0][0][idx]*100, color = 'C0', label = 'Mass flow')
    lines.append(l)
    dashlines.append(l)
    l, = plt.plot(x/1000.0, relativeMaxDiffAlong[0][0][idx]*100, linestyle = '--', color = 'C0')
    dashlines.append(l)

    l, = plt.plot(x/1000.0, averageRelativeDiffAlong[0][1][idx]*100, color = 'C2', label = 'Pressure')
    lines.append(l)
    plt.plot(x/1000.0, relativeMaxDiffAlong[0][1][idx]*100, linestyle = '--', color = 'C2')

    ax1 = ax0.twinx()
    axes = [ax0, ax1]

    # ax2.plot(t, s2, 'r.')
    # ax2.set_ylabel('sin', color='r')
    l, = ax1.plot(x/1000.0, averageDiffAlong[0][2][idx], color = 'C3', label = 'Temperature')
    lines.append(l)
    ax1.plot(x/1000.0, maxDiffAlong[0][2][idx], linestyle = '--', color = 'C3')


    # plt.title('Max and average (relative) mass flow difference along pipeline')
    ax0.set_xlabel('Position [km]')
    ax0.set_ylabel('Relative mass flow/pressure diff. [%]')
    ax1.set_ylabel('Absolute temperature diff. [°C]')
    # plt.ylabel('Relative mass flow difference [%]')
    plt.xlim([0, 650])
    # plt.axis([0, 650, 0, 0.9])

    ax0.set_ylim([0, 8])
    ax1.set_ylim([0, 0.8])

    ax0.tick_params(axis = 'y', left = 'on', right = 'off', direction = 'out')
    ax0.tick_params(axis = 'x', top = 'off', bottom = 'on', direction = 'out')
    ax1.tick_params(axis = 'y', left = 'off', right = 'on', direction = 'out')

    # for ax in [ax0, ax1]:
        # ax.spines['top'].set_visible(False)

    from matplotlib.ticker import MultipleLocator
    # locator = MultipleLocator(1)
    ax0.yaxis.set_major_locator(MultipleLocator(1))
    ax1.yaxis.set_major_locator(MultipleLocator(0.1))

    ax1.spines['right'].set_color('C3')

    ax0.grid(color = [0.8]*3)

    for ax in [ax0]:
        ax.axvspan(0, 25, facecolor='0', alpha=0.15, edgecolor = 'none')
        ax.axvspan(625, 650, facecolor='0', alpha=0.15, edgecolor = 'none')

    for t in ax1.get_yticklabels():
        t.set_color('C3')

    for t in ax1.get_yticklines():
        t.set_color('C3')

    if h < 8/2.54:
        xpos = 0.64
        ypos0 = 1.02
        ypos1 = 0.9
    else:
        xpos = 0.55
        ypos0 = 1.02
        ypos1 = 0.94

    # add legend for m, p, T
    # lgdArtists = []
    # lgdArtists.append(plt.Line2D((0,0),(0,0), color='C0'))
    # lgdArtists.append(plt.Line2D((0,0),(0,0), color='C2'))
    # lgdArtists.append(plt.Line2D((0,0),(0,0), color='C3'))
    lgdArtists = lines
    leg0 = ax0.legend(
        lgdArtists, ["Mass flow", "Pressure", "Temperature"],
        loc = 'upper center', fontsize = 10, 
        bbox_to_anchor = (xpos, ypos0), ncol = 3
    )

    # add custom legend for solid and dashed lines
    lgdArtists = []
    lgdArtists.append(plt.Line2D((0,0),(0,0), color='k', linestyle='-'))
    lgdArtists.append(plt.Line2D((0,0),(0,0), color='k', linestyle='--'))
    leg1 = ax1.legend(
        lgdArtists, ["Avg. diff.", "Max. diff."], 
        loc = 'upper center', fontsize = 10, 
        bbox_to_anchor = (xpos, ypos1), ncol = 2
    )

    ax0.set_title('Max and average difference along pipeline')
    fig.tight_layout(pad = 0) # fill figure

    if save_figure:
        # fig.savefig('all_differences_position.png', dpi = 300)
        fig.savefig(
            'all_differences_position.pdf', 
            # dpi = 300, 
            # bbox_inches="tight", # gives error if figure(tight_layout = ) is used
            # pad_inches = 0,
            # bbox_extra_artists = (lgd,)
            );

    if False:
        # vertical lines to mark shore and stuff
        for x in [25, 45, 325, 625]:
            plt.axvline(x = x, color = 'k'
                        # , linestyle = '--'
                        )

        if save_figure:
            # fig.savefig('all_differences_position_with_lines.png', dpi = 300)
            fig.savefig('all_differences_position_with_lines.pdf', dpi = 300, bbox_inches="tight", pad_inches = 0);

plt.show()



    # mpl.rcParams['axes.prop_cycle'] = defaultColorCycle

