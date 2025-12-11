from collections import defaultdict

day, test = 11, 0

with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

g = {}

for line in data:
    g[line.split(': ')[0]] = line.split(': ')[1].split()

g['out'] = []

def paths(start, end):
    tot = 0
    d_step_last = defaultdict(int)
    d_step_last[start] = 1
    for i in range(0, len(g)):
        d_step_new = defaultdict(int)

        for vortex in d_step_last:   
                for target in g[vortex]:
                    d_step_new[target] += d_step_last[vortex]
                    if target == end:
                        tot += d_step_last[vortex]
        d_step_last = d_step_new
    return tot

print(paths('svr', 'fft') * paths('fft', 'dac') * paths('dac', 'out'))
