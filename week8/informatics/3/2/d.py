import math

a = int(input())
i = 0
n = 1
d = 0
while n <= a:
    i += 1
    if n==a:
        print('YES')
        exit()
    while d != i:
        n *= 2
        d+=1
print('NO')