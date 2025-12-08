from collections import deque

day, test = 8, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()
    data = [tuple(int(n) for n in line.split(',')) for line in data]

def dist(t1, t2):
    return ((t1[0]-t2[0])**2 + (t1[1]-t2[1])**2 + (t1[2]-t2[2])**2)**(1/2)

dist_dict = {}

for i in range(len(data)):
    for j in range(i+1, len(data)):
        dist_dict.update({(i,j): dist(data[i], data[j])})

a = (sorted(dist_dict.items(), key=lambda item: item[1]))
all_clusters = [set([*e[0]]) for e in a]
clusters = deque()

while True:
    new_cluster = all_clusters.popleft()
    clusters.append(new_cluster)

    cluster_list = list(new_cluster)
    append_counter = 0
    old_len = len(clusters)
    while append_counter < len(clusters): 
        curr = clusters.popleft()
        for j in range(len(clusters)):
            for e in curr:
                if e in clusters[j]:
                    clusters[j] |= curr
                    break 
            else:
                continue
            break
        else:
            clusters.append(curr)
            append_counter += 1

    if len(clusters[0]) == len(data):
        print(data[cluster_list[0]][0] * data[cluster_list[1]][0]) 
        break
