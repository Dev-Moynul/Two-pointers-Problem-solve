def do(l):
    n = l.copy()
    for i in range(1, len(l)-1):
        if l[i-1] == l[i+1] == '1':
            n[i] = '1' if l[i] == '0' else '0'
    return n

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())

    # print(s)
    for _ in range(min(4, k)):
        s = do(s)
        # print(_+1, s)
    
    if k > 4:
        if k%2:
            s = do(s)
    print(''.join(s))