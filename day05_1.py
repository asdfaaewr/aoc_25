day, test = 5, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    ranges, ing = file.read().split('\n\n')

ranges = ranges.split()

tot = 0

for i in ing.split():
    for r in ranges:
        start, end = r.split('-')
        if int(i) in range(int(start), int(end)+1):
            tot += 1
            break

print(tot)