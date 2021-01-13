def zxc(a1, n1):
    if n1 > 1:
        a1 = a1 * zxc(a1, n1 - 1)
    else:
        a1 = a1 ** n1
    return a1


a, n = float(input()), float(input())
print(zxc(a, n))
