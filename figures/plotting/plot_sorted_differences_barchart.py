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

use_relative_temperature = True

# colors = ['#348ABD', '#7A68A6', '#A60628', '#467821', '#CF4457', '#188487', '#E24A33']
# colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
colors = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9']


if True:
    # figsize = [8, 8]
    figsize = [16/2.54, 6.65]
    # save_figure = False
    barheight = 0.8 # default 0.8
    barspacing = 0.2 # default 0.2

    if True:
        indices0 = [0, 25, 84, 110]
        l0 = ['Inlet', 'End onshore section', 'End offshore section', 'Outlet']
    elif True:
        indices0 = [0, 25, 27, 55, 84, 110]
        l0 = ['Inlet', 'End onshore section', '20 km offshore', '300 km offshore (midpoint)', 'End offshore section', 'Outlet']
    else:
        indices0 = [0, 27, 55]
        l0 = ['Inlet', '20 km offshore', '300 km offshore (midpoint)']



    ## mass flow difference - average and max #####################################################
    if True:
        indices = [25, 84, 110]
        l = ['End onshore section', 'End offshore section', 'Outlet']
        barcolors = colors[1:]
    else:
        indices = [25, 27, 55, 84, 110]
        l = ['End onshore section', '20 km offshore', '300 km offshore (midpoint)', 'End offshore section', 'Outlet']
        barcolors = ['g', 'm', 'y', 'r', 'c']

    fig = plt.figure(
        figsize = figsize,
        # tight_layout = {'pad' : 0}
    )
    ax = fig.add_subplot(111)

    values_avg = []
    values_max = []
    labels = []
    colors2 = []
    for j in range(len(maxDiff[0][0])): # loop over folders
        for i, idx in enumerate(indices):
            if True:
            # if relativeMaxDiffAlong[0][0][j][idx]*100 > 0.04:
                values_avg.append(averageRelativeDiffAlong[0][0][j][idx])
                values_max.append(relativeMaxDiffAlong[0][0][j][idx])
                labels.append(dataSetLabels[j])
                colors2.append(barcolors[i])

    labels = np.array(labels)
    values_avg = np.array(values_avg)
    values_max = np.array(values_max)
    colors2 = np.array(colors2)
    inds = values_avg.argsort() # sort average

    labels = labels[inds]
    values_avg = values_avg[inds]
    values_max = values_max[inds]
    colors2 = colors2[inds]
    
    y_pos = np.arange(len(values_avg))*(barheight + barspacing)

    # max
    rects = ax.barh(y_pos, values_max*100.0, height = barheight, color = colors2, align = 'center')

    # averages
    # ax.barh(y_pos, values_avg*100.0, facecolor = (1,1,1,0.4), align = 'center', hatch = '//') # this doesn't work due to a bug in matplotlib 2.0.0
    rects = ax.barh(y_pos, values_avg*100.0, height = barheight, align = 'center', facecolor = (1,1,1,0.4))
    rects = ax.barh(y_pos, values_avg*100.0, height = barheight, align = 'center', hatch = '////', color = 'None')

    plt.yticks(y_pos, labels)
    plt.setp(ax.get_yticklines(), visible = False)
    plt.title('Relative difference in mass flow for selected pipe sections')
    plt.xlabel('Relative mass flow difference [%]')
    plt.ylim([-0.5, len(y_pos) - 0.5])
    plt.xlim([0, 7.5])
    ax.grid('on', axis = 'x')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis = 'x', bottom = 'off')

    # left align y tick labels
    ax.yaxis.set_tick_params(pad = 0)
    # for label in ax.yaxis.get_ticklabels():
        # label.set_horizontalalignment('left')

    # Create custom artists
    artists = []
    legends = []
    for i, idx in enumerate(indices):
        artists.append(plt.Rectangle((0,0), 0, 0, facecolor = barcolors[i], edgecolor = None))
        legends.append(l[i])

    artists.append(plt.Rectangle((0,0), 0, 0, facecolor = 'lightgrey', hatch = '////', edgecolor = None))
    # artists.append(plt.Rectangle((0,0), 0, 0, facecolor = 'none', edgecolor = 'k'))

    # Create legend from custom artist/label lists
    ax.legend(artists, legends + ['Average', 'Max'], loc = 'lower right')

    fig.tight_layout(pad = 0) # fill figure
    fig.subplots_adjust(left = 0.1) # add some space on left side, so all figures have same size in the end

    if save_figure:
        plt.savefig('barchart_all_mass_flow_relative.pdf'
            # , dpi = 72
            # , bbox_inches='tight'
            # , pad_inches = 0
        )



    ## pressure difference - average and max ######################################################
    indices = [0, 25, 84]
    l = ['Inlet', 'End onshore section', 'End offshore section']
    barcolors = colors

    fig = plt.figure(
        figsize = figsize,
        # tight_layout = {'pad' : 0}
    )
    ax = fig.add_subplot(111)

    values_avg = []
    values_max = []
    labels = []
    colors2 = []
    for j in range(len(maxDiff[0][0])): # loop over folders
        for i, idx in enumerate(indices):
            if True:
            # if relativeMaxDiffAlong[0][1][j][idx]*100 > 0.006:
                values_avg.append(averageRelativeDiffAlong[0][1][j][idx])
                values_max.append(relativeMaxDiffAlong[0][1][j][idx])
                labels.append(dataSetLabels[j])
                colors2.append(colors[i])

    labels = np.array(labels)
    values_avg = np.array(values_avg)
    values_max = np.array(values_max)
    colors2 = np.array(colors2)
    inds = values_avg.argsort() # sort average

    labels = labels[inds]
    values_avg = values_avg[inds]
    values_max = values_max[inds]
    colors2 = colors2[inds]
    
    y_pos = np.arange(len(values_avg))*(barheight + barspacing)
    ax.barh(y_pos, values_max*100.0, color = colors2, align = 'center')
    # ax.barh(y_pos, values_avg*100.0, facecolor = (1,1,1,0.4), align = 'center', hatch = '//')
    rects = ax.barh(y_pos, values_avg*100.0, align = 'center', facecolor = (1,1,1,0.4))
    rects = ax.barh(y_pos, values_avg*100.0, align = 'center', hatch = '////', color = 'None')
    plt.yticks(y_pos, labels)
    plt.setp(ax.get_yticklines(), visible = False)
    plt.title('Relative difference in pressure for selected pipe sections')
    plt.xlabel('Relative pressure difference [%]')
    plt.ylim([-0.5, len(y_pos) - 0.5])
    plt.xlim([0, 7.5])
    ax.grid('on', axis = 'x')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis = 'x', bottom = 'off')

    # left aligh y tick labels
    ax.yaxis.set_tick_params(pad = 0)
    # for label in ax.yaxis.get_ticklabels():
        # label.set_horizontalalignment('left')

    # Create custom artists
    artists = []
    legends = []
    for i, idx in enumerate(indices):
        artists.append(plt.Rectangle((0,0), 0, 0, facecolor = barcolors[i], edgecolor = None))
        legends.append(l[i])

    artists.append(plt.Rectangle((0,0), 0, 0, facecolor = 'lightgrey', edgecolor = None, hatch = '////'))
    # artists.append(plt.Rectangle((0,0), 0, 0, facecolor = 'none', edgecolor = 'k'))

    # Create legend from custom artist/label lists
    ax.legend(artists, legends + ['Average', 'Max'], loc = 'lower right')

    fig.tight_layout(pad = 0) # fill figure
    fig.subplots_adjust(left = 0.1) # add some space on left side, so all figures have same size in the end

    if save_figure:
        plt.savefig(
            'barchart_all_pressure_relative.pdf', 
            # dpi = 300, 
            # bbox_inches='tight', 
            # pad_inches = 0
        )



    ## temperature flow difference - average and max #####################################################
    if False:
        indices = [25, 84, 110]
        l = ['End onshore section', 'End offshore section', 'Outlet']
        barcolors = colors[1:]
        xlim = [0, 0.75]
        fig = plt.figure(figsize = figsize)
    else:
        indices = [25, 27, 55, 84, 110]
        l = ['End onshore section', '20 km offshore', '300 km offshore (midpoint)', 'End offshore section', 'Outlet']

        if True:
            barcolors = ['g', 'm', 'y', 'r', 'c']
        else:
            # greyscale gradient from inlet to outlet
            from seaborn.apionly import light_palette
            barcolors = seaborn.light_palette('k', n_colors = 5)
        xlim = [0, 1.15]
        
    fig = plt.figure(
        figsize = figsize,
        # tight_layout = {'pad' : 0}
    )
    ax = fig.add_subplot(111)

    values_avg = []
    values_max = []
    labels = []
    colors2 = []
    for j in range(len(maxDiff[0][0])): # loop over folders
        for i, idx in enumerate(indices):
            # if True:
            # if maxDiffAlong[0][2][j][idx] > 0.05: # skip some
            if use_relative_temperature:
                if maxDiffAlong[0][2][j][idx] > 0.0371: # skip some
                    values_avg.append(averageRelativeDiffAlong[0][2][j][idx])
                    values_max.append(relativeMaxDiffAlong[0][2][j][idx])
                    labels.append(dataSetLabels[j])
                    colors2.append(barcolors[i])
            else:
                if maxDiffAlong[0][2][j][idx] > 0.0371: # skip some
                    values_avg.append(averageDiffAlong[0][2][j][idx])
                    values_max.append(maxDiffAlong[0][2][j][idx])
                    labels.append(dataSetLabels[j])
                    colors2.append(barcolors[i])

    labels = np.array(labels)
    values_avg = np.array(values_avg)
    values_max = np.array(values_max)
    colors2 = np.array(colors2)

    inds = values_avg.argsort() # sort average
    # inds = values_max.argsort() # sort max error

    labels = labels[inds]
    values_avg = values_avg[inds]
    values_max = values_max[inds]
    colors2 = colors2[inds]
    
    y_pos = np.arange(len(values_avg))*(barheight + barspacing)
    if use_relative_temperature:
        factor = 100
    else:
        factor = 1
    rects = ax.barh(y_pos, values_max*factor, color = colors2, align = 'center')
    # rects = ax.barh(y_pos, values_avg, facecolor = (1,1,1,0.4), align = 'center', hatch = '//')
    rects = ax.barh(y_pos, values_avg*factor, align = 'center', facecolor = (1,1,1,0.4))
    rects = ax.barh(y_pos, values_avg*factor, align = 'center', hatch = '////', color = 'None')
    plt.yticks(y_pos, labels)
    plt.setp(ax.get_yticklines(), visible = False)
    if use_relative_temperature:
        plt.title('Relative difference in temperature for selected pipe sections')
        plt.xlabel('Relative temperature difference [%]')
        plt.xlim([0, 0.41])
    else:
        plt.title('Difference in temperature for selected pipe sections')
        plt.xlabel('Absolute temperature difference [°C]')
        plt.xlim(xlim)
    plt.ylim([-0.5, len(y_pos) - 0.5])
    ax.grid('on', axis = 'x')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis = 'x', bottom = 'off')

    # left aligh y tick labels
    ax.yaxis.set_tick_params(pad = 0)
    # for label in ax.yaxis.get_ticklabels():
        # label.set_horizontalalignment('left')

    # Create custom artists
    artists = []
    legends = []
    for i, idx in enumerate(indices):
        artists.append(plt.Rectangle((0,0), 0, 0, facecolor = barcolors[i], edgecolor = None))
        legends.append(l[i])

    artists.append(plt.Rectangle((0,0), 0, 0, facecolor = 'lightgrey', edgecolor = None, hatch = '////'))
    # artists.append(plt.Rectangle((0,0), 0, 0, facecolor = 'none', edgecolor = 'k'))

    # Create legend from custom artist/label lists
    ax.legend(artists, legends + ['Average', 'Max'], loc = 'lower right')

    fig.tight_layout(pad = 0) # fill figure
    fig.subplots_adjust(left = 0.1) # add some space on left side, so all figures have same size in the end

    if save_figure:
        plt.savefig(
            'barchart_all_temperature_absolute.pdf', 
            # dpi = 72, 
            # bbox_inches='tight', 
            # pad_inches = 0
        )



    ## one temperature figure for each point
    if False:
        for i, idx in enumerate(indices): # loop over grid points
            # fig = plt.figure(figsize = [8, 12])
            fig = plt.figure()
            ax = fig.add_subplot(111)

            values_avg = []
            values_max = []
            labels = []
            colors2 = []
            for j in range(len(maxDiff[0][0])): # loop over folders
                values_avg.append(averageDiffAlong[0][2][j][idx])
                values_max.append(maxDiffAlong[0][2][j][idx])
                labels.append(dataSetLabels[j])
                colors2.append(barcolors[i])

            labels = np.array(labels)
            values_avg = np.array(values_avg)
            values_max = np.array(values_max)
            colors2 = np.array(colors2)

            inds = values_avg.argsort() # sort average
            # inds = values_max.argsort() # sort max error

            labels = labels[inds]
            values_avg = values_avg[inds]
            values_max = values_max[inds]
            colors2 = colors2[inds]
            
            y_pos = np.arange(len(values_avg))
            rects = ax.barh(y_pos, values_max, color = colors2, align = 'center')
            rects = ax.barh(y_pos, values_avg, facecolor = (1,1,1,0.4), align = 'center'
                            , hatch = '//'
                            )
            plt.yticks(y_pos, labels)
            plt.setp(ax.get_yticklines(), visible = False)
            # plt.title('Difference in temperature for selected pipe sections (sorted by average diff.)' + l[i])
            plt.title(l[i])
            plt.xlabel('Absolute temperature difference [°C]')
            plt.ylim([-0.5, len(y_pos) - 0.5])
            plt.xlim(xlim)
            ax.grid('on', axis = 'x')


plt.show()