


outer = 0

with open('./data.txt') as f:
    lines = f.read().strip().split('\n')
    
    width, height = len(lines[0]), len(lines)
    outer = (width + height ) * 2 - 4
    for h in range(1, height-1):
        for w in range(1, width-1):
            if lines[w][h] > lines[w-1][h-1]


