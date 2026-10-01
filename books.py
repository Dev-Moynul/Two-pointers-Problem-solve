n, t = map(int, input().split())
a = list(map(int, input().split()))
l, m, rlt = 0, 0, 0

for r in range(n):
    m += a[r]
    while m > t:
        m -= a[l]
        l += 1
    rlt = max(rlt, r - l + 1)
print(rlt)