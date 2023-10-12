import turtle
import random as rnd

turtle.setup(width=1000,height=1000,startx=0,starty=0)

t=turtle.Turtle()
t.shape("square")
turtle.bgcolor("black")


t.pensize(5)
t.pencolor("white")
for i in range(4):
    t.fd(200)
    t.left(90)

turtle.exitonclick()
