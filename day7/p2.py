
from collections import defaultdict


path = []
size = defaultdict(int)

with open('./data.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    for line in lines:
        words = line.strip().split()
        if words[1] == 'cd':
            if words[2] == '..':
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == 'ls':
            continue
        elif words[0] == 'dir':
            continue
        else:
            sz = int(words[0])
            for i in range(1, len(path)+1):
                size['/'.join(path[:i])] += sz


total = 70000000
unused = 30000000
used = size['/']
needed = used - (total - unused)
ans = 99999999

for k, v in size.items():
    if v >= needed:
        ans = min(v, ans)
print(ans)