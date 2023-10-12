import turtle 

turtle.setup(width=1000,height=1000,startx=0,starty=0)
t=turtle.Turtle()
#t.hideturtle()
t.speed(10)

def square(side,angle):
    for i in range(4):
        t.fd(side)
        t.left(angle)

t.up()
t.goto(-400,300)
t.down()
square(100,90)
t.fd(100)
t.fillcolor("black")
t.begin_fill()

square(100,90)
t.end_fill()
turtle.done()