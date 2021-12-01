# part 1
with open('1.txt', 'r', encoding='utf-8') as fp:
    s = fp.readline()
    o = int(s)
    ans = 0
    for s in fp.readlines():
        n = int(s)
        if n > o:
            ans += 1
        o = n
print(ans) #1387
# part 2
with open('1.txt', 'r', encoding='utf-8') as fp:
    l = []
    for _ in range(3):
        l.append(int(fp.readline()))
    ans = 0
    for s in fp.readlines():
        n = int(s)
        if l[0] < n: #l[0]+l[1]+l[2] < l[1]+l[2]+n
            ans += 1
        l.pop(0)
        l.append(n)
print(ans) #1362