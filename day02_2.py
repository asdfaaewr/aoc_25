from collections import Counter

day, test = 2, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().split(',')

tot = 0

for r in data:
    start, end =  [int(x) for x in r.split('-')]

    for n in range(start, end+1):
        l = len(str(n))
        for i in range(1, l//2+1):
            if l % i == 0: 

                first = str(n)[0:i]
                for k in range(1, l//i):
                    if str(n)[0: i] != str(n)[k * i: (k+1) * i]:
                        break
                else:
                    tot += n
                    break
print(tot)
