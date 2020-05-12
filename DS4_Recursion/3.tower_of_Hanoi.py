'''
    LeetCode   面试题08.06  汉诺塔问题


    递归：
    1.找出最基础部分
    2.无限向着最基础的部分靠近
    3.递归函数


    第一步：找出最基础的部分：假设说，N=5，（1,2,3,号杆），最初在1号杆上。

    1号5   借助3号杆移动4个到2号               剩1个移动到3号杆（1:0  2:4  3:1）
    2号4   借助1号杆移动3个到3号杆         剩1到1号        （1:1  2:0  3:4）
           借助2号杆移动2个到xx号
           借助x好杆移动1个到xx号
    fromPole  从哪个杆
    withPole  借助哪个杆
    num       移动多少个
    toPole    到哪个杆
    move(num,fromPole,withPole,toPole)

'''

def move(num,fromPole,withPole,toPole):



'''
    迷宫：参考LeetCode1210题：穿过迷宫的最少移动次数

    1.从初始位置尝试向上走一步，以此来开始递归
    2.如果上面走不通则尝试走下面，再开始递归
    3.上下都不通，走左边，再开始递归
    4.上下左都不通，走右边，再开始递归

    四种基本情况：
    1.碰到“墙壁”，方格被占用无法通行
    2.方格被访问过，为避免陷入循环不再此位置继续寻找
    3.碰到边缘，表示成功
    4.四个方向，探索失败，游戏失败。

    turtle
    __init__        用来读取迷宫的数据，初始化迷宫内部，并找到精灵的初始位置
    draw_maze       用来在屏幕上绘制迷宫
    update_position 用来更新迷宫内的状态和游戏精灵的位置
    is_exit         用来判断当前位置是否是出口

 
'''
# 迷宫的地图：从txt文件中获取,地图是一个只包含：+ 空格 的文件
# turtle  GUI库绘制迷宫地图
# 用到的绘制迷宫符号：+  空格

import turtle
self.wn = turtle.Screen()
class Maze:
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []

        mazeFile = open(mazeFileName,'r')
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'Q':
                    self.startRow = rowsInMaze
                    self.starCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        print(self.xTranslate)
        print(self.yTranslate)
        self.t = turtle.Turtle(shape='turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5,-(rowsInMaze-1)/2-.5,(columnsInMaze-1)/2+.5,(rowsInMaze-1)/2+.5)
        # self.wn.exitonclick()   
    # 绘制屏幕
    def draw_maze(self,x,y,color):
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color('black',color)
        self.t.setheading(90)
        self.t.down
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        update()



mazeFileName = 'DS4_Recursion/maze.txt'
maze = Maze(mazeFileName)
maze.draw_maze(0,0,"red")
                    


