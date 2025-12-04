day, test = 4, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

tot = 0
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
papers = set()

for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] =='@':
            papers.add((r,c))

temp = len(papers)
while True:
    remove = set()
    for r in range(len(data)):
        for c in range(len(data[0])):
            p = 0

            if (r,c) in papers:
                for dr, dc in dirs:
                    if r+dr >= len(data) or r+dr < 0 or c+dc >= len(data[0]) or c+dc < 0: continue
                    if (r+dr, c+dc) in papers:
                        p +=1

                if p <4:
                    remove.add((r,c))
                    tot += 1
    
    if len(remove) == 0:
        print(temp-len(papers))
        break

    papers = papers - remove