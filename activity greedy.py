n = int(input())
a = []
for i in range(n):
    s, e = map(int, input().split())
    a.append((s, e))
a.sort(key = lambda x: x[1])
c = 0
le = 0

for s, e in a:
    if s >= le:
        c += 1
        le = e
print(c)