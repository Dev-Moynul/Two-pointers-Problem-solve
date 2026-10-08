n, x = map(int, input().split())
arr =list(map(int, input().split()))
arr.sort()
l, r = 0, len(arr)-1        
cnt = 0
while l <= r:
    # cnt = 0
    if arr[l] + arr[r] <= x:
        l += 1
    r -= 1
    cnt += 1
print(cnt)