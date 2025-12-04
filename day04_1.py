day, test = 4, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

tot = 0
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


for r in range(len(data)):
    for c in range(len(data[0])):
        p = 0

        if data[r][c] =='@':
            for dr, dc in dirs:
                if r+dr >= len(data) or r+dr < 0 or c+dc >= len(data[0]) or c+dc < 0: continue
                if data[r+dr][c+dc] =='@':
                    p +=1

            if p < 4:
                tot += 1

print(tot)