import turtle 

turtle.setup(width=1000,height=1000,startx=0,starty=0)
t=turtle.Turtle()

def square(side,angle):
    for i in range(4):
        t.fd(side)
        t.left(angle)

square(200,90)

turtle.exitonclick()