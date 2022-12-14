
from collections import defaultdict

SIZE_MAX = 100000
path = []
size = defaultdict(int)
ans = 0

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

for k, v in size.items():
    if v <= SIZE_MAX:
        ans += v

print(ans)