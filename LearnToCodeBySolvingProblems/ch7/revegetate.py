with open('revegetate.in', 'r') as fin:
    buckets = tuple(map(int, fin.readline().strip().split()))
    N = buckets[0]
    M = buckets[1]
    rows = [list(map(int, x.strip().split())) for x in fin.readlines()]
    for i in range(len(rows)):
        if (rows[i][0] > rows[i][1]):
            temp = rows[i][0]
            rows[i][0] = rows[i][1]
            rows[i][1] = temp
    A = [row[0] for row in rows]
    B = [row[1] for row in rows]
    G = [0] * 200
    with open('revegetate.out', 'w') as fout:
        for pasture in range(1, N+1):
            for seed in range(1, 5):
                ok = True
                for cow in range(M):
                    if (B[cow] == pasture and G[A[cow]] == seed):
                        ok = False
                if ok:
                    break
            G.insert(pasture, seed)
            fout.write(str(seed))
        fout.write('\n')        