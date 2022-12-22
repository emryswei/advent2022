with open('data.txt') as f:
    lines = f.read().split('\n')
    for line in lines:
        line = line.split(' ')
        

def update_tail(H, T):
    d_row = H[0] - T[0]
    d_col = H[1] - T[1]

    if abs(d_row) <= 1 and abs(d_col) <= 1:
        pass

    elif (abs(d_row) == 2 and abs(d_col) == 1) or (abs(d_row) == 1 and abs(d_col) == 2):
        if H[0] > T[0] and H[1] < T[1]:
            T = (T[0] + 1, T[1] - 1)
        elif H[0] > T[0] and H[1] > T[1]:
            T = (T[0] + 1, T[1] + 1)
        elif H[0] < T[0] and H[1] < T[1]:
            T = (T[0] - 1, T[1] - 1)
        elif H[0] < T[0] and H[1] > T[1]:
            T = (T[0] - 1, T[1] + 1)

    elif abs(d_row) == 2:
        if H[0] > T[0]:
            T = (H[0] - 1, T[1])
        else:
            T = (H[0] + 1, T[1])

    elif abs(d_col) == 2:
        if H[1] > T[1]:
            T = (T[0], H[1] - 1)
        else:
            T = (T[0], H[1] + 1)

    return T
    # elif abs(d_row) == 1 and abs(d_col) == 2:
    #     if H[0] > T[0] and H[1] < T[1]:
    #         T = (T[0] + 1, T[1] - 1)
    #     elif H[0] > T[0] and H[1] > T[1]:
    #         T = (T[0] + 1, T[1] + 1)
    #     elif H[0] < T[0] and H[1] < T[1]:
    #         T = (T[0] - 1, T[1] - 1)
    #     elif H[0] < T[0] and H[1] > T[1]:
    #         T = (T[0] - 1, T[1] + 1)
