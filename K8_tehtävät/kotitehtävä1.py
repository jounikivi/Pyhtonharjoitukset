#2 Write a program to draw this. Assume the innermost square is 20 units per side, and each successive square is 20 units bigger, per side, than the one inside it.

def piirä_square(ttl, len):

  ttl.pendown()          
  for dummy in range(4):
    ttl.forward(len)
    ttl.left(90)
  ttl.penup()             
  ttl.backward(10)
  ttl.right(90)
  ttl.forward(10)
  ttl.left(90)


import turtle
window = turtle.Screen()
window.bgcolor('lightgreen')

alex = turtle.Turtle()
alex.color('red')
alex.pensize(3)

for i in range(4):
    piirä_square(alex, 20 + 20 * i)

window.mainloop()