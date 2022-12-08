with open('./data.in') as f:
    nums = f.read().strip().split('\n')

max = 0
current_max = 0

for num in nums:
    if num != '':
        current_max += int(num)
    else:
        if current_max >= max:
            max = current_max
            current_max = 0
        current_max = 0

print(max)