day, test = 3, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

tot = 0

for line in data:
    line = [int(x) for x in line]
    m = max(line[:-1])

    flag, running_m = 0, 0
    for e in line:

        if flag:
            running_m = max(running_m, e)
        if e == m:
            flag = 1
        
    tot = tot + 10*m + running_m

print(tot) 


