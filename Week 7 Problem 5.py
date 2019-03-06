#Benjamin Page
#2/28/2019
#Problem 5: Use the following chunk of code as a base to produce the image shown bel

import turtle
def drawsquare(t,sz):
     for i in range(4):
         t.forward(sz)
         t.left(90)

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")

def concentricsquares(x,size):
    alex = turtle.Turtle()
    alex.color("blue")
    sizelist = [20,40,60,80,100]
    #sizelist = []
   # sizelist.append(size)
    #movesize = size
    #for i in range(x-1):
        #size = size*1.5
       # sizelist.append(size)
    for y in sizelist:
        drawsquare(alex,y)
        alex.penup()
        #alex.backward(movesize/2)
        alex.backward(10)
        alex.right(90)
        #alex.forward(movesize/2)
        alex.forward(10)
        alex.left(90)
        alex.pendown()
#Try increasing each step in increments of the original size?
concentricsquares(5,25)
wn.exitonclick()
