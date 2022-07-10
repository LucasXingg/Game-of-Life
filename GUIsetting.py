from socket import NI_NAMEREQD
import config as cf

def colSize(width, height, val, axis = 'n'):
    space = cf.empty_space
    row_list = [height - space / 2]
    col_list = [space / 2]
    height_space = (height - 30 - space)
    width_space = (width - space)
    n_m, n_n = colRatio(width_space, height_space, val, axis)
    row_space = (height - 30 - space) / n_m
    col_space = (width - space) / n_n
    for i in range(n_n):
        col_list.append(space / 2 + (i + 1) * col_space) 
    for i in range(n_m):
        row_list.append(height - space / 2 - (i + 1) * row_space)

    return row_list, col_list, n_m, n_n

def colRatio(width, height, val, axis = "n"):
    space = cf.empty_space
    if axis == 'n':
        n_m = height * val / width
        n_n = val
    else:
        n_n = width * val / height
        n_m = val
    return round(n_m), round(n_n)