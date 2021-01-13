def count(n, m1, m):
    j = 0
    for i in range(n[1]):
        m1 += m[i]
        if m1 <= n[0]:
            j += 1
    return j


n = list(map(int, input().split()))
m = []
for i in range(n[1]):
    m.extend(list(map(int, input().split())))
m.sort()
m1 = 0
print(count(n, m1, m))
