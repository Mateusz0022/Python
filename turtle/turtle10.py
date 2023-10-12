import turtle 
turtle.bgcolor("black")

t=turtle.Turtle()

turtle.setup(width=1200, height=1200, startx=-0, starty=0)

t.speed(10000000)
t.color("yellow")

t.pensize(6)
t.fillcolor("yellow")
t.begin_fill()
for i in range(360):
     t.fd(4)
     t.left(1)
t.end_fill()



for i in range(36):
     t.up()
     t.right(60)
     t.fd(20)
     t.down()
     t.fd(90)
     t.backward(90)
     t.up()
     t.backward(20)
     t.down()
     t.left(60)
     for i in range (10):
        t.fd(4)
        t.left(1)
     
     
# dac co dziesiąty

    
