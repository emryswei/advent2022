


with open('./data.txt', 'r') as f:
    data = f.read()
    curr = 0
    end = len(data) - 14
    ans = 0
    while curr <= end:
        if len(set(data[curr:curr+14])) == 14:
            ans = (curr+14)
            break
        else:
            curr += 1
print(ans)