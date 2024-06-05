def makeTup(num, lst):
    ls = []
    for n in range(num):
        ls.append((lst[n], n))
    return ls


nT = makeTup(int(input()), list(map(int, input().split())))
mT = makeTup(int(input()), list(map(int, input().split())))
nT.sort()
mT.sort()
k = 0
i = 0
result = [None] * len(nT)
while i < len(nT):
    if k + 1 == len(mT) or \
            abs(nT[i][0] - mT[k][0]) <= abs(nT[i][0] - mT[k + 1][0]):
        result[nT[i][1]] = mT[k][1] + 1
        i += 1
    else:
        k += 1
print(*result)




print (я жив) 
