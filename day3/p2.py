letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ltos = {k:v for v, k in enumerate(letters, 1)}

res = 0
with open('./data.in') as f:
    ls = f.read().strip().split('\n')
    counts = len(ls)
    for i in range(0, counts, 3):
        one, two, three = ls[i], ls[i+1], ls[i+2]
        x = [x for x in one if x in two and x in three][0]
        res += ltos[x]

print(res)
    