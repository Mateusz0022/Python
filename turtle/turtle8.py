import turtle

turtle.setup(width=1000, height=1000, startx=0, starty=0)
t = turtle.Turtle()
t.hideturtle()
t.speed(1000)


def square(side, angle):
    for i in range(4):
        t.fd(side)
        t.left(angle)


def square_black(side, angle):
    t.fillcolor("black")
    t.begin_fill()
    for i in range(4):
        t.fd(side)
        t.left(angle)
    t.end_fill()


t.up()
t.goto(-400, 300)
t.down()

for i in range(4):
    for i in range(4):
        square(100, 90)
        t.fd(100)
        square_black(100, 90)
        t.fd(100)
    t.up()
    t.back(800)
    t.right(90)
    t.fd(100)
    t.left(90)
    t.down()
    for i in range(4):
        square_black(100, 90)
        t.fd(100)
        square(100, 90)
        t.fd(100)
    t.up()
    t.back(800)
    t.right(90)
    t.fd(100)
    t.left(90)
    t.down()
turtle.done()
