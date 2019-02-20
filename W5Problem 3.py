#Ben Page
#2/20/2019
#Creates a regular polygon based on parameters the user inputs: number of sides, length, and colors.
import turtle
wn = turtle.Screen()
drawboy = turtle.Turtle()
drawboy.shape("turtle")
sides = int(input("How many sides do you want to draw?"))
length = int(input("How long should each side be?"))
color = str(input("What color should the shape's borders be?"))
fill = str(input("What color should the shape's inside be?"))
angle = (360/sides)
drawboy.pensize(10)
drawboy.begin_fill()
drawboy.color(color)
drawboy.fillcolor(fill)
for i in range(sides):
    drawboy.forward(length)
    drawboy.left(angle)
drawboy.end_fill()

wn.exitonclick()
