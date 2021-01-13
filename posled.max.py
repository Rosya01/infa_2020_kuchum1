s = [int(i) for i in input().split()]
print(max(s), len(s) - 1 - s[::-1].index(max(s)))
