import turtle


t=turtle.Turtle()

t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)


input()


import turtle 


t=turtle.Turtle()

turtle.setup(width=1200, height=1200, startx=-0, starty=0)

t.pensize(3)

x=30+1

for i in range(200):
    t.left(45)
    t.fd(30)
    t.left(45)
    t.fd(45)
    t.left(45)