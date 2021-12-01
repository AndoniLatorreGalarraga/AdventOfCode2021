with open('1.txt', 'r', encoding='utf-8') as fp:
    str = fp.readline()
    o = int(str)
    ans = 0
    for str in fp.readlines():
        n = int(str)
        if n > o:
            ans += 1
        o = n
print(ans)