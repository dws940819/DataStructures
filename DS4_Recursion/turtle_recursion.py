'''
import turtle
import time
myTurtle = turtle.Turtle()

# 递归三大条件
1.最小条件 
2.无限靠近这个条件
3.拥有一个函数函数

def drawSpiral(myTrurtle,lineLen)
    if lineLen > 0:
        myTurtle.forward(lineLen)

    myTurtle.right(90)
    drawSpiral(myTurtle,lineLen - 5)

drawSpiral(myTurtle,100)

myWin.exitonclick()

'''

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def tree(distance,myTurtle):
    if distance > 5 :
        myTurtle.forward(distance)
        myTurtle.right(20)
        tree(distance-15, myTurtle)
        myTurtle.left(40)
        tree(distance-10, myTurtle)
        myTurtle.right(20)
        myTurtle.backward(distance)

tree(100,myTurtle)
myWin.exitonclick()


