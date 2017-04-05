if False:
    m = np.average(averageRelativeDiffAlong[0][0], 1)
    p = np.average(averageRelativeDiffAlong[0][1], 1)
    # T = np.average(averageDiffAlong[0][2], 1)
    T = np.average(averageRelativeDiffAlong[0][2], 1)

    avgs = zip(m, p, T)
else:
    dx = x[1:]-x[0:-1]
    L = np.sum(dx)

    n = len(averageRelativeDiffAlong[0][0])
    avgs = np.zeros([n, 3])
    for i in range(3): # loop over m, p, T
        for j in range(n): # loop over data sets
            y = averageRelativeDiffAlong[0][i][j]
            avgs[j, i] = np.sum((y[1:] + y[0:-1])/2*(dx))/L

labels = [
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
labels[1] = r"$\eval{\partial Z/\partial p}_T$"
labels[2] = r"$\eval{\partial Z/\partial T}_p$"
labels[3] = r"$\eval{\partial Z/\partial T}_\rho$"
labels = [labels[i] for i in folders] # rearrange to same order as dataSets


for idx, avg in enumerate(avgs):
    # avg[0] = avg[0]*100
    # avg[1] = avg[1]*100
    print('%s & %1.4f & %1.4f & %1.4f \\\\' %(labels[idx], avg[0]*100, avg[1]*100, avg[2]*100))

print()
for i in range(3):
    a = np.sort(avgs[:,i])
    den = a[-3]
    print(a[-1]/den)
    print(a[-2]/den)
    print()