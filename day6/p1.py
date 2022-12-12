


with open('./data.txt', 'r') as f:
    data = f.read()
    curr = 0
    end = len(data) - 4
    ans = 0
    while curr <= end:
        if len(set(data[curr:curr+4])) == 4:
            ans = (curr+4)
            break
        else:
            curr += 1
print(ans)