# 1.Write a void (non-fruitful) function to draw a square. Use it in a program to draw the image shown below. Assume each side is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the last square when the program ends.)

def piirä_neliöt(nm):
  for dummy in range(4):
    nm.forward(20)
    nm.left(90)

  nm.penup()
  nm.forward(40)
  nm.pendown()

import turtle

piirä = turtle.Turtle()
piirä.color('red')
piirä.pensize(4)
wn = turtle.Screen()
wn.bgcolor('lightgreen')

for dummy in range(5):
  piirä_neliöt(piirä)

wn.mainloop()