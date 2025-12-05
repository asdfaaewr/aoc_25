day, test = 5, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    ranges =  [[int(y) for y in x.split('-')] for x in file.read().split('\n\n')[0].splitlines()]

tot, highest = 0, 0

for r in sorted(ranges):
    tot += max(0, r[1] - max(highest, r[0]-1))
    highest = max(highest, r[1])

print(tot)