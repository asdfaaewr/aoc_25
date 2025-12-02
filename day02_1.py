day, test = 2, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().split(',')

tot = 0

for r in data:
    start, end =  [int(x) for x in r.split('-')]

    for n in range(start, end+1):
        l = len(str(n))
        if l % 2 == 0: 
            if str(n)[0:l//2] == str(n)[l//2:]:
                tot += n
print(tot)
