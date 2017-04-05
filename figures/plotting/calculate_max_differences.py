
i = 35
j = 86
idx = 2 # temperature

# a = np.array(averageDiffAlong[0][idx])
# print('average temperature diff between %d and %d km = %1.4f Celsius' %(x[i], x[j], np.max(a[:, i:j])))
# a = np.array(maxDiffAlong[0][idx])
# print('max temperature diff between %d and %d km = %1.4f Celsius' %(x[i], x[j], np.max(a[:, i:j])))

print()
a = np.array(averageRelativeDiffAlong[0][idx])*100
print('highest average temperature diff between %d and %d km = %1.4f %%' %(x[i], x[j-1], np.max(a[:, i:j])))

a = np.array(relativeMaxDiffAlong[0][idx])*100
print('highest max temperature diff between %d and %d km = %1.4f %%' %(x[i], x[j-1], np.max(a[:, i:j])))

for k in [2,6]:
    a = averageRelativeDiffAlong[0][2][k][j-1]*100
    b = averageRelativeDiffAlong[0][2][k][j]*100
    print(b/a)
    # k = 6
    print('difference for %s at %d = %1.5f' %(dataSetLabels[k], x[j-1], a))
    print('difference for %s at %d = %1.5f' %(dataSetLabels[k], x[j], b))