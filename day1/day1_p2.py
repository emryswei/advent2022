with open('./data.in') as f:
    nums = f.read().strip().split('\n')

L = []
current_max = 0

for num in nums:
    if num != '':
        current_max += int(num)
    else:
        L.append(current_max)
        current_max = 0

print(sum(sorted(L)[-3:]))