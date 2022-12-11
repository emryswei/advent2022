
ans = 0

with open('./data.in') as f:
    data = f.read().strip().split('\n')
    for d in data:
        fh, sh = d.split(',')
        fh1, fh2 = [int(n) for n in fh.split('-')]
        sh1, sh2 = [int(n) for n in sh.split('-')]

        if (fh1 >= sh1 and fh2 <= sh2) or (sh1 >= fh1 and sh2 <= fh2):
            ans += 1
            
print(ans)