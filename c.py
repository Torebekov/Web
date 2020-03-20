def xor(a, b):
    if a == 1 and b == 1: return 0
    if a == 0 and b == 0: return 0
    return 1


arr = list(map(int, input().split()))
a = arr[0]
b = arr[1]
print(xor(a, b))
