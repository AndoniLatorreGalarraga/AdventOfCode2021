# part 1
count = [0]*12
lines = 0
with open('3.txt', 'r', encoding='utf-8') as fp:
    for line in fp.readlines():
        lines += 1
        for i in range(12):
            count[i] += int(line[i])
    gamma, epsilon = '', ''
    for i in range(12):
        if count[i] > lines/2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
print(int(gamma, base=2)*int(epsilon, base=2)) # 4103154
# part 2
with open('3.txt', 'r', encoding='utf-8') as fp:
    ox = []
    co = []
    for line in fp.readlines():
        ox += line.split()
        co += line.split()
bit = 0
while len(ox) > 1:
    zeros = 0
    ones = 0
    delete = []
    for n in ox:
        if n[bit] == '1':
            ones += 1
        else:
            zeros += 1
    if zeros > ones:
        for i in ox:
            if i[bit] == '1':
                delete.append(i)
    else:
        for i in ox:
            if i[bit] == '0':
                delete.append(i)
    for d in delete:
        ox.remove(d)
    bit += 1
bit = 0
while len(co) > 1:
    zeros = 0
    ones = 0
    delete = []
    for n in co:
        if n[bit] == '1':
            ones += 1
        else:
            zeros += 1
    if zeros > ones:
        for i in co:
            if i[bit] == '0':
                delete.append(i)
    else:
        for i in co:
            if i[bit] == '1':
                delete.append(i)
    for d in delete:
        co.remove(d)
    bit += 1
print(int(ox[0], base=2)*int(co[0], base=2)) #4245351