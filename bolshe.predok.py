s = [int(i) for i in input().split()]
print(*[s[i + 1] for i in range(len(s) - 1) if s[i] < s[i + 1]], sep=' ')
