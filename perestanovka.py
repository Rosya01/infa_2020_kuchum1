n = list(map(int, input().split()))
for i in range(len(n)):
    if i % 2 != 0:
        n[i], n[i - 1] = n[i - 1], n[i]
print(*n)
