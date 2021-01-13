s = [int(i) for i in input().split()]
a = list(filter(lambda s: s % 2 == 0, s))
print(*a)
