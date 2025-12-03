day, test = 3, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

tot = 0

def find_highest(line, lengths):
    if lengths==0: return ''
    s = str(max([int(x) for x in line][:len(line)-(lengths-1)]))
    return s + find_highest(line[line.find(s)+1:], lengths-1)

for line in data:
    tot += int(find_highest(line, 12))

print(tot) 


