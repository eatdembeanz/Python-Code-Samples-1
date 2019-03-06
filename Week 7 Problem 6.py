#Benjamin Page
#2/28/2019
#Problem 6: Use the polygon program from last week and convert it to a function. Call the  function in a way to create a pattern similar to below
import turtle
drawboy = turtle.Turtle()
drawboy.shape("turtle")
drawboy.color("pink")
drawboy.pensize(3)
def drawshape(sides,size):
    angle = 360/sides
    for i in range(sides):
        drawboy.left(angle)
        drawboy.forward(size)

wn = turtle.Screen()
for i in range(10):
    drawshape(6,60)
    drawboy.left(36)
wn.exitonclick()
