# part 1
h, d = 0, 0
with open('2.txt', 'r', encoding='utf-8') as fp:
    for line in fp.readlines():
        l = line.split()
        n = int(l[1])
        if l[0] == 'forward':
            h += n
        elif l[0] == 'down':
            d += n
        elif l[0] == 'up':
            d -= n
print(h*d) #2322630
# part 2
h, d, a = 0, 0,0
with open('2.txt', 'r', encoding='utf-8') as fp:
    for line in fp.readlines():
        l = line.split()
        n = int(l[1])
        if l[0] == 'forward':
            h += n
            d += a*n
        elif l[0] == 'down':
            a += n
        elif l[0] == 'up':
            a -= n
print(h*d) #2105273490