def find_min(a, b, c, d):
    return min(a, min(b, min( c, d)))


nums = list(map(int, input().split()))
a = nums[0]
b = nums[1]
c = nums[2]
d = nums[3]
print(find_min(a,b,c,d))