day, test = 1, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

pos, count = 50, 0

for line in data:
    if line[0] == "R":
        pos = (pos + int(line[1:])) % 100

    else:
        pos = (pos - int(line[1:])) % 100

    if pos == 0:
        count += 1

print(count)

