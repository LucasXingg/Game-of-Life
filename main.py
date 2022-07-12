#from operator import truediv
import pyglet
from pyglet import shapes
from pyglet.window import key
import time
import GUIsetting as gS
import matrixOperation as mO
import cmdOperation as cO
import config
import gameProcess as gP
from config import command_list as cL

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++(class)++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class myVariables(object):

    def __init__(self):
        self.input = ''
        self.err = ''
        self.rand_run = False
        self.iter_run = False
        self.row_list, self.col_list, self.m, self.n = gS.colSize(window.get_size()[0], window.get_size()[1], config.default_n)
        mymat = mO.matrixCreate(self.m, self.n)
        self.mat = mO.combinMat(mymat, gP.readShape(config.shape_list['logo']), 11, 19)
        self.shape_list = {}
        self.shape = ''
        self.bound = False

        self.cmd_line = shapes.Line(0, 30, window.get_size()[0], 30)
        self.label = pyglet.text.Label(text = self.input, x = 10, y = 10)
        self.errlabel = pyglet.text.Label(text = self.err, x = window.get_size()[0] - 10, y = 10, color = config.warning_color, anchor_x = 'right',)
        self.shapelabel = pyglet.text.Label(text = self.shape, x = 35, y = 50)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++(methods)++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def drawMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i] [j] == 1:
                square = shapes.Rectangle(my.col_list[j], my.row_list[i], my.col_list[1] - my.col_list[0], my.row_list[1] - my.row_list[0], color = (200, 200, 200))
                square.draw()

def drawDiag():
    for i in my.row_list:
        line = shapes.Line(my.col_list[0], i, my.col_list[-1], i)
        line.draw()
    for i in my.col_list:
        line = shapes.Line(i, my.row_list[0], i, my.row_list[-1])
        line.draw()

def rand(dt):
    window.clear()
    my.mat = mO.matrixCreate(my.m, my.n, rand = True)

def iterations(dt):
    my.mat = gP.regularUpdate(my.mat, my.bound)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++(operations)+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def processCommand(text):
    my.err = ''
    name, para = cO.processCmd(text)
    if name == cL[0]:
        upDate(para)
    elif name == cL[1]:
        run(para)
    elif name == cL[2]:
        randmat(para)
    elif name == cL[3]:
        stop(para)
    elif name == cL[4]:
        boat(para)
    elif name == cL[5]:
        exitWindow(para)
    elif name == cL[6]:
        resizeMat(para)
    elif name == cL[7]:
        matLoad(para)
    elif name == cL[8]:
        matInit(para)
    elif name == cL[9]:
        putShape(para)
    elif name == cL[10]:
        setWall(para)
    else:
        my.err = 'Command not found'
        

def upDate(para):
    my.rand_run = True
    if len(para) > 0:
        pyglet.clock.schedule_interval(rand, float(para[0]))
    else:
        pyglet.clock.schedule_interval(rand, 1)

def run(para):
    if len(para) > 0:
        my.iter_run = True
        pyglet.clock.schedule_interval(iterations, float(para[0]))
    else:
        iterations(1)

def randmat(para):
    rand(1)

def stop(para):
    if my.rand_run == True:
        pyglet.clock.unschedule(rand)
        my.rand_run = False
    elif my.iter_run == True:
        pyglet.clock.unschedule(iterations)
        my.iter_run = False
    else:
        my.err = 'Nothing running'

def boat(para):
    my.mat = mO.boat()

def exitWindow(para):
    window.close()

def resizeMat(para):
    if len(para) > 0:
        if int(para[0]) > 100:
            my.err = 'Size too BIG'
        elif int(para[0]) < 10:
            my.err = 'Size too SMALL'
        else:
            my.row_list, my.col_list, my.m, my.n = gS.colSize(window.get_size()[0], window.get_size()[1], int(para[0]))
            my.mat = mO.matrixCreate(my.m, my.n)
    else:
        my.row_list, my.col_list, my.m, my.n = gS.colSize(window.get_size()[0], window.get_size()[1], my.n)
        my.mat = mO.matrixCreate(my.m, my.n)

def matLoad(para):
    try:
        my.shape_list[para[0]] = config.shape_list[para[0]]
    except:
        if len(para) > 0 and para[0] == 'clear':
            my.shape_list.clear()
        else:
            my.err = 'shape not found'

def matInit(para):
    para.append('0')
    if para[0] == '1':
        my.mat = mO.matrixCreate(my.m, my.n, int(1))
    else:
        my.mat = mO.matrixCreate(my.m, my.n)

def putShape(para):
    try:
        my_shape = gP.readShape(my.shape_list[para[0]])
    except:
        my.err = 'shape not found in memory'
        return 0
    try:
        my_m = int(para[1])
        my_n = int(para[2])
    except:
        my_m = 1
        my_n = 1
    try:
        my.mat = mO.combinMat(my.mat, my_shape, my_m, my_n)
    except:
        my.err = 'Can\'t draw'

def setWall(para):
    para.append("1")
    if para[0] == "1":
        one_vector = []
        for i in range(my.n):
            one_vector.append(1)
        for i in my.mat:
            i[0] = 1
            i[-1] = 1
        my.mat[0] = one_vector
        my.mat[-1] = one_vector
        my.bound = True
    elif para[0] == "0":
        zero_vector = []
        for i in range(my.n):
            zero_vector.append(0)
        for i in my.mat:
            i[0] = 0
            i[-1] = 0
        my.mat[0] = zero_vector
        my.mat[-1] = zero_vector
        my.bound = True
    elif para[0] == 'set':
        my.bound = True
        my.err = "wall set"
    elif para[0] == 'clear':
        my.bound = False
        my.err = "wall clear"


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++(init values)++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

window = pyglet.window.Window(resizable = True, caption = 'Lucas\'s Gmae of Life   -V_1.0.1-')
my = myVariables()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++(main)+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ENTER:
        processCommand(my.input[0:len(my.input) - 1])
        my.input = ''
    elif symbol == key.BACKSPACE:
        my.input = my.input[0:-1]
    else:
        pass

@window.event
def on_text(text):
    my.input = my.input + str(text)


@window.event
def on_draw():
    window.clear()
    drawMatrix(my.mat)
    drawDiag()
    my.cmd_line = shapes.Line(0, 30, window.get_size()[0], 30)
    my.cmd_line.draw()
    my.label = pyglet.text.Label(text = my.input, x = 10, y = 10)
    my.label.draw()
    my.errlabel = pyglet.text.Label(text = my.err, x = window.get_size()[0] - 10, y = 10, color = config.warning_color, anchor_x = 'right',)
    my.errlabel.draw()
    my.shape = ''
    for i in my.shape_list:
            my.shape = my.shape + i + '   '
    my.shapelabel = pyglet.text.Label(text = my.shape, x = 35, y = 50)
    my.shapelabel.draw()

pyglet.app.run()