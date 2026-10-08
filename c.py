n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
l = 0
r = 0
cnt = 0

while l < n and r < m :
    if b[r] < a[l] - k :
        r += 1 
#print(r) 
    elif b[r] > a[l] + k:
        l += 1
    else:
        cnt += 1
        l += 1
        r += 1
print(cnt)