from collections import Counter, defaultdict
from functools import cache
import time

day, test = 9, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()
    data = [[int(e) for e in line.split(',')] for line in data]

red_up, red_up_ver, red_down, red_down_ver, boarder = set(), set(), set(), set(), set()

for i in range(len(data)):
    if data[(i+1)%len(data)][0] > data[i][0] or data[(i-1)%len(data)][0] > data[i][0]:
        red_down.add((data[i][0], data[i][1]))
    else:
        red_up.add((data[i][0], data[i][1]))

    if data[(i+1)%len(data)][1] > data[i][1] or data[(i-1)%len(data)][1] > data[i][1]:
        red_down_ver.add((data[i][0], data[i][1]))
    else:
        red_up_ver.add((data[i][0], data[i][1]))

    for r in range(min(data[i][0], data[(i+1)%len(data)][0]), max(data[i][0], data[(i+1)%len(data)][0])+1):
        for c in range(min(data[i][1], data[(i+1)%len(data)][1]), max(data[i][1], data[(i+1)%len(data)][1])+1):
            boarder.add((r, c))

def line_inside_hor(point1, point2):
    r, c1, c2 = point1[0], point1[1], point2[1]

    if c1 > c2:
        c1, c2 = c2, c1

    relevant_boarder = sorted([p for p in boarder if p[0]==r])  
    touch_counter = 0
    if relevant_boarder[0][1] > c1: return False
    if relevant_boarder[-1][1] < c2: return False

    for p in relevant_boarder:
        if p[1] >= c2: return True

        if (r, p[1]-1) not in relevant_boarder:

            if p in red_down: last = ('down', touch_counter)
            if p in red_up: last = ('up', touch_counter)

            if touch_counter == 0:
                touch_counter = 1
            elif touch_counter == 1 and (r, p[1]+1) not in relevant_boarder:
               touch_counter = 0
        else:
            if p in red_down and last[0] =='down': touch_counter = last[1]
            if p in red_up and last[0] =='up': touch_counter = last[1]

            if p in red_down and last[0] =='up': touch_counter = (last[1] + 1) % 2
            if p in red_up and last[0] =='down': touch_counter = (last[1] + 1) % 2
        
        if touch_counter == 0 and c1 <= p[1] < c2:
            return False
    
    return True   

def line_inside_ver(point1, point2):
    c, r1, r2 = point1[1], point1[0], point2[0]

    if r1 > r2:
        r1, r2 = r2, r1

    relevant_boarder = sorted([p for p in boarder if p[1]==c])  
    touch_counter = 0

    if relevant_boarder[0][0] > r1: return False
    if relevant_boarder[-1][0] < r2: return False

    for p in relevant_boarder:
        if p[0] >= r2: return True

        if (p[0]-1, c) not in relevant_boarder:
            if p in red_down_ver: last = ('down', touch_counter)
            if p in red_up_ver: last = ('up', touch_counter)
            
            if touch_counter == 0:
                touch_counter = 1
            elif touch_counter == 1 and (p[0]+1, c) not in relevant_boarder:
               touch_counter = 0 
        else:
            if p in red_down_ver and last[0] =='down': touch_counter = last[1]
            if p in red_up_ver and last[0] =='up': touch_counter = last[1]
        
            if p in red_down_ver and last[0] =='up': touch_counter = (last[1] + 1) % 2
            if p in red_up_ver and last[0] =='down': touch_counter = (last[1] + 1) % 2

        if touch_counter == 0 and r1 <= p[0] < r2:
            return False
    
    return True   

tot = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        r1, c1 = data[i]
        r2, c2 = data[j]
        if r1 == r2 or c1 == c2: continue
        area = (1+abs(r1-r2)) * (1+abs(c1-c2))
        if area > tot:

            if not line_inside_hor((r1, c1), (r1, c2)):
                continue

            if not line_inside_hor((r2, c1), (r2, c2)):
                continue

            if not line_inside_ver((r1, c1), (r2, c1)):
                continue

            if not line_inside_ver((r1, c2), (r2, c2)):
                continue           

            tot = area
      
print(tot)
