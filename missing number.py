n = int(input())
a = list(map(int, input().split()))
t = n * (n+1) // 2
m = t - sum(a)
print(m)