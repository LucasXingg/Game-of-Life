# default graphs
empty_space = 100   # empty space from window edge
warning_color = (200, 0, 0, 255) # R, G, B, A
default_n = 50    # default workspace width

#============================
# command list

command_list = [
    "random",
    "run",
    "randmat",
    "stop",
    "boat",
    "exit",
    "resize",
    "load",
    "clear",
    "draw",
    "wall"
]
#============================
# dictionary to store shapes
# #:begining of a row
# o:dead cell
# x:alive cell
# e.g:
# "#2o1x#1x1o1x#1o2x":
#   [ ][ ][x]
#   [x][ ][x]
#   [ ][x][x]

shape_list = {
    'glider': "#2o1x#1x1o1x#1o2x",
    'blinker': "#3x",
    'dot': "#1x",
    'empty': "#1o",
    'logo': "#2o3x1o3x2o#1o1x7o1x1o#1x1o1x5o1x1o1x#3o1x3o1x2o1x#1x3o1x1o1x4o#1x4o1x4o1x#1x3o1x1o1x3o1x#1x2o1x3o1x2o1x#1x1o1x5o1x1o1x#1o1x7o1x1o#2o1x1o4x3o",
    'beacon': "#2x2o#1x3o#3o1x#2o2x",
    'pentadecathlon': "#2o1x4o1x2o#2x1o4x1o2x#2o1x4o1x2o"
}