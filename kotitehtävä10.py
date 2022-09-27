#Kohdan 3.8 tehtävä 12
#Write a program to draw a face of a clock that looks something like this

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
tess.pensize(2)


for x in range(12):
    tess.left(30)
    tess.penup()
    tess.forward(70)
    tess.pendown()
    tess.forward(7)
    tess.penup()
    tess.forward(13)
    tess.stamp()
    tess.backward(90)


wn.mainloop()