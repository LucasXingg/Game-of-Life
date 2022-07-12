# command list
- run
- randmat
- random
- stop
- clear
- resize
- load
- draw
- wall
- exit

## run
*run*
- simply start iteration

## randmat
*randmat*
- randomily init the workspace

## random
*random /dt*
- keep randomily init the workspace
- dt: time interval, 1/s if no input parameter

## stop
*run*
- stop run/random

## clear
*clear /i*
- clear workspace/ make workspace full of cells if *i* == 1
![clear](im/截屏2022-07-10%2018.01.23.png)

## resize
*resize /int*
- set the size of workspace
- int: width of workspace
- default size can be change in config.py
- if you has change the size of game window, you can use *resize* to fit the workspace

## load
*load /shapename*
- load shapes to memory from config.py
- shapes can be found in config.py
![load](im/截屏2022-07-10%2018.30.39.png)

## draw
*draw /shapename /m /n*
- put shapes to workspace
- m n: coordinates same as matrix
- m = 1, n = 1 if no parameter input
![draw](im/截屏2022-07-10%2017.56.13.png)

## wall
*wall /para*
- para: /0 /1 /set /clear
- for 0 and 1, you can set the edge of workspace as cell or dead cell
- wall /set: set a "wall" in your workspace, so edge of workspace will not participate in iteration
- wall /clear: clear the wall

## exit
*exit*
- quit the program

