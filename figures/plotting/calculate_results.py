#!/usr/local/bin/python3

# python 3 compatible yes/no question
def query_yes_no(question, default = True):
    """Ask a yes/no question via standard input and return the answer.

    If invalid input is given, the user will be asked until
    they acutally give valid input.

    Args:
        question(str):
            A question that is presented to the user.
        default(bool|None):
            The default value when enter is pressed with no value.
            When None, there is no default value and the query
            will loop.
    Returns:
        A bool indicating whether user has entered yes or no.

    Side Effects:
        Blocks program execution until valid input(y/n) is given.
    """
    yes_list = ["yes", "y"]
    no_list = ["no", "n"]

    default_dict = {  # default => prompt default string
        None: "[y/n]",
        True: "[Y/n]",
        False: "[y/N]",
    }

    default_str = default_dict[default]
    prompt_str = "%s %s " % (question, default_str)

    while True:
        choice = input(prompt_str).lower()

        if not choice and default is not None:
            return default
        if choice in yes_list:
            return True
        if choice in no_list:
            return False

        notification_str = "Please respond with 'y' or 'n'"
        print(notification_str)

def main():

    alreadyLoaded = True
    if 'maxDiff' not in locals() or maxDiff == []:
        alreadyLoaded = False

    run = False
    if alreadyLoaded:
        run = query_yes_no('Variables already in memory. Really run calculation?', default = False)
    else:
        run = query_yes_no('Really run calculation?', default = True)
    if not run:
        raise SystemExit

    import numpy as np

    x1 = np.linspace(0, 25, 26)*1000.0;
    x2 = (np.linspace(0, 600, 60 + 1) + 25.0)*1000.0;
    x2 = x2[1:];
    x3 = np.linspace(625 + 1, 650, 25)*1000.0;
    x = np.concatenate((x1, x2, x3));

    dir = "./projects/sensitivityAnalysis/internalEnergy/newUnsteady/"
    # supdir = dir + "rampDown/" + "massFlow/"
    # supdir = dir + "rampDown/" + "temperatureAndMassFlow/"
    # projects = ["massFlow/", "temperatureAndMassFlow/"]
    projects = ["massFlow/"]

    files = [0, 1, 2]
    # folders = range(13)
    folders = [
        0, 1, 2, 3,     # Z and derivatives
        # 4, 5, 7, 8, 9,  # ho, hi, (lambda_gas, c_p, c_v)
        4, 5, 9,  # ho, hi, c_v
        # 6, 10, 11   # diameter, visc, friction 1.2
        10, 11   # visc, friction 1.2
    ] # lambda_gas and c_p effectively the same as h_inner, so skip those

    # dataSetLabels = [
    #     r"$Z$",            # 0
    #     r"$\partial Z/\partial p\/|_T$",         # 1
    #     r"$\partial Z/\partial T\/|_p$",       # 2
    #     r"$\partial Z/\partial T\/|_\rho$",     # 3
    #     r"$h_\mathrm{seawater}$",   # 4
    #     r"$h_\mathrm{inner}$",      # 5
    #     r"D 0.1\%", # 6
    #     r"$\lambda_\mathrm{gas}$",   # 7
    #     r"$c_p$ (gas)",          # 8
    #     r"$c_v$ (gas)",          # 9
    #     r"Viscosity",    # 10
    #     r"Friction", # 11
    #     r"Friction 1.01",# 12
    #     r"Ambient temp." # 13
    # ]
    dataSetLabels = [
        r"$Z$",            # 0
        r"$\partial Z/\partial p\/|_T$",         # 1
        r"$\partial Z/\partial T\/|_p$",       # 2
        r"$\partial Z/\partial T\/|_\rho$",     # 3
        r"$h_\mathrm{outer}$",   # 4
        r"$h_\mathrm{inner}$",      # 5
        r"D 0.1\%", # 6
        r"$\lambda_\mathrm{gas}$",   # 7
        r"$c_p$ (gas)",          # 8
        r"$c_v$ (gas)",          # 9
        r"$\mu$ (gas)",    # 10
        r"$f$", # 11
        r"Friction 1.01",# 12
        r"Ambient temp." # 13
    ]
    dataSetLabels = [dataSetLabels[i] for i in folders] # rearrange to same order as dataSets


    if True:
    # if False:
        # data was saved using 
        # 'np.savez('data.npz', maxDiff, relativeMaxDiff, maxDiffAlong, averageDiffAlong, relativeMaxDiffAlong, averageRelativeDiffAlong)''
        # data = np.load('data.npz')
        # maxDiff, relativeMaxDiff, maxDiffAlong, averageDiffAlong, relativeMaxDiffAlong, averageRelativeDiffAlong = (data[k] for k in data)
        import pickle
        PIK = "pickle.dat"

        with open(PIK, "rb") as f:
            maxDiff, relativeMaxDiff, maxDiffAlong, averageDiffAlong, relativeMaxDiffAlong, averageRelativeDiffAlong = pickle.load(f)

    else:
        import os
        cwd = os.getcwd()
        os.chdir("D:/VirtualBox VMs/Shared folder/gas_flow")
        from tools import tools

        maxDiff =         [[] for j in range(len(projects))]
        relativeMaxDiff = [[] for j in range(len(projects))]

        maxDiffAlong =             [[[[] for k in range(len(folders))] for i in range(3)] for j in range(len(projects))]
        averageDiffAlong =         [[[[] for k in range(len(folders))] for i in range(3)] for j in range(len(projects))]
        relativeMaxDiffAlong =     [[[[] for k in range(len(folders))] for i in range(3)] for j in range(len(projects))]
        averageRelativeDiffAlong = [[[[] for k in range(len(folders))] for i in range(3)] for j in range(len(projects))]

        for projectIdx, project in enumerate(projects):
            supdir = dir + "rampDown/" + project

            baseCaseDataSet = tools.loadDataSets(
                supdir = supdir,
                folders = ["default"], 
                files = files)[0]
            baseCaseDataSet = baseCaseDataSet[0]
            baseCaseDataSet[2][:, 1:] += 273.15; # convert temperature to Kelvin

            maxDiff[projectIdx] =         np.zeros([3, len(folders)])
            relativeMaxDiff[projectIdx] = np.zeros([3, len(folders)])
            for folderIdx, folder in enumerate(folders):
                dataSets = tools.loadDataSets(
                    supdir = supdir,
                    folders = ["%02d" %folder], 
                    files = files)[0]
                dataSet = dataSets[0] # only load 1 dataSet anyway
                dataSet[2][:,1:] += 273.15; # convert temperature to Kelvin

                # calculate overall max difference
                for j in range(3): # loop over massFlow, pressure, temperature
                    baseCase = baseCaseDataSet[j][:, 1:]
                    absDiff = np.abs(dataSet[j][:, 1:] - baseCase)
                    
                    maxDiff[projectIdx][j, folderIdx] = np.max(absDiff);

                    idx = np.argmax(absDiff/baseCase) # returns FLAT index
                    # use ndarray.flat[idx] to index using flat index
                    relativeMaxDiff[projectIdx][j, folderIdx] = np.abs(absDiff.flat[idx]/baseCase.flat[idx])

                # calculate max difference for each pipeline section
                nGridPoints = np.shape(dataSet)[2] - 1
                for j in range(3): # loop over massFlow, pressure, temperature
                    maxDiffAlong            [projectIdx][j][folderIdx] = np.zeros(nGridPoints)
                    averageDiffAlong        [projectIdx][j][folderIdx] = np.zeros(nGridPoints)
                    relativeMaxDiffAlong    [projectIdx][j][folderIdx] = np.zeros(nGridPoints)
                    averageRelativeDiffAlong[projectIdx][j][folderIdx] = np.zeros(nGridPoints)
                    for i in range(0, nGridPoints):
                        baseCase = baseCaseDataSet[j][:, i+1]
                        absDiff = np.abs(dataSet[j][:, i+1] - baseCase)

                        maxDiffAlong            [projectIdx][j][folderIdx][i] = np.max(absDiff);
                        averageDiffAlong        [projectIdx][j][folderIdx][i] = np.average(absDiff);
                        averageRelativeDiffAlong[projectIdx][j][folderIdx][i] = np.average(absDiff/baseCase);

                        idx = np.argmax(absDiff/baseCase) # returns FLAT index
                        # use ndarray.flat[idx] to index using flat index
                        relativeMaxDiffAlong[projectIdx][j][folderIdx][i] = np.abs(absDiff.flat[idx]/baseCase.flat[idx])
        # change back to dir where we started
        os.chdir(os.path.realpath(cwd))

        # save to file
        # np.savez('data.npz', maxDiff, relativeMaxDiff, maxDiffAlong, averageDiffAlong, relativeMaxDiffAlong, averageRelativeDiffAlong)
        import pickle
        PIK = "pickle.dat"

        data = [maxDiff, relativeMaxDiff, maxDiffAlong, averageDiffAlong, relativeMaxDiffAlong, averageRelativeDiffAlong]
        with open(PIK, "wb") as f:
            pickle.dump(data, f)

    return locals()

if __name__ == '__main__':
    import os
    cwd = os.getcwd()
    try:
        new_locals = main()
        locals().update(new_locals)
    except KeyboardInterrupt:
        # change back to dir where we started if we are interrupted
        os.chdir(os.path.realpath(cwd))
        raise SystemExit('KeyboardInterrupt, exiting cleanly')