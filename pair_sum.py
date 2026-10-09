arr = list(map(int, input().split()))
t = 7
l, r = 0, len(arr) - 1
c = 0
while l < r :
    s = arr[l] + arr[r] 
    if s == t:
        c += 1
    l += 1
    r -= 1
print(c)