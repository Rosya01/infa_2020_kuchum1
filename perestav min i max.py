s = list(map(int, input().split()))
a = s.index(max(s))
b = s.index(min(s))
s[a], s[b] = s[b], s[a]
print(*s)
