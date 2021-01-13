n = int(input())
myList = []
for now in range(n):
    myList.append(list(map(str, input().split())))

myList.sort(key=lambda p: int(p[1]) * -1)
for i in myList:
    print(i[0])
