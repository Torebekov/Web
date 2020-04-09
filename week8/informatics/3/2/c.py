import math

a = int(input())
i = 0
n = 1
d = 0
while n <= a:
    print(n)
    i += 1
    while d != i:
        n *= 2
        d+=1
