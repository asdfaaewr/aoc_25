day, test = 12, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().split("\n\n")

trees = data[-1]
used = []
for pres in data[:-1]:
    used.append(pres.count('#'))

wrong, right = 0, 0

for tree in trees.splitlines():
    grid, numbers = tree.split(": ")
    rows, cols = [int(x) for x in grid.split('x')]
    total_size = rows * cols
    total_used = sum(int(numbers.split()[i]) * used[i] for i in range(6))
    if total_used/total_size > 1:
        wrong += 1
    
    if total_used/total_size < 0.8:
        right += 1
    
print(wrong, right)



