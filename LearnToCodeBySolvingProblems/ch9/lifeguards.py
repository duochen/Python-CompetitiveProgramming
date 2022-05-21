"""
ID: duochen2
LANG: PYTHON3
TASK: lifeguards
"""

with open('lifeguards.in', 'r') as fin:
    N = int(fin.readline())
    start = []
    end = []
    for i in range(N):
        line = fin.readline().strip().split(' ')
        start.append(int(line[0]))
        end.append(int(line[1]))
    numCover = [0] * 1000
    for i in range(N):
        for t in range(start[i], end[i]):
            numCover[t] += 1

    maxCover = 0
    for i in range(N):
        # We fire lifeguard i temporarily
        for t in range(start[i], end[i]):
            numCover[t] -= 1

        covered = 0
        for t in range(1000):
            if numCover[t] > 0:
                covered += 1
        maxCover = max(maxCover, covered)
        # Revert the firing
        for t in range(start[i], end[i]):
            numCover[t] += 1

    with open('lifeguards.out', 'w') as fout:
        fout.write(f"{maxCover}")    
