
i = 35
j = 86
idx = 2 # temperature

a = np.array(averageDiffAlong[0][idx])
print('average temperature diff between %d and %d km = %1.4f Celsius' %(x[i], x[j], np.max(a[:, i:j])))
a = np.array(maxDiffAlong[0][idx])
print('max temperature diff between %d and %d km = %1.4f Celsius' %(x[i], x[j], np.max(a[:, i:j])))

print()
a = np.array(averageRelativeDiffAlong[0][idx])*100
print('average temperature diff between %d and %d km = %1.4f %%' %(x[i], x[j], np.max(a[:, i:j])))
a = np.array(relativeMaxDiffAlong[0][idx])*100
print('max temperature diff between %d and %d km = %1.4f %%' %(x[i], x[j], np.max(a[:, i:j])))

