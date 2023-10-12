import turtle 

t=turtle.Turtle()

turtle.setup(width=1200, height=600, startx=-0, starty=0)

t.hideturtle()
t.up()
t.goto(-500,200)
t.down()
t.showturtle()

t.speed(5)

for i in range(16):
    t.fd(50)
    t.right(90)
    t.fd(90)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(90)
    t.right(90)

    



turtle.done()