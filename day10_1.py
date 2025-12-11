
from collections import deque

day, test = 10, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

tot = 0

for line in data:
    lights, buttons = line.split()[0], line.split()[1:-1]
    lights = [0 if l == '.' else 1 for l in lights[1:-1]]
    buttons = [list(map(int, b[1:-1].split(','))) for b in buttons]

    curr = [0] * len(lights)
    d = deque([(curr, 0)])
    while d:
        curr, n = d.popleft()

        if curr == lights:
            tot += n
            break

        for button in buttons:
            if len(button) == 1:
                button = (button)
            d.append(([(curr[i]+1)%2 if i in button else curr[i] for i in range(len(curr))], n+1))

    print(tot)    
