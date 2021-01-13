import math
a = float(input())
b = float(input())
c = float(input())
if b == 0 and c == 0:
    print(0)
elif b != 0 and c == 0:
    x1 = 0
    x2 = -(b / a)
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)
elif b == 0 and c != 0:
    if c < 0:
        x1 = math.sqrt(- c)
        x2 = -(math.sqrt(- c))
        if x1 > x2:
            print(x2, x1)
        else:
            print(x1, x2)
else:
    d = (b ** 2) - 4 * a * c
    if d == 0:
        x = -(b / (2 * a))
        print(x)
    elif d < 0:
        print()
    else:
        x1 = -((b + math.sqrt(d)) / (2 * a))
        x2 = -((b - math.sqrt(d)) / (2 * a))
        if x1 > x2:
            print(x2, x1)
        else:
            print(x1, x2)
