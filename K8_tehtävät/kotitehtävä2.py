#3.Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular polygon. When called with draw_poly(tess, 8, 50), it will draw a shape like this:

def piirä_octagon(t, n, sz):
  for dummy in range(n):
    t.forward(sz)
    t.left(360 / n)

import turtle

piirä = turtle.Turtle()
piirä.color('darkblue')
piirä.pensize(2)

wn = turtle.Screen()
wn = turtle.bgcolor('lightgreen')

piirä_octagon(piirä, 8 , 50)

wn.mainloop()

