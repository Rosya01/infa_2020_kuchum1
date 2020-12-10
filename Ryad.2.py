a = int(input())
b = int(input())
if a != b:
    for i in range(a, b + 1):
        if a < b:
            print(i, end=" ")
    for j in range(a, b - 1, -1):
        if a > b:
            print(j, end=" ")
else:
    print(a)
