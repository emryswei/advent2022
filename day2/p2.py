
scores = []
table = {
    'AX':3, 'BX':1, 'CX':2,
    'AY':4, 'BY':5, 'CY':6,
    'AZ':8, 'BZ':9, 'CZ':7
}
with open('./data.in') as f:
    data = f.read().strip().split('\n')
    for d in data:
        d = d.replace(' ', '')
        scores.append(table[d])

print(sum(scores))

