from turtle import *


window = Screen()
window.setup(width=680, height=680)
window.bgcolor("white")

c1 = Turtle()
c1.color("#2C5D54")
c1.pensize(680)
c1.forward(0)

b1 = Turtle()
b1.penup()
b1.goto(-180,-220)
b1.pendown()
b1.fillcolor("purple4")
b1.begin_fill()
 
for i in range(2):
    b1.forward(70)
    b1.left(90)
    b1.forward(180)
    b1.left(90)
 
b1.end_fill()

b2 = Turtle()
b2.penup()
b2.goto(-220,-220)
b2.pendown()
b2.fillcolor("#6C2624")
b2.begin_fill()
b2.left(90)
b2.forward(180)
b2.right(150)
b2.forward(210)
b2.right(120)
b2.forward(105)
b2.end_fill()
