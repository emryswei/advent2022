

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
    d, f = int(d) - 1, int(f) - 1
    for _ in range(int(b)):
        q[f] += q[d][-1]
        q[d] = q[d][:-1]

ans = ''
ll = len(q)
for i in range(ll):
    ans += q[i][-1]
print(ans)