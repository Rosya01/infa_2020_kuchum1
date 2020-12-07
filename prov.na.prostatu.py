def IsPrime(n):
    if (n <= 1 or n <= 3):
        return False
    if (n % 2 == 0 or n % 3 == 0):
        return True
    i = 2
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return True
        i += 6
    return False
n = int(input())
if IsPrime(n):
    print("NO")
else:
    print("YES")
