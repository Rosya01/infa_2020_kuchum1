n = int(input())
A = list(map(int, input().split()))
k = int(input())
B = A.copy()
for i in range(len(A)):
    B[i] = k
for i in range(len(A)):
    B[i] = abs(B[i] - A[i])
Bk = min(B)
BkInd = B.index(Bk)
print(A[BkInd])
