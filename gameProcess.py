from turtle import shape
import matrixOperation as mO

# iteration by regular life game rule
def regularUpdate(matrix):
    if_rec, len, wid = mO.checkRec(matrix)
    if if_rec == True:
        matrix_it = []
        for i in matrix:
            matrix_it.append(i.copy())
        for n in range(1, wid - 1):
            for m in range(1, len - 1):
                matrix_it[m][n] = iteration(matrix, m, n)
    else:
        return 0
    #matrixShow(matrix)
    return matrix_it


# check status of a cell for next iteration
def iteration(matrix, m, n):
    count = 0
    self = matrix[m][n]
    for i in -1, 0, 1:
        for j in -1, 0, 1:
            if matrix[m + i][n + j] == 1:
                count = count + 1
            else:
                pass
    count = count - self
    if self == 0 and count == 3:
        return 1
    elif self == 1 and count < 2:
        return 0
    elif self == 1 and count > 3:
        return 0
    elif self == 1 and count == 2:
        return 1
    elif self == 1 and count == 3:
        return 1
    else:
        return 0

def readShape(txt):
    shape_mat = []
    new_txt = txt[1: -1] + txt[-1]
    row_txt_list = new_txt.split('#')
    for i in row_txt_list:
        row_shape = []
        while len(i) > 1:
            id_num = int(i[0])
            id = i[1]
            if id == 'x':
                for j in range(id_num):
                    row_shape.append(1)
            else:
                for j in range(id_num):
                    row_shape.append(0)
            i = i[2: -1] + i[-1]
        shape_mat.append(row_shape)
    return shape_mat

#    "#2o1x#1x1o1x#1o2x"
