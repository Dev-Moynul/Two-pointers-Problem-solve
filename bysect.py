from bisect import bisect_right

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
for x in b:
    print(bisect_right(a, x), end=" ")