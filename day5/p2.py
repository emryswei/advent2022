

with open('./data.in') as f:
    x, y = f.read().split('\n\n')
    x, y = x.splitlines(), y.splitlines()

q = [''] * 9

l = len(x)
chars = len(x[0])

for i in range(l-2, -1, -1):
    for j in range(1, chars, 4):
        if x[i][j].isupper():
            q[j // 4] += x[i][j]

for i in y:
    a, b, c, d, e, f = i.split()
    b, d, f = int(b), int(d) - 1, int(f) - 1
    q[f] += q[d][-b:]
    q[d] = q[d][:-b]

        

ans = ''
ll = len(q) 
for i in range(ll):
    ans += q[i][-1]
print(ans)

