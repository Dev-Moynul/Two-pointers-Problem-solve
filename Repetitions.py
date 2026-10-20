a = input()
c = 1
m = 1
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        c += 1
    else:
        c = 1
    m = max(m, c)
print(m)