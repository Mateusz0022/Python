import turtle

turtle.setup(width=1000,height=1000,startx=0,starty=0)
zolw=turtle.Turtle()

for i in range(10):
    zolw.fd(150)
    zolw.left(36)

zolw.speed(200)
for i in range(360):
    zolw.fd(2)
    zolw.left(1)

zolw.color("red")
for i in range(360):
    zolw.fd(3)
    zolw.right(1)

input()