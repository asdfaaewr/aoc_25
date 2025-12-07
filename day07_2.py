day, test = 7, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()
    data =[[*line] for line in data]

for r in range(0, len(data)):
    for c in range(len(data[0])):
        if data[r][c] == 'S': data[r][c] = 1
        if data[r][c] == '.': data[r][c] = 0
        if data[r][c] == '^': data[r][c] = -1

for r in range(1, len(data)):
    for c in range(len(data[0])):
        if data[r-1][c] > 0:
            if data[r][c] == -1:
                data[r][c-1] = data[r-1][c] + data[r][c-1]
                data[r][c+1] = data[r-1][c]
            else:
                data[r][c] = data[r-1][c] + data[r][c]

tot = 0
for c in range(len(data[0])):
    tot += data[-1][c]

print(tot)
