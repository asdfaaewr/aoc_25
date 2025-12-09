day, test = 9, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()
    data = [[int(e) for e in line.split(',')] for line in data]

tot = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        tot = max(tot, (1+data[i][0]-data[j][0]) *  (1+data[i][1]-data[j][1]))

print(tot)