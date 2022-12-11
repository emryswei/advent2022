

count = 1000
ans = 0 

with open('./data.in') as f:
    data = f.read().strip().split('\n')
    for d in data:
        fh, sh = d.split(',')
        fh1, fh2 = [int(n) for n in fh.split('-')]
        sh1, sh2 = [int(n) for n in sh.split('-')]

        if (fh2 < sh1) or (fh1 > sh2):
            ans += 1
print(count - ans)