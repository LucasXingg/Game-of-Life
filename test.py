import matrixOperation as mO
import gameProcess as gP

a = "#2o1x#1x1o1x#1o2x"
print(a)
shape = gP.readShape(a)
board = mO.matrixCreate(100, 100, 3)
result = mO.combinMat(board, shape, 1, 1)

print('shape')
mO.matrixShow(shape)
print('board')
mO.matrixShow(board)
print('result')
mO.matrixShow(result)