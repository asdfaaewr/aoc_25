from math import prod

day, test = 6, 1
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

ops = data[-1]
ops_pos = []
for i, c in enumerate(ops):
    if c in ('+', '*'):
        ops_pos.append(i)

ops_pos.append(len(ops)+1)

data = [[n.replace(' ', '0') for n in [line[ops_pos[i]:ops_pos[i+1]-1] for i in range(len(ops_pos)-1)]] for line in data[:-1]]
data = [[''.join(l) for l in zip(*line)] for line in list(map(list, zip(*data)))]

tot = 0
ops = ops.split()

for i, line in enumerate(data):
    line = [str(int(l[::-1]))[::-1] for l in line]
    if ops[i] == '*':
        tot += prod([int(x) for x in line])
    else:
        tot += sum([int(x) for x in line])

print(tot)

