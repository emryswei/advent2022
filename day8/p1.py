
edge = 0
moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
ans = 0
with open('./data.txt') as f:
    trees = f.read().strip().split('\n')
    R, C = len(trees[0]), len(trees)
    edge = (R + C) * 2 - 4
    for r in range(1, R-1):
        for c in range(1, C-1):
            can_add = False

            for (move_r, move_c) in moves:
                curr_r = r 
                curr_c = c
                need_add = True
                while True:
                    curr_r += move_r
                    curr_c += move_c
                    if not (0 <= curr_r < R and 0 <= curr_c < C):
                        break
                    if trees[r][c] <= trees[curr_r][curr_c]:
                        need_add = False
                if need_add:
                    can_add = True

            if can_add:
                ans += 1
print(ans+edge)
