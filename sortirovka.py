n = int(input())
a = list(map(int, input().split()[:n]))
print(*sorted(a))

