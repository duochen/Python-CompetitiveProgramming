fin = open('citystate.in', 'r')
fout = open('citystate.out', 'w')
n = int(fin.readline())
d = {}
for i in range(n):
    city, state = fin.readline().split(' ')
    if city[:2] == state.strip():
        continue
    # combine the two prefix
    key = city[:2] + state.strip()
    # insert into dict
    if key in d:
        d[key] = d[key] + 1
    else:
        d[key] = 1
ans = 0
# enumerate key and find pairs
for i in d.keys():
    pair = i[2:] + i[:2]
    if pair in d:
        ans = ans + d[pair] * d[i]

fout.write(str(ans // 2))
