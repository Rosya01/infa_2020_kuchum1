inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
a = []
for line in inFile:
    a.append(line.split())
a.sort()
inFile.close()
for i in range(len(a)):
    print(*a[i][:2], a[i][3], file=outFile)
