# command list
- run
- randmat
- random
- stop
- clear
- resize
- load
- draw
- exit

## run
*run*
simply start iteration

## randmat
*randmat*
randomily init the workspace

## random
*random /dt*
keep randomily init the workspace
dt: time interval, 1/s if no input parameter

## stop
*run*
stop run/random

## clear
*clear /i*
clear workspace/ make workspace full of cells if *i* == 1
![clear](im/截屏2022-07-10%2018.01.23.png)

## resize
*resize /int*
set the size of workspace
int: width of workspace
default size can be change in config.py

if you has change the size of game window, you can use *resize* to fit the workspace

## load
*load /shapename*
load shapes to memory from config.py
shapes can be found in config.py
![load](im/截屏2022-07-10%2017.54.01.png)

## draw
*draw /shapename /m /n*
put shapes to workspace
m n: coordinates same as matrix
m = 1, n = 1 if no parameter input
![draw](im/截屏2022-07-10%2017.56.13.png)

## exit
*exit*
quit the program

