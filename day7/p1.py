

SIZE_MAX = 100000
ans = 0

directory = []
with open('./data.txt', 'r') as f:
    data = f.read().split('\n')
    for d in data:
        if d[0:3] == 'dir':
            if d[4:] not in directory: 
                directory.append(d[4:]) 
