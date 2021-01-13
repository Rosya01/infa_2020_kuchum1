def merge(a, b):
    countA = 0
    countB = 0
    c = list()
    for i in range(0, len(a) + len(b)):
        if len(a) > countA and len(b) > countB:
            if a[i - countB] > b[i - countA]:
                c.append(b[i - countA])
                countB += 1
            else:
                c.append(a[i - countB])
                countA += 1
        else:
            if len(a) > countA:
                c.extend(a[countA:])
                break
            else:
                c.extend(b[countB:])
                break
    return c


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*merge(A, B))
