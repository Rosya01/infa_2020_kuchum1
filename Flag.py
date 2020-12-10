n = int(input())
for i in range(n):
    print("+___", end=" ")
print()
for i in range(1, n+1):
    print('|', i, " / ", sep='', end="")
print()
for i in range(n):
    print("|__\\", end=" ")
print()
for i in range(n):
    print("|   ", end=" ")
print()
