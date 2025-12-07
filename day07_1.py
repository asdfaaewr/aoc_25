day, test = 7, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()
    data =[[*line] for line in data]

tot = 0
for r in range(1, len(data)):
    for c in range(len(data[0])):
        if data[r-1][c] in ('S', '|'):
            if data[r][c] == '^':
                data[r][c-1] = '|'
                data[r][c+1] = '|'
                tot += 1
            else:
                data[r][c] = '|'

print(tot)
