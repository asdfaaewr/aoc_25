day, test = 1, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

pos, count = 50, 0

for line in data:
    old_pos =  pos

    if line[0] == "R":
        n, pos = divmod(pos + int(line[1:]), 100)
        count += n
    else:
        n, pos = divmod(pos - int(line[1:]), 100)
        count -= n

        if pos == 0:
            count += 1

        if old_pos == 0:
            count -= 1

print(count)
