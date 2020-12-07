import math
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(S)
