# 4.Draw this pretty pattern.

def piirä_kuvio(t, n, sz):
  for dummy in range(n):
    t.forward(sz)
    t.left(360 / n)

import turtle
piirä = turtle.Turtle()
piirä.color('black')
piirä.pensize(5)

wn = turtle.Screen()
wn.title('Hieno kuvio')

for dummy in range(0, 20):
  piirä_kuvio(piirä, 4, 100)
  piirä.right(18)

wn.mainloop()