n = map(int, input().split())
grades = [0] * 101
for i in n:
    grades[i] += 1
for j in range(len(grades)):
    for i in range(grades[j]):
        print(j, end=' ')
