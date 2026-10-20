n, b = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
c = 0
for i in p:
    if b >= i:
        b -= i
        c += 1
    else:
        break
print(c)