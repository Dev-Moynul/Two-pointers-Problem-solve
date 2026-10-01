n, x = map(int, input().split())
lst = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append((lst[i], i+1))
    #print(arr)

arr.sort()
l, r = 0, n-1
t = x
flag = False
while l < r:
    sum = arr[l][0] + arr[r][0]
    if sum == x:
        flag = True
        break
    elif sum < x:
        l += 1
    else:
        r -=1
if flag == True:
    print(arr[l][1], arr[r][1] )
else:
    print("IMPOSSIBLE")
    
