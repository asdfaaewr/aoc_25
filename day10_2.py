import numpy as np
from scipy.optimize import minimize, LinearConstraint

day, test = 10, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

tot = 0
tot_arr = []

for line in data:
    joltage , buttons = line.split()[-1], line.split()[1:-1]

    joltage = list(map(int,joltage[1:-1].split(',')))
    joltage = tuple(joltage)
    buttons = [list(map(int, b[1:-1].split(','))) for b in buttons]

    matrix = np.zeros((len(joltage), len(buttons)), dtype=int)

    for col_idx, sublist in enumerate(buttons):
        for row_idx in sublist:
            matrix[row_idx, col_idx] = 1

    b = np.array(joltage)

    cons2 = LinearConstraint(np.eye(len(buttons)), 0, 10000)
    res_array = []

    for i in range(-10, 20):
        for j in range(-10, 20):

            def objq(x):
                return sum(abs(x))+ sum(abs(x - np.rint(x)))*17*j + sum(abs((matrix@x-b)))*(i*67)
            
            resq = minimize(objq, np.zeros(len(buttons)), constraints = cons2)
            resq_x = np.rint(resq.x)

            if max((matrix@resq_x - b)**2) < 0.0000001:
                res_array.append(sum(resq_x))

    for i in range(-10, 20):
        for j in range(-10, 20):

            def objq(x):
                return sum(abs(x))+ sum((x - np.rint(x))**2)*2*j + sum(abs((matrix@x-b)))*(i*51)
            
            resq = minimize(objq, np.zeros(len(buttons)), constraints = cons2)
            resq_x = np.rint(resq.x)

            if max((matrix@resq_x - b)**2) < 0.0000001:
                res_array.append(sum(resq_x))

    for i in range(-10, 20):
        for j in range(-10, 20):

            def objq(x):
                return sum(abs(x))+ sum(abs(x - np.rint(x)))*28*j + sum(((matrix@x-b))**2)*(i*14)
            
            resq = minimize(objq, np.zeros(len(buttons)), constraints = cons2)
            resq_x = np.rint(resq.x)

            if max((matrix@resq_x - b)**2) < 0.0000001:
                res_array.append(sum(resq_x))
   
    if len(res_array) > 0:
        tot += min(res_array)
        tot_arr.append(min(res_array))
    else:
        print(line)

print(tot)
print(tot_arr)
