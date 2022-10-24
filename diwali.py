import turtle
import math

c= ["green", "blue" , "red"]
t =turtle.pen()
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.color ("green")
turtle.width()
turtle.speed(18743359)
for i in range (1200):
    turtle.pencolor(c[i%3])
    turtle.width(i/20+1)
    turtle.fd(i/100+1)
    turtle.rt(120)
    turtle.fd(i)
    turtle.rt(144)
    turtle.fd(i)
    turtle.rt(144)

turtle.done()