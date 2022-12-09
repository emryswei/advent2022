
scores = []
table = {
    'AX':4, 'AY':8, 'AZ':3,
    'BX':1, 'BY':5, 'BZ':9,
    'CX':7, 'CY':2, 'CZ':6
}

with open('./data.in') as f:
    results = f.read().strip().split('\n')
    for res in results:
        res = res.replace(' ', '')
        scores.append(table[res])


print(sum(scores))
