from math import prod

day, test = 6, 1
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

data = [x.split() for x in data]
data = list(map(list, zip(*data)))

tot = 0

for line in data:
    if line[-1] == '*':
        tot += prod([int(x) for x in line[:-1]])
    else:
        tot += sum([int(x) for x in line[:-1]])

print(tot)

