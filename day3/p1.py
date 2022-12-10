letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ltos = {k:v for v, k in enumerate(letters, 1)}

ans = 0
res = []
with open('./data.in') as f:
    letters = f.read().strip().split('\n')
    for letter in letters:
        length = len(letter)
        fh, sh = letter[:length//2], letter[length//2:]
        x =[ x for x in fh if x in sh][0]
        # res.append(x)
        ans += ltos[x]
print(ans)