# -*- coding: utf-8 -*-
from __future__ import unicode_literals # for degree sign in strings: °C

# import warnings
# if ('maxDiff' not in locals() or maxDiff == []) or ('maxDiffAlong' not in locals() or maxDiffAlong == []):
#     # print('Error: need to import stuff first (or run using %run -i scriptname.py)!')
#     raise SystemExit('Error: need to import stuff first (or run using %run -i scriptname.py)!')

import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

save_figure = False
save_figure = True


## load files
import os
cwd = os.getcwd() # current directory
os.chdir("D:/VirtualBox VMs/Shared folder/gas_flow")

dir = "./projects/sensitivityAnalysis/internalEnergy/newUnsteady/"
project = "massFlow/"
supdir = dir + "rampDown/" + project

baseCaseDataSet = tools.loadDataSets(
    supdir = supdir,
    folders = ["default"], 
    files = files)[0]
baseCaseDataSet = baseCaseDataSet[0]
baseCaseDataSet[2][:, 1:] += 273.15; # convert temperature to Kelvin

# folder = 0 # Z factor * 1.2
folder = 11 # friction factor * 1.2
dataSets = tools.loadDataSets(
    supdir = supdir,
    folders = ["%02d" %folder], 
    files = files)[0]
dataSet = dataSets[0] # only load 1 dataSet anyway
dataSet[2][:,1:] += 273.15; # convert temperature to Kelvin

os.chdir(os.path.realpath(cwd)) # change back to original directory


## plot base case -- horizontal
if True:
    t = baseCaseDataSet[0][:,0]
    t = t/(60.0*60.0) # convert to hours

    # figsize = np.array([16, 9])/2.54
    figsize = np.array([16, 7])/2.54
    fig = plt.figure(figsize = figsize)

    axes = []

    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    axes.append(ax1);
    axes.append(ax2);
    axes.append(ax3);

    ylabels = ["Mass flow [kg/s]", "Pressure [MPa]", u"Temperature [°C]"]
    for ax, ylabel in zip(axes, ylabels):
        ax.tick_params(axis = 'y', left = 'on', right = 'off', direction = 'out')
        ax.tick_params(axis = 'x', bottom = 'on', top = 'off', direction = 'out')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.set_ylabel(ylabel)
        ax.set_xlabel("Time [h]")
        ax.set_xlim(0, 110)

    # set up grid
    from matplotlib.ticker import MultipleLocator
    locator = MultipleLocator(25)
    for ax in axes:
        ax.xaxis.set_major_locator(locator)
        ax.grid()

    ax1.plot(t, baseCaseDataSet[0][:,1], label = "Inlet")
    ax1.plot(t, baseCaseDataSet[0][:,-1], label = "Outlet", color = 'C2')
    ax1.set_ylim([175, 625])

    ax2.plot(t, baseCaseDataSet[1][:,1], label = "Inlet")
    ax2.plot(t, baseCaseDataSet[1][:,-1], label = "Outlet", color = 'C2')
    ax2.set_ylim([9.75, 19.25])

    ax3.plot(t, baseCaseDataSet[2][:,1] - 273.15, label = "Inlet")
    ax3.plot(t, baseCaseDataSet[2][:,-1] - 273.15, label = "Outlet", color = 'C2')
    ax3.set_ylim([-2.5, 35])

    fig.tight_layout(pad = 0) # fill figure
    fig.subplots_adjust(top = 0.91, bottom = 0.27) # make room for suptitle and legend

    # fig.suptitle('Inlet and outlet model values with modified parameter ' + r"$Z^{*} = 1.2 Z$")
    # fig.suptitle('Inlet and outlet results for base case, and with modified parameter ' + r"$Z$")
    fig.suptitle('Inlet and outlet results for base case, and with modified friction factor')
    ax2.legend(loc = 'lower center', fontsize = 10, ncol = 3, bbox_to_anchor = [0.5, -0.01], bbox_transform = fig.transFigure)

    if True:
        ax3.set_ylim([-1, 2.4])

    # if save_figure:
    #     plt.savefig(
    #         'base_case_horiz.pdf'
    #         # , dpi = 300
    #         # , bbox_inches="tight"
    #         , pad_inches = 0
    #     )

    adjustedLabel = "Modified parameter"
    # adjustedLabel = r"$Z^{*} = 1.2 Z$";

    # add adjusted parameter plot (Z factor)
    ax1.plot(t, dataSet[0][:,-1], '--', label = adjustedLabel, color = 'C3')
    ax2.plot(t, dataSet[1][:,1], '--', label = adjustedLabel, color = 'C3')
    ax2.set_ylim([9.75, 20.5])
    ax3.plot(t, dataSet[2][:,-1] - 273.15, '--', label = adjustedLabel, color = 'C3')

    ax2.legend(loc = 'lower center', fontsize = 10, ncol = 3, bbox_to_anchor = [0.5, -0.02], bbox_transform = fig.transFigure) # update legend

    if save_figure:
        plt.savefig(
            'base_case_with_adjusted_Z_horiz.pdf', 
            # dpi = 300, 
            # bbox_inches="tight", 
            pad_inches = 0
        )

# if True:
if False:
    # plot base case using gridspec
    from matplotlib.gridspec import GridSpec
    t = baseCaseDataSet[0][:,0]
    t = t/(60.0*60.0) # convert to hours

    n_rows = 3
    n_cols = 1
    gs = GridSpec(n_rows, n_cols)
    gs.update(
        hspace = 0.1
        # , wspace = 0.03
        ) # reduce spacing

    # figsize = np.array([8., 5.975])/2.0
    figsize = [5.69/2, 7]
    fig = plt.figure(figsize = figsize)

    axes = []

    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1], sharex=ax1)
    ax3 = fig.add_subplot(gs[2], sharex=ax1)
    axes.append(ax1);
    axes.append(ax2);
    axes.append(ax3);

    ylabels = ["Mass flow [kg/s]", "Pressure [MPa]", u"Temperature [°C]"]
    for ax, ylabel in zip(axes, ylabels):
        ax.tick_params(axis = 'y', left = 'on', right = 'off', direction = 'out')
        ax.tick_params(axis = 'x', bottom = 'on', top = 'off', direction = 'out')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.set_ylabel(ylabel)

    # remove x tick labels
    plt.setp(ax1.get_xticklabels(), visible = False)
    plt.setp(ax2.get_xticklabels(), visible = False)

    # set x title and limits
    ax3.set_xlabel("Time [h]")
    # ax3.set_xlim(0, np.max(t))
    ax3.set_xlim(0, 110)

    ax1.plot(t, baseCaseDataSet[0][:,1], label = "Inlet")
    ax1.plot(t, baseCaseDataSet[0][:,-1], label = "Outlet", color = 'C2')
    ax1.set_ylim([175, 625])

    ax2.plot(t, baseCaseDataSet[1][:,1], label = "Inlet")
    ax2.plot(t, baseCaseDataSet[1][:,-1], label = "Outlet", color = 'C2')
    ax2.set_ylim([9.75, 19.25])

    ax3.plot(t, baseCaseDataSet[2][:,1] - 273.15, label = "Inlet")
    ax3.plot(t, baseCaseDataSet[2][:,-1] - 273.15, label = "Outlet", color = 'C2')
    ax3.set_ylim([-2.5, 35])

    # lgd = plt.legend(bbox_to_anchor=(0.5,4.4), loc='upper center', ncol=2, fontsize = 12, frameon = 0)
    ax2.legend(loc = 'best', fontsize = 10)

    # plt.show()

    if save_figure:
        plt.savefig('base_case.pdf', dpi = 300, bbox_inches="tight", pad_inches = 0);

    # add adjusted parameter plot (Z factor)
    ax1.plot(t, dataSet[0][:,-1], '--', label = adjustedLabel, color = 'C3')
    ax2.plot(t, dataSet[1][:,1], '--', label = adjustedLabel, color = 'C3')
    ax2.set_ylim([9.75, 20.5])
    ax3.plot(t, dataSet[2][:,-1] - 273.15, '--', label = adjustedLabel, color = 'C3')

    ax2.legend(loc = 'best', fontsize = 10) # update legend

    if save_figure:
        plt.savefig('base_case_with_adjusted_Z.pdf', dpi = 300, bbox_inches="tight", pad_inches = 0);

if False:
    # plot base case using gridspec -- two columns

    from matplotlib.gridspec import GridSpec
    t = baseCaseDataSet[0][:,0]
    t = t/(60.0*60.0) # convert to hours

    n_rows = 3
    n_cols = 2
    gs = GridSpec(n_rows, n_cols)
    gs.update(
        hspace = 0.1
        , wspace = 0.05
        ) # reduce spacing

    # figsize = np.array([8., 5.975])/2.0
    figsize = [5.69, 7]
    fig = plt.figure(figsize = figsize)

    # axes = [[] for _ in range(3)]
    # axes = numpy.zeros((5, 5))

    ax20 = fig.add_subplot(gs[2,0])
    ax00 = fig.add_subplot(gs[0,0], sharex = ax20)
    ax10 = fig.add_subplot(gs[1,0], sharex = ax20)
    
    ax21 = fig.add_subplot(gs[2,1])
    ax01 = fig.add_subplot(gs[0,1], sharex = ax21)
    ax11 = fig.add_subplot(gs[1,1], sharex = ax21)

    axes = np.array([[ax00, ax01], [ax10, ax11], [ax20, ax21]])

    for ax in np.stack(axes.flat): # all axes
        # remove top ticks, make bottom ticks outside
        ax.tick_params(axis = 'x', bottom = 'on', top = 'off', direction = 'out')

        # remove top spines
        ax.spines['top'].set_visible(False)

    for ax in axes[:,0]: # first column
        # remove right tick, make left tick marks outside
        ax.tick_params(axis = 'y', left = 'on', right = 'off', direction = 'out')

        # remove right spines
        ax.spines['right'].set_visible(False)

    for ax in np.stack(axes[:,1]): # second column
        # remove left tick, make right tick marks outside
        ax.tick_params(axis = 'y', left = 'off', right = 'on', direction = 'out')

        # remove top and left spines
        ax.spines['left'].set_visible(False)

    # move y ticks to the right
    for ax in axes[:, 1]: # second column
        ax.yaxis.tick_right()

    # set y labels
    ylabels = ["Mass flow [kg/s]", "Pressure [MPa]", u"Temperature [°C]"]
    for ax, ylabel in zip(axes[:,0], ylabels): # first column
        ax.set_ylabel(ylabel)
    # for ax, ylabel in zip(axes[:,1], ylabels): # second column
    #     ax.set_ylabel(ylabel)

    # remove x tick labels
    for ax in np.stack(axes[:2].flat):
        plt.setp(ax.get_xticklabels(), visible = False)

    # set x title and limits
    ax20.set_xlabel("Time [h]")
    ax21.set_xlabel("Time [h]")
    ax20.set_xlim(0, 110)
    ax21.set_xlim(0, 110)

    ax00.plot(t, baseCaseDataSet[0][:,1], label = "Inlet")
    for ax in [ax00, ax01]:
        ax.plot(t, baseCaseDataSet[0][:,-1], label = "Outlet")
        ax.set_ylim([175, 625])

    ax01.plot(t, dataSet[0][:,-1], '--', label = 'Adjusted parameter', color = 'r')

    ax10.plot(t, baseCaseDataSet[1][:,-1], label = "Outlet", color = 'g')
    for ax in [ax10, ax11]:
        ax.plot(t, baseCaseDataSet[1][:,1], label = "Inlet", color = 'b')
        ax.set_ylim([9.75, 19.25])

    ax11.plot(t, dataSet[1][:,1], '--', label = 'Adjusted parameter', color = 'r')
    ax11.set_ylim([11, 20.5])

    ax20.plot(t, baseCaseDataSet[2][:,1] - 273.15, label = "Inlet")
    ax20.plot(t, baseCaseDataSet[2][:,-1] - 273.15, label = "Outlet")
    ax20.set_ylim([-2.5, 35])

    lgd = ax00.legend(bbox_to_anchor = (1.0, 1.1), loc='center', ncol=2, fontsize = 10, frameon = 0)

    # # add adjusted parameter plot (Z factor)
    # axes[4].plot(t, dataSet[0][:,-1], '--', label = 'Adjusted parameter', color = 'r')
    # ax2.plot(t, dataSet[1][:,1], '--', label = 'Adjusted parameter', color = 'r')
    # ax2.set_ylim([9.75, 20.5])
    # ax3.plot(t, dataSet[2][:,-1] - 273.15, '--', label = 'Adjusted parameter', color = 'r')

    # ax2.legend(loc = 'best', fontsize = 10) # update legend

    plt.show()
    # plt.savefig(
    #     'base_case_2col_with_adjusted_Z.pdf', 
    #     bbox_extra_artists=(lgd,),
    #     dpi = 300, 
    #     bbox_inches="tight", 
    #     pad_inches = 0
    #     );

plt.show()